# FreeRDP: A Remote Desktop Protocol Implementation
# FreeRDP meson build script
#
# Licensed under the Apache License, Version 2.0 (the "License").
#
# This is the Meson port of the FreeRDP CMake build system. It is designed to
# coexist with the existing CMake build (CMakeLists.txt) and to reach feature,
# option and platform parity for the desktop tier-1 targets:
#   Linux (gcc/clang), Windows (MSVC + MinGW), macOS, FreeBSD.
#
# Mirrors: top-level CMakeLists.txt + cmake/ConfigOptions.cmake +
#          cmake/CommonConfigOptions.cmake + cmake/PlatformDefaults.cmake

project(
  'freerdp',
  'c',
  version : '3.16.0',
  license : 'Apache-2.0',
  meson_version : '>=1.3.0',
  default_options : [
    # gnu11, not c11: CMake sets CMAKE_C_EXTENSIONS ON (ProjectCStandard.cmake),
    # and WinPR/FreeRDP rely on POSIX/GNU extensions (fseeko, strndup, ...) that
    # strict -std=c11 hides behind __STRICT_ANSI__.
    'c_std=gnu11,c11',
    'cpp_std=gnu++17,c++17',
    'b_pie=true',
    'warning_level=2',
    'default_library=shared',
  ],
)

cc = meson.get_compiler('c')
# Objective-C is needed for the Apple-specific sources (WinPR crt unicode_apple.m,
# macOS client). Enabled only where an ObjC compiler exists.
add_languages('objc', native : false, required : host_machine.system() == 'darwin')
fs = import('fs')
host_system = host_machine.system()
cpu_family = host_machine.cpu_family()

is_windows = host_system == 'windows'
is_darwin = host_system == 'darwin'
is_linux = host_system == 'linux'
is_freebsd = host_system == 'freebsd'
is_openbsd = host_system == 'openbsd'
is_netbsd = host_system == 'netbsd'
is_dragonfly = host_system == 'dragonfly'
is_sunos = host_system == 'sunos'
is_bsd = is_freebsd or is_openbsd or is_netbsd or is_dragonfly
is_android = host_system == 'android'
is_unix = not is_windows

############################################################
# Version (mirror CMakeLists.txt regex / .source_tag / git logic)
############################################################
version_py = files('meson' / 'freerdp_version.py')
python = import('python').find_installation('python3', required : true)

use_git_version = get_option('use_version_from_git_tag')
version_res = run_command(
  python, version_py,
  meson.project_source_root(),
  '3.16.0',
  use_git_version ? '1' : '0',
  check : true,
)
version_parts = version_res.stdout().strip().split('\n')
freerdp_version_major = version_parts[0].strip()
freerdp_version_minor = version_parts[1].strip()
freerdp_version_revision = version_parts[2].strip()
freerdp_version_suffix = version_parts.length() > 3 ? version_parts[3].strip() : ''
git_revision = version_parts.length() > 4 ? version_parts[4].strip() : ''

freerdp_api_version = freerdp_version_major
freerdp_version = '@0@.@1@.@2@'.format(
  freerdp_version_major, freerdp_version_minor, freerdp_version_revision)
freerdp_version_full = freerdp_version_suffix != '' \
  ? '@0@-@1@'.format(freerdp_version, freerdp_version_suffix) \
  : freerdp_version
if git_revision == ''
  git_revision = freerdp_version
endif

message('FREERDP_VERSION=@0@'.format(freerdp_version_full))
message('Git Revision @0@'.format(git_revision))

# Versioned directory / install names (CMake: FREERDP_MAJOR_DIR)
freerdp_major_dir = 'freerdp@0@'.format(freerdp_version_major)
freerdp_include_dir = 'include' / freerdp_major_dir

############################################################
# Package identity (CMake: VENDOR / PRODUCT / PROJECT_URL)
############################################################
vendor = get_option('vendor')
product = get_option('product')
project_url = get_option('project_url')

