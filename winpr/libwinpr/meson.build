# WinPR library (mirrors winpr/libwinpr/CMakeLists.txt)
#
# The CMake build accumulates sources/libs/includes from each module subdir via
# the winpr_module_add() PARENT_SCOPE pattern, then builds a single library.
# Meson's subdir() shares scope, so module meson.build files simply append to
# the accumulator arrays declared here.

# Accumulators (CMake: WINPR_SRCS / WINPR_LIBS_* / WINPR_DEFINITIONS / ...)
winpr_srcs = []
winpr_priv_deps = [threads_dep]
winpr_pub_deps = []
winpr_defs = []
winpr_c_args = []
winpr_link_args = []
# winpr_inc = include_directories('include') already covers both the source
# public headers and the generated config headers (build/winpr/include).
winpr_incs = [winpr_inc]

dl_dep_winpr = is_windows ? dependency('', required : false) : cc.find_library('dl', required : false)
if dl_dep_winpr.found()
  winpr_priv_deps += dl_dep_winpr
endif

# Shared crypto backends (resolved in the root meson.build)
if with_openssl
  winpr_priv_deps += openssl_dep
endif
if with_mbedtls
  winpr_priv_deps += mbedtls_dep
endif

############################################################
# Library-wide optional dependencies
############################################################
# uriparser (CMake: WITH_URIPARSER, default = found)
uriparser_dep = dependency('liburiparser', required : false)
if uriparser_dep.found()
  winpr_priv_deps += uriparser_dep
  winpr_defs += 'WITH_URIPARSER'
endif

# POSIX timers -> librt (CMake: timer_create/delete/settime/gettime)
if not is_windows
  if cc.has_function('timer_create', prefix : '#include <time.h>') \
     and cc.has_function('timer_settime', prefix : '#include <time.h>')
    winpr_defs += 'WITH_POSIX_TIMER'
    rt_dep = cc.find_library('rt', required : false)
    if rt_dep.found()
      winpr_priv_deps += rt_dep
    endif
  endif
endif

# pthread_setschedprio
if cc.has_function('pthread_setschedprio', prefix : '#include <pthread.h>', dependencies : pthread_dep)
  winpr_defs += 'PTHREAD_SETSCHEDPRIO'
endif

# Android logging
if is_android
  winpr_priv_deps += cc.find_library('log', required : true)
endif

############################################################
# Module subdirectories (CMake: WINPR_CORE + WINPR_LEVEL2)
############################################################
winpr_core_modules = [
  'synch', 'library', 'file', 'comm', 'credentials', 'pipe', 'interlocked', 'security',
  'environment', 'crypto', 'registry', 'path', 'io', 'memory', 'ncrypt',
  'input', 'shell', 'utils', 'error', 'timezone', 'sysinfo', 'pool', 'handle',
  'thread',
]
winpr_level2_modules = [
  'winsock', 'sspi', 'sspicli', 'crt', 'bcrypt', 'rpc', 'wtsapi', 'dsparse',
  'smartcard', 'nt', 'clipboard',
]
foreach m : winpr_core_modules + winpr_level2_modules
  subdir(m)
endforeach

############################################################
# Crypto backend requirement (CMake: FATAL_ERROR if none)
############################################################
if not (with_openssl or with_mbedtls or with_libressl)
  error('WinPR requires a crypto backend: OpenSSL, LibreSSL or mbedTLS (none found/enabled)')
endif

############################################################
# Build the winpr library (CMake: AddTargetWithResourceFile + install)
############################################################
winpr_libname = with_library_versioning ? 'winpr@0@'.format(winpr_version_major) : 'winpr'
winpr_lib_kwargs = {}
if with_library_versioning
  winpr_lib_kwargs += {'version' : winpr_version, 'soversion' : winpr_version_major}
else
  winpr_lib_kwargs += {'name_prefix' : ''}
endif

if get_option('with_resource_versioning')
  winpr_defs += 'WITH_RESOURCE_VERSIONING'
endif

# Private compile definitions (CMake: WINPR_DEFINITIONS, stored as bare macro names)
winpr_def_args = []
foreach d : winpr_defs
  winpr_def_args += '-D' + d
endforeach

winpr_lib = library(
  winpr_libname,
  winpr_srcs,
  include_directories : winpr_incs,
  dependencies : winpr_priv_deps + winpr_pub_deps,
  c_args : winpr_def_args + winpr_c_args,
  link_args : winpr_link_args,
  gnu_symbol_visibility : default_symbol_visibility,
  install : true,
  kwargs : winpr_lib_kwargs,
)

# Public dependency object reused by libfreerdp / channels / clients / servers.
winpr_dep = declare_dependency(
  link_with : winpr_lib,
  include_directories : winpr_inc,
  dependencies : winpr_pub_deps,
)

############################################################
# pkg-config (CMake: winpr.pc.in via pkgconfig module)
############################################################
pkgconfig = import('pkgconfig')
pkgconfig.generate(
  winpr_lib,
  name : 'WinPR',
  description : 'WinPR: Windows Portable Runtime',
  url : 'http://www.freerdp.com/',
  version : winpr_version,
  filebase : 'winpr@0@'.format(winpr_version_major),
  subdirs : 'winpr@0@'.format(winpr_version_major),
)

# CMake find_package(WinPR) package
cmake_packages += [{
  'name' : 'WinPR',
  'version' : winpr_version,
  'cmake_subdir' : 'WinPR@0@'.format(winpr_version_major),
  'template' : winpr_config_cmake_in,
  'targets' : 'winpr,@0@,@1@'.format(
    libdir / (shared_lib_prefix + winpr_libname + shared_lib_suffix), winpr_include_dir),
  'vars' : [
    'BUILD_SHARED_LIBS=' + (get_option('default_library') == 'static' ? 'OFF' : 'ON'),
    'WITH_JSON_DISABLED=OFF',
    'JSONC_FOUND=' + (winpr_json_define == 'WITH_JSONC' ? 'ON' : ''),
    'CJSON_FOUND=' + (winpr_json_define == 'WITH_CJSON' ? 'ON' : ''),
    'WITH_CJSON_REQUIRED=OFF',
    'WITH_URIPARSER=' + (uriparser_dep.found() ? 'ON' : 'OFF'),
    'WINPR_VERSION_MAJOR=' + winpr_version_major,
    'WINPR_VERSION_MINOR=' + winpr_version_minor,
    'WINPR_VERSION_REVISION=' + winpr_version_revision,
    'WITH_WINPR_JSON=' + (with_winpr_json ? 'ON' : 'OFF'),
    'PACKAGE_WINPR_INCLUDE_DIR=${PACKAGE_PREFIX_DIR}/' + winpr_include_dir,
  ],
}]
