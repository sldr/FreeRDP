#!/usr/bin/env python3
# FreeRDP: A Remote Desktop Protocol Implementation
#
# Generate channels/client/tables.c from collected static-channel metadata.
# This replaces the CMake string-building in channels/client/CMakeLists.txt
# (the @CLIENT_STATIC_*@ substitutions in channels/client/tables.c.in).
#
# Usage: gen_channel_tables.py <metadata> <tables.c.in> <output tables.c>
#
# <metadata> is either a path to a JSON file or a literal JSON string with the
# schema:
#   {
#     "modules": [
#       {"channel": "echo", "name": "echo-client",
#        "entries": ["DVCPluginEntry"], "subsystems": ["alsa", "pulse-foo"]},
#       ...
#     ]
#   }
import json
import os
import sys


def entry_kind(entry):
    """Return (C type, initializer field, import signature) for an entry point."""
    if entry == 'VirtualChannelEntry':
        return ('STATIC_ENTRY_VC', '.csevc',
                'extern BOOL VCAPITYPE {n}(PCHANNEL_ENTRY_POINTS);')
    if entry == 'VirtualChannelEntryEx':
        return ('STATIC_ENTRY_VCEX', '.csevcex',
                'extern BOOL VCAPITYPE {n}(PCHANNEL_ENTRY_POINTS,PVOID);')
    if entry.endswith('DVCPluginEntry'):
        return ('STATIC_ENTRY_DVC', '.csedvc',
                'extern UINT VCAPITYPE {n}(IDRDYNVC_ENTRY_POINTS* pEntryPoints);')
    if entry.endswith('DeviceServiceEntry'):
        return ('STATIC_ENTRY_DSE', '.csedse',
                'extern UINT VCAPITYPE {n}(PDEVICE_SERVICE_ENTRY_POINTS pEntryPoints);')
    return ('STATIC_ENTRY', '.cse', 'extern UINT VCAPITYPE {n}(void);')


def main():
    meta_arg, template_path, output_path = sys.argv[1], sys.argv[2], sys.argv[3]
    if os.path.isfile(meta_arg):
        with open(meta_arg, 'r', encoding='utf-8') as handle:
            data = json.load(handle)
    else:
        data = json.loads(meta_arg)
    modules = data.get('modules', [])

    # Unique ordered list of entry-point kinds (CHANNEL_STATIC_CLIENT_ENTRIES)
    entries = []
    for mod in modules:
        for entry in mod['entries']:
            if entry not in entries:
                entries.append(entry)

    imports = ''
    tables = ''
    tables_list = ('\nextern const STATIC_ENTRY_TABLE CLIENT_STATIC_ENTRY_TABLES[];\n'
                   'const STATIC_ENTRY_TABLE CLIENT_STATIC_ENTRY_TABLES[] =\n{')

    for entry in entries:
        ctype, initializer, sig = entry_kind(entry)
        entry_imports = ''
        entry_table = ''
        for mod in modules:
            if entry in mod['entries']:
                name = '{}_{}'.format(mod['channel'], entry)
                entry_imports += '\n' + sig.format(n=name)
                entry_table += '\n\t{{ "{}", {} }},'.format(mod['channel'], name)
        imports += '\n' + entry_imports
        tables += '\nextern const {t} CLIENT_{e}_TABLE[];\n'.format(t=ctype, e=entry)
        tables += 'const {t} CLIENT_{e}_TABLE[] =\n{{'.format(t=ctype, e=entry)
        tables += '\n' + entry_table
        tables += '\n\t{ NULL, NULL }\n};'
        tables_list += '\n\t{{ "{e}", {{ {i} = CLIENT_{e}_TABLE }} }},'.format(
            e=entry, i=initializer)
    tables_list += '\n\t{ NULL, { .cse = NULL } }\n};'

    # Addin + subsystem tables
    subsystem_imports = ''
    subsystem_tables = ''
    addin = ('extern const STATIC_ADDIN_TABLE CLIENT_STATIC_ADDIN_TABLE[];\n'
             'const STATIC_ADDIN_TABLE CLIENT_STATIC_ADDIN_TABLE[] =\n{')
    for mod in modules:
        channel = mod['channel']
        sub_table_name = 'CLIENT_{}_SUBSYSTEM_TABLE'.format(channel.upper())
        sub_table = ('extern const STATIC_SUBSYSTEM_ENTRY {n}[];\n'
                     'const STATIC_SUBSYSTEM_ENTRY {n}[] =\n{{').format(n=sub_table_name)
        for subsystem in mod.get('subsystems', []):
            if '-' in subsystem:
                sub_name, sub_type = subsystem.split('-', 1)
            else:
                sub_name, sub_type = subsystem, ''
            if sub_type:
                sub_entry = '{s}_freerdp_{c}_client_{t}_subsystem_entry'.format(
                    s=sub_name, c=channel, t=sub_type)
            else:
                sub_entry = '{s}_freerdp_{c}_client_subsystem_entry'.format(
                    s=sub_name, c=channel)
            sub_table += '\n\t{{ "{n}", "{t}", {e} }},'.format(
                n=sub_name, t=sub_type, e=sub_entry)
            subsystem_imports += '\nextern UINT VCAPITYPE {}(void*);'.format(sub_entry)
        sub_table += '\n\t{ NULL, NULL, NULL }\n};'
        subsystem_tables += '\n' + sub_table

        for entry in mod['entries']:
            _, initializer, _ = entry_kind(entry)
            name = '{}_{}'.format(channel, entry)
            addin += ('\n\t{{ "{c}", "{e}", {{ {i} = {n} }}, {s} }},').format(
                c=channel, e=entry, i=initializer, n=name, s=sub_table_name)
    addin += '\n\t{ NULL, NULL, { .cse = NULL }, NULL }\n};'

    with open(template_path, 'r', encoding='utf-8') as handle:
        content = handle.read()

    replacements = {
        '${CLIENT_STATIC_TYPEDEFS}': '',
        '${CLIENT_STATIC_ENTRY_IMPORTS}': imports,
        '${CLIENT_STATIC_SUBSYSTEM_IMPORTS}': subsystem_imports,
        '${CLIENT_STATIC_ENTRY_TABLES}': tables,
        '${CLIENT_STATIC_ENTRY_TABLES_LIST}': tables_list,
        '${CLIENT_STATIC_SUBSYSTEM_TABLES}': subsystem_tables,
        '${CLIENT_STATIC_ADDIN_TABLE}': addin,
    }
    for key, val in replacements.items():
        content = content.replace(key, val)

    with open(output_path, 'w', encoding='utf-8') as handle:
        handle.write(content)


if __name__ == '__main__':
    main()