############################################################
# Global compile definitions
############################################################
# Project-wide C arguments accumulated here and applied once at the end.
add_project_arguments('-DFREERDP_EXPORTS', language : 'c')
# MSVC compatibility with system headers (CMake: NONAMELESSUNION)
add_project_arguments('-DNONAMELESSUNION', language : 'c')

global_args = []
winpr_timezone_file = ''

if is_windows
  global_args += [
    '-DUNICODE', '-D_UNICODE',
    '-D_CRT_SECURE_NO_WARNINGS',
    '-DWIN32_LEAN_AND_MEAN',
    '-D_WINSOCK_DEPRECATED_NO_WARNINGS',
  ]
  win_ver = get_option('windows_version')
  win_ver_map = {
    'WINXP' : '0x0501',
    'WIN7'  : '0x0601',
    'WIN8'  : '0x0602',
    'WIN10' : '0x0A00',
  }
  win_ver_val = win_ver_map[win_ver]
  global_args += ['-DWINVER=@0@'.format(win_ver_val), '-D_WIN32_WINNT=@0@'.format(win_ver_val)]
elif is_linux
  global_args += '-D_FILE_OFFSET_BITS=64'
  winpr_timezone_file = '/etc/timezone'
elif is_freebsd or is_dragonfly
  global_args += [
    '-D_POSIX_C_SOURCE=200809L',
    '-D__BSD_VISIBLE',
    '-D_XOPEN_SOURCE=700',
    '-D_FILE_OFFSET_BITS=64',
  ]
  winpr_timezone_file = '/var/db/zoneinfo'
elif is_darwin
  global_args += ['-D_POSIX_C_SOURCE=200809L', '-D_DARWIN_C_SOURCE']
elif is_sunos
  global_args += '-D_POSIX_PTHREAD_SEMANTICS'
endif

# BSD fallback timezone file (CMake: WINPR_TIMEZONE_FILE default)
if winpr_timezone_file == ''
  winpr_timezone_file = '/var/db/zoneinfo'
endif
if is_unix
  global_args += '-DWINPR_TIMEZONE_FILE="@0@"'.format(winpr_timezone_file)
endif

# BSD: /usr/local prefixes (CMake: PlatformDefaults.cmake)
if is_bsd and fs.is_dir('/usr/local/include')
  add_project_arguments('-I/usr/local/include', language : 'c')
endif

if global_args.length() > 0
  add_project_arguments(global_args, language : 'c')
endif

############################################################
# Deprecated-symbol switches
############################################################
if get_option('with_freerdp_deprecated')
  add_project_arguments('-DWITH_FREERDP_DEPRECATED', language : 'c')
endif
without_freerdp_3x_deprecated = get_option('without_freerdp_3x_deprecated')
if without_freerdp_3x_deprecated
  add_project_arguments('-DWITHOUT_FREERDP_3x_DEPRECATED', language : 'c')
endif
if get_option('with_freerdp_deprecated_commandline')
  add_project_arguments('-DWITH_FREERDP_DEPRECATED_COMMANDLINE', language : 'c')
endif
if get_option('with_verbose_winpr_assert')
  add_project_arguments('-DWITH_VERBOSE_WINPR_ASSERT', language : 'c')
endif

############################################################
# X11 / Wayland availability (CMake: top-level WITH_X11 option gated by
# platform + Wayland feature). Actual dependency lookup happens where used.
############################################################
x11_feat = get_option('with_x11')
x11_default = not (is_windows or is_android or is_darwin)
with_x11 = x11_feat.enabled() or (x11_feat.auto() and x11_default)

wayland_feat = get_option('with_wayland')
wayland_default = is_unix and not is_darwin and not is_android
with_wayland = wayland_feat.enabled() or (wayland_feat.auto() and wayland_default)

