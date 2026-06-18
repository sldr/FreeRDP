#!/usr/bin/env python3
# FreeRDP: A Remote Desktop Protocol Implementation
#
# Generate include/freerdp/settings_keys.h from settings_types_private.h.
#
# This mirrors the parsing logic in include/CMakeLists.txt: every
# SETTINGS_DEPRECATED(ALIGN64 <type> <Name>); /* <index> */ line is turned into
# an enum entry "FreeRDP_<Name> = <index>", grouped by the C type into the
# matching FreeRDP_Settings_Keys_* enumeration.
#
# Usage: gen_settings_keys.py <settings_types_private.h> <settings_keys.h.in> <output>
import re
import sys

# Capture: type (may end with '*'), member name, decimal index from the comment.
ENTRY_RE = re.compile(
    r"SETTINGS_DEPRECATED\(\s*ALIGN64\s+(.+?)\s+(\w+)\)\s*;.*?/\*+\s*(\d+)"
)

GROUPS = [
    "BOOL", "INT16", "UINT16", "INT32", "UINT32",
    "INT64", "UINT64", "STRING", "POINTER",
]


def classify(ctype):
    ctype = ctype.strip()
    if ctype in ("BOOL", "INT16", "UINT16", "INT32", "UINT32", "INT64", "UINT64"):
        return ctype
    if "*" in ctype:
        base = ctype.replace("*", "").strip().lower()
        if base in ("char", ""):
            return "STRING"
        return "POINTER"
    return "POINTER"


def main():
    src, template, output = sys.argv[1], sys.argv[2], sys.argv[3]
    keys = {name: [] for name in GROUPS}

    with open(src, "r", encoding="utf-8") as handle:
        for line in handle:
            if "ALIGN64" not in line:
                continue
            match = ENTRY_RE.search(line)
            if not match:
                continue
            ctype, name, index = match.group(1), match.group(2), match.group(3)
            keys[classify(ctype)].append("FreeRDP_{} = {}".format(name, index))

    for name in GROUPS:
        keys[name].append("FreeRDP_{}_UNUSED = -1".format(name))

    with open(template, "r", encoding="utf-8") as handle:
        content = handle.read()

    for name in GROUPS:
        content = content.replace(
            "@SETTINGS_KEYS_{}@".format(name),
            ",\n\t".join(keys[name]),
        )

    with open(output, "w", encoding="utf-8") as handle:
        handle.write(content)


if __name__ == "__main__":
    main()
