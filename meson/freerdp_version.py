#!/usr/bin/env python3
# FreeRDP: A Remote Desktop Protocol Implementation
#
# Determine the FreeRDP version, mirroring the logic in the top-level
# CMakeLists.txt:
#   1. If <source>/.source_tag exists, use its contents.
#   2. Else, if use_version_from_git_tag is requested, use `git describe`.
#   3. Else, fall back to the hard-coded RAW_VERSION_STRING.
#
# The version string is parsed with the same regex CMake uses:
#   ^(.*)([0-9]+)\.([0-9]+)\.([0-9]+)-?(.*)
# and the four components MAJOR MINOR REVISION SUFFIX are printed, one per
# line (the SUFFIX line may be empty). A 5th line carries the git revision.
#
# Usage: freerdp_version.py <source_dir> <default_version> <use_git: 0|1>
import os
import re
import subprocess
import sys

VERSION_REGEX = re.compile(r"^(.*?)([0-9]+)\.([0-9]+)\.([0-9]+)-?(.*)$")


def _git(source_dir, *args):
    try:
        out = subprocess.run(
            ["git", "-C", source_dir, *args],
            capture_output=True, text=True, check=True,
        )
        return out.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        return ""


def main():
    source_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    raw = sys.argv[2] if len(sys.argv) > 2 else "3.16.0"
    use_git = (sys.argv[3] if len(sys.argv) > 3 else "1") == "1"

    source_tag = os.path.join(source_dir, ".source_tag")
    git_revision = ""

    if os.path.isfile(source_tag):
        with open(source_tag, "r", encoding="utf-8") as handle:
            raw = handle.read().strip()
    elif use_git:
        tag = _git(source_dir, "describe", "--tags", "--always")
        if tag and VERSION_REGEX.match(tag):
            raw = tag

    raw = raw.strip()

    # Git revision (mirrors .source_version / git_get_exact_tag / git_rev_parse)
    source_version = os.path.join(source_dir, ".source_version")
    if os.path.isfile(source_version):
        with open(source_version, "r", encoding="utf-8") as handle:
            git_revision = handle.read().strip()
    elif use_git:
        git_revision = _git(source_dir, "describe", "--tags", "--always")
        if not git_revision:
            git_revision = _git(source_dir, "rev-parse", "--short", "HEAD")

    match = VERSION_REGEX.match(raw)
    if not match:
        sys.stderr.write("Unable to parse version string '{}'\n".format(raw))
        sys.exit(1)

    major, minor, revision, suffix = match.group(2, 3, 4, 5)
    if not git_revision:
        git_revision = "{}.{}.{}".format(major, minor, revision)

    print(major)
    print(minor)
    print(revision)
    print(suffix)
    print(git_revision)


if __name__ == "__main__":
    main()