# uwac (Unified Wayland Client lib) + Wayland frontend prerequisites:
# wayland-client, xkbcommon and the wayland-scanner code generator.
with_uwac = false
if with_wayland and not without_freerdp_3x_deprecated
  wayland_scanner_prog = find_program('wayland-scanner', required : wayland_feat.enabled())
  wayland_client_dep = dependency('wayland-client', required : wayland_feat.enabled())
  wayland_cursor_dep = dependency('wayland-cursor', required : false)
  xkbcommon_dep = dependency('xkbcommon', required : wayland_feat.enabled())
  with_uwac = wayland_scanner_prog.found() and wayland_client_dep.found() and xkbcommon_dep.found()
endif

############################################################
# Core dependencies
############################################################
# Threads (CMake: find_package(Threads REQUIRED))
threads_dep = dependency('threads')

# zlib, required when smartcard emulation is enabled
with_smartcard_emulate = get_option('with_smartcard_emulate')
zlib_dep = dependency('', required : false)
if with_smartcard_emulate
  zlib_dep = dependency('zlib', required : true)
  add_project_arguments('-DWITH_SMARTCARD_EMULATE', language : 'c')
endif

# dl (CMake: CMAKE_DL_LIBS; empty on Windows)
dl_dep = is_windows ? dependency('', required : false) : cc.find_library('dl', required : false)
# math
m_dep = cc.find_library('m', required : false)

# Crypto backend selection (CMake top-level: WITH_LIBRESSL / OpenSSL / MbedTLS)
with_libressl = get_option('with_libressl')
with_openssl = false
with_mbedtls = false
openssl_dep = dependency('', required : false)
mbedtls_dep = dependency('', required : false)

if with_libressl
  # LibreSSL exposes the OpenSSL API; use its pkg-config names.
  openssl_dep = dependency('libcrypto', 'libssl', required : true)
  with_openssl = true
  add_project_arguments('-DWITH_LIBRESSL', '-DWITH_OPENSSL', language : 'c')
else
  openssl_feature = get_option('with_openssl')
  openssl_dep = dependency('openssl', required : openssl_feature)
  with_openssl = openssl_dep.found()
  if with_openssl
    add_project_arguments('-DWITH_OPENSSL', language : 'c')
    message('Using OpenSSL Version: @0@'.format(openssl_dep.version()))
  endif
  mbedtls_feature = get_option('with_mbedtls')
  # mbedTLS has no canonical pkg-config in many distros; try, then fall back.
  mbedtls_dep = dependency('mbedtls', required : false)
  if not mbedtls_dep.found() and mbedtls_feature.allowed()
    mbedcrypto = cc.find_library('mbedcrypto', required : mbedtls_feature)
    if mbedcrypto.found()
      mbedtls_dep = declare_dependency(dependencies : [
        mbedcrypto,
        cc.find_library('mbedtls', required : false),
        cc.find_library('mbedx509', required : false),
      ])
    endif
  endif
  with_mbedtls = mbedtls_dep.found()
  if with_mbedtls
    add_project_arguments('-DWITH_MBEDTLS', language : 'c')
  endif
endif

############################################################
# Install path layout (CMake: FREERDP_*_PATH, GNUInstallDirs)
############################################################
prefix = get_option('prefix')
bindir = get_option('bindir')
libdir = get_option('libdir')
datadir = get_option('datadir')
includedir = get_option('includedir')

# WITH_ABSOLUTE_PLUGIN_LOAD_PATHS default differs for Android/Windows/macOS bundle.
abs_plugin_default = not (is_android or is_windows)
abs_plugin_opt = get_option('with_absolute_plugin_load_paths')
with_absolute_plugin_load_paths = abs_plugin_opt.auto() \
  ? abs_plugin_default \
  : abs_plugin_opt.enabled()

if not with_absolute_plugin_load_paths
  freerdp_data_path = 'share'
  freerdp_install_prefix = '.'
  freerdp_library_path = '.'
  freerdp_plugin_path = '.'
