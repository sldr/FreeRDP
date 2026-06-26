#!/usr/bin/env python3
# FreeRDP: A Remote Desktop Protocol Implementation
#
# Compile-in resource generator for the SDL client, replacing the CMake
# file_to_hex_array() function (cmake/ConvertFileToHexArray.cmake) + the
# resource.{hpp,cpp}.in configure_file() pipeline + the resource-init.cpp
# writer in client/SDL/common/res/CMakeLists.txt.
#
# Subcommands:
#   all  <out_dir> <project> <hpp_in> <cpp_in> <types_csv> <infile> [<infile> ...]
#        Emits, into <out_dir>, every resource's <classname>.{hpp,cpp} plus a
#        single resource-init.cpp (SDLResourceManager::init()). Used as one
#        custom_target so all generated files share one output directory.
#        <types_csv> is a comma-separated list of class types (one per infile,
#        in order); infiles are passed via the custom_target's @INPUT@.
#   res  <out_dir> <project> <classtype> <infile> <hpp_in> <cpp_in>
#        Hex-encodes <infile> and emits <classname>.hpp / <classname>.cpp into
#        <out_dir> (classname = infile basename with non-alphanumerics -> '_',
#        matching the CMake REGEX REPLACE).
#   init <out_file> <classname> [<classname> ...]
#        Emits resource-init.cpp defining SDLResourceManager::init().
import os
import re
import sys


def classname_for(path):
    return re.sub(r'[^a-zA-Z0-9]', '_', os.path.basename(path))


def file_to_hex_array(path):
    with open(path, 'rb') as handle:
        data = handle.read()
    return ', '.join('0x{:02x}'.format(b) for b in data)


def cmd_res(argv):
    out_dir, project, classtype, infile, hpp_in, cpp_in = argv
    os.makedirs(out_dir, exist_ok=True)
    filename = os.path.basename(infile)
    classname = classname_for(infile)
    subst = {
        'PROJECT_NAME': project,
        'FILENAME': filename,
        'CLASSNAME': classname,
        'CLASSTYPE': classtype,
        'FILEDATA': file_to_hex_array(infile),
    }
    for template, ext in ((hpp_in, '.hpp'), (cpp_in, '.cpp')):
        with open(template, 'r', encoding='utf-8') as handle:
            content = handle.read()
        for key, value in subst.items():
            content = content.replace('@{}@'.format(key), value)
        with open(os.path.join(out_dir, classname + ext), 'w', encoding='utf-8') as handle:
            handle.write(content)


def cmd_init(argv):
    out_file = argv[0]
    classes = argv[1:]
    lines = ['#include <sdl_resource_manager.hpp>']
    lines += ['#include "{}.hpp"'.format(c) for c in classes]
    lines.append('void SDLResourceManager::init() {')
    lines += ['\t{}::init();'.format(c) for c in classes]
    lines.append('}')
    with open(out_file, 'w', encoding='utf-8') as handle:
        handle.write('\n'.join(lines) + '\n')


def cmd_all(argv):
    out_dir, project, hpp_in, cpp_in, types_csv = argv[:5]
    infiles = argv[5:]
    types = types_csv.split(',')
    if len(types) != len(infiles):
        raise SystemExit('types/infiles count mismatch: {} vs {}'.format(types, infiles))
    classes = []
    for classtype, infile in zip(types, infiles):
        cmd_res([out_dir, project, classtype, infile, hpp_in, cpp_in])
        classes.append(classname_for(infile))
    cmd_init([os.path.join(out_dir, 'resource-init.cpp')] + classes)


def main():
    cmd, argv = sys.argv[1], sys.argv[2:]
    if cmd == 'all':
        cmd_all(argv)
    elif cmd == 'res':
        cmd_res(argv)
    elif cmd == 'init':
        cmd_init(argv)
    else:
        raise SystemExit('unknown subcommand: ' + cmd)


if __name__ == '__main__':
    main()