else
  freerdp_data_path = prefix / 'share' / freerdp_major_dir
  freerdp_install_prefix = prefix
  freerdp_library_path = libdir
  freerdp_plugin_path = is_windows \
    ? bindir / freerdp_major_dir \
    : libdir / freerdp_major_dir
endif
freerdp_addin_path = freerdp_plugin_path
freerdp_extension_postfix = freerdp_major_dir / 'extensions'
freerdp_extension_rel_path = libdir / freerdp_extension_postfix

# Proxy plugins directory (CMake: PROXY_PLUGINDIR / FREERDP_PROXY_PLUGINDIR)
proxy_plugindir_opt = get_option('proxy_plugindir')
freerdp_proxy_plugindir = proxy_plugindir_opt != '' \
  ? proxy_plugindir_opt \
  : freerdp_plugin_path / 'proxy'

############################################################
# Target architecture (CMake: TARGET_ARCH in ConfigOptions.cmake)
############################################################
if cpu_family == 'x86'
  target_arch = 'x86'
elif cpu_family == 'x86_64'
  target_arch = 'x64'
elif cpu_family.startswith('arm') or cpu_family == 'aarch64'
  target_arch = 'ARM'
elif cpu_family == 'sparc' or cpu_family == 'sparc64'
  target_arch = 'sparc'
elif cpu_family == 'e2k'
  target_arch = 'e2k'
else
  target_arch = cpu_family
endif

# Shared library affixes (CMake: CMAKE_SHARED_LIBRARY_PREFIX/SUFFIX)
if is_windows
  shared_lib_prefix = ''
  shared_lib_suffix = '.dll'
elif is_darwin
  shared_lib_prefix = 'lib'
  shared_lib_suffix = '.dylib'
else
  shared_lib_prefix = 'lib'
  shared_lib_suffix = '.so'
endif

############################################################
# Global compiler flags / visibility (Phase 1)
# Replaces cmake/CompilerFlags.cmake, CommonCompilerFlags.cmake,
# ExportAllSymbols.cmake. Sanitizers/LTO/PIC/ccache use Meson built-ins
# (b_sanitize / b_lto / b_staticpic / b_ccache) set via -D on the command line.
############################################################
common_c_args = []
if cc.get_id() == 'msvc'
  common_c_args += ['/utf-8']
else
  # Always keep frame pointers + a few portability warnings, mirroring
  # cmake/CompilerFlags.cmake / CommonCompilerFlags.cmake.
  candidate_args = [
    '-fno-omit-frame-pointer',
    '-Wredundant-decls',
  ]
  common_c_args += cc.get_supported_arguments(candidate_args)
endif
if common_c_args.length() > 0
  add_project_arguments(common_c_args, language : 'c')
endif

# SIMD per-file compiler flags (CMake: cmake/DetectIntrinsicSupport.cmake
# set_simd_source_file_properties). Maps an intrinsic level to the c_args used
# to compile that group of sources. Empty list => sources compile with no extra
# flag (they are #if-guarded to be empty on the wrong architecture).
simd_flags = {}
if cc.get_id() == 'msvc'
  if cpu_family == 'x86'
    simd_flags = {'avx2' : ['/arch:AVX2']}
  elif cpu_family == 'x86_64'
    simd_flags = {'sse4.2' : ['/arch:SSE4.2'], 'avx2' : ['/arch:AVX2']}
  endif
elif cc.get_id() in ['gcc', 'clang']
  if cpu_family in ['x86', 'x86_64']
    simd_flags = {
      'sse2' : ['-msse2'], 'sse3' : ['-msse3'], 'ssse3' : ['-mssse3'],
      'sse4.1' : ['-msse4.1'], 'sse4.2' : ['-msse4.2'], 'avx2' : ['-mavx2'],
    }
  elif cpu_family == 'arm'
    simd_flags = {'neon' : ['-mfpu=neon']}
  elif cpu_family == 'aarch64'
    simd_flags = {'neon' : []}  # NEON is baseline on AArch64, no flag needed
  endif
endif

# Symbol visibility (CMake: ExportAllSymbols.cmake)
export_all_symbols = get_option('export_all_symbols')
if export_all_symbols
  add_project_arguments('-DEXPORT_ALL_SYMBOLS', language : 'c')
endif
# Per-target gnu_symbol_visibility:'hidden' is applied in library definitions
# unless export_all_symbols is set.
default_symbol_visibility = export_all_symbols ? 'default' : 'hidden'

############################################################
# Debug message switches (CMake: WITH_DEBUG_*)
############################################################
with_debug_all = get_option('with_debug_all')
debug_channels = get_option('debug_channels')

############################################################
# Build configuration string (CMake: FREERDP_BUILD_CONFIG)
############################################################
freerdp_build_config_list = []

############################################################
# Template / generator file handles (created here where the relative paths
# are valid; consumed by include/freerdp/meson.build).
############################################################
# FreeRDP public include dir (source include/ + generated build/include/).
# Defined here so libfreerdp and later phases can use it before include/ runs.
freerdp_public_inc = include_directories('include')

gen_settings_py = files('meson' / 'gen_settings_keys.py')
tmpl_version_h = files('include' / 'config' / 'version.h.in')
tmpl_buildconfig_h = files('include' / 'config' / 'build-config.h.in')
tmpl_config_h = files('include' / 'config' / 'config.h.in')
tmpl_buildflags_h = files('include' / 'config' / 'buildflags.h.in')
tmpl_settings_keys_h = files('include' / 'config' / 'settings_keys.h.in')
settings_types_private_h = files('include' / 'freerdp' / 'settings_types_private.h')
gen_channel_tables_py = files('meson' / 'gen_channel_tables.py')
tmpl_channel_tables = files('channels' / 'client' / 'tables.c.in')
tmpl_oss_includes = files('cmake' / 'oss-includes.h.in')

############################################################
# config.h data (CMake: include/config/config.h.in via #cmakedefine).
# Only TRUE entries are set; unset entries become "/* #undef X */".
# Populated further by later phases (winpr/libfreerdp/channels) before the
# header is generated in include/meson.build (added last).
############################################################
config_h = configuration_data()

with_opaque_settings = without_freerdp_3x_deprecated
if with_opaque_settings
  config_h.set('WITH_OPAQUE_SETTINGS', true)
endif

# Options known at this stage
opt_to_define = {
  'WITH_PROFILER'         : get_option('with_profiler'),
  'WITH_GPROF'            : get_option('with_gprof'),
  'WITH_SIMD'             : get_option('with_simd'),
  'WITH_JPEG'             : get_option('with_jpeg'),
  'WITH_CAIRO'            : get_option('with_cairo'),
  'WITH_SWSCALE'          : get_option('with_swscale'),
  'WITH_DSP_EXPERIMENTAL' : get_option('with_dsp_experimental'),
  'WITH_CHANNELS'         : get_option('with_channels'),
  'WITH_CLIENT_CHANNELS'  : get_option('with_channels') and get_option('with_client_channels'),
  'WITH_SERVER_CHANNELS'  : get_option('with_channels') and get_option('with_server_channels'),
}
foreach name, val : opt_to_define
  if val
    config_h.set(name, true)
  endif
endforeach
if get_option('with_simd') and get_option('with_avx2')
  config_h.set('WITH_AVX2', true)
endif
if is_windows and get_option('with_win8')
  config_h.set('WITH_WIN8', true)
endif
if is_windows and get_option('with_media_foundation')
  config_h.set('WITH_MEDIA_FOUNDATION', true)
endif

# Debug flags
foreach dbg : debug_channels
  config_h.set('WITH_DEBUG_' + dbg.to_upper(), true)
endforeach
if with_debug_all
  foreach dbg : get_option('debug_channels').choices()
    config_h.set('WITH_DEBUG_' + dbg.to_upper(), true)
  endforeach
endif

############################################################
# version.h / build-config.h / buildflags.h data
############################################################
version_data = configuration_data()
version_data.set('FREERDP_VERSION_MAJOR', freerdp_version_major)
version_data.set('FREERDP_VERSION_MINOR', freerdp_version_minor)
version_data.set('FREERDP_VERSION_REVISION', freerdp_version_revision)
version_data.set('FREERDP_VERSION_SUFFIX', freerdp_version_suffix)
version_data.set('FREERDP_API_VERSION', freerdp_api_version)
version_data.set('FREERDP_VERSION', freerdp_version)
version_data.set('FREERDP_VERSION_FULL', freerdp_version_full)
version_data.set('GIT_REVISION', git_revision)
version_data.set('VENDOR', vendor)
version_data.set('PRODUCT', product)

# Keymap path (CMake sets FREERDP_KEYMAP_PATH; refined in Phase 3/locale)
freerdp_keymap_path = ''

buildconfig_data = configuration_data()
buildconfig_data.set('NATIVE_FREERDP_DATA_PATH', freerdp_data_path)
buildconfig_data.set('NATIVE_FREERDP_KEYMAP_PATH', freerdp_keymap_path)
buildconfig_data.set('NATIVE_FREERDP_PLUGIN_PATH', freerdp_plugin_path)
buildconfig_data.set('NATIVE_FREERDP_INSTALL_PREFIX', freerdp_install_prefix)
buildconfig_data.set('NATIVE_FREERDP_LIBRARY_PATH', freerdp_library_path)
buildconfig_data.set('NATIVE_FREERDP_ADDIN_PATH', freerdp_addin_path)
buildconfig_data.set('NATIVE_FREERDP_PROXY_PLUGINDIR', freerdp_proxy_plugindir)
buildconfig_data.set('CMAKE_SHARED_LIBRARY_SUFFIX', shared_lib_suffix)
buildconfig_data.set('CMAKE_SHARED_LIBRARY_PREFIX', shared_lib_prefix)
buildconfig_data.set('VENDOR', vendor)
buildconfig_data.set('PRODUCT', product)

# buildflags.h is generated in include/meson.build once the full build config
# list has been accumulated by all sub-builds.

############################################################
# Staged subdirectories (added per implementation phase)
############################################################
# Phase 2: WinPR (config headers generated now; library modules pending)
if get_option('unified_build')
  subdir('winpr')
endif

# Phase 3: libfreerdp (depends on winpr_dep)
subdir('libfreerdp')

# uwac (Unified Wayland Client) — deprecated-3x, built when Wayland is available.
if with_uwac
  subdir('uwac')
endif

# Phase 4: channels (build virtual channel plugins + static dispatch tables)
freerdp_channels_client_dep = dependency('', required : false)
freerdp_channels_server_dep = dependency('', required : false)
if get_option('with_channels')
  subdir('channels')
endif

# Phase 5: clients (frontends are Phase 5b)
if get_option('with_client_common') or get_option('with_client')
  subdir('client')
endif
# Phase 5b: rdtk toolkit (CMake: unified build, WITH_SERVER && WITH_RDTK) — used by shadow
if get_option('with_server') and get_option('with_rdtk')
  subdir('rdtk')
endif

# Phase 5b: servers (shadow/proxy/Windows are further 5b work)
if get_option('with_server')
  subdir('server')
endif

# Phase 1: config headers. Generated last in CMake (after all WITH_*/CHANNEL_*
# are known); kept here for now and re-ordered when later phases land.
subdir('include')

############################################################
# Configuration summary
############################################################
summary({
  'Version'        : freerdp_version_full,
  'Git revision'   : git_revision,
  'Host system'    : host_system,
  'CPU family'     : cpu_family,
  'OpenSSL'        : with_openssl,
  'mbedTLS'        : with_mbedtls,
  'LibreSSL'       : with_libressl,
  'Smartcard emul' : with_smartcard_emulate,
  'Plugin path'    : freerdp_plugin_path,
}, section : 'FreeRDP')
