# WinPR: Windows Portable Runtime
# Meson build script (mirrors winpr/CMakeLists.txt)
#
# Part of the unified FreeRDP build. WinPR shares the version source with
# FreeRDP, so the version variables computed in the root meson.build are reused.

winpr_version_major = freerdp_version_major
winpr_version_minor = freerdp_version_minor
winpr_version_revision = freerdp_version_revision
winpr_version_suffix = freerdp_version_suffix
winpr_version = freerdp_version
winpr_version_full = freerdp_version_full
winpr_api_version = freerdp_api_version
winpr_include_dir = 'include' / 'winpr@0@'.format(winpr_version_major)

############################################################
# WinPR option resolution (mirror winpr/CMakeLists.txt)
############################################################
native_sspi_default = is_windows  # WIN32 AND NOT UWP
with_native_sspi = get_option('with_native_sspi') and native_sspi_default

# Internal crypto defaults depend on the mbedTLS backend (CMake: *_DEFAULT)
with_internal_rc4 = with_mbedtls ? true : get_option('with_internal_rc4')
with_internal_md4 = with_mbedtls ? true : get_option('with_internal_md4')
with_internal_md5 = get_option('with_internal_md5')

with_winpr_deprecated = get_option('with_winpr_deprecated')
if with_winpr_deprecated
  add_project_arguments('-DWITH_WINPR_DEPRECATED', language : 'c')
endif

# PKCS11 default (CMake: ON unless win32/ios/android)
with_pkcs11 = not (is_windows or is_android)

############################################################
# Global WinPR compile definitions
############################################################
add_project_arguments('-DWINPR_EXPORTS', language : 'c')
if get_option('default_library') != 'static'
  add_project_arguments('-DWINPR_DLL', language : 'c')
endif
if not is_windows
  add_project_arguments('-DWINPR_CRITICAL_SECTION_DISABLE_SPINCOUNT', language : 'c')
endif
if with_pkcs11
  add_project_arguments('-DWITH_PKCS11', language : 'c')
endif

############################################################
# Feature detection (mirror the check_* calls in winpr/CMakeLists.txt)
############################################################
winpr_config = configuration_data()

# Headers
check_headers = {
  'WINPR_HAVE_FCNTL_H'      : 'fcntl.h',
  'WINPR_HAVE_UNISTD_H'     : 'unistd.h',
  'WINPR_HAVE_INTTYPES_H'   : 'inttypes.h',
  'WINPR_HAVE_STDBOOL_H'    : 'stdbool.h',
  'WINPR_HAVE_AIO_H'        : 'aio.h',
  'WINPR_HAVE_SYS_FILIO_H'  : 'sys/filio.h',
  'WINPR_HAVE_SYS_SELECT_H' : 'sys/select.h',
  'WINPR_HAVE_SYS_SOCKIO_H' : 'sys/sockio.h',
  'WINPR_HAVE_SYS_EVENTFD_H': 'sys/eventfd.h',
  'WINPR_HAVE_SYS_TIMERFD_H': 'sys/timerfd.h',
  'WINPR_HAVE_POLL_H'       : 'poll.h',
  'WINPR_HAVE_SYSLOG_H'     : 'syslog.h',
  'WINPR_HAVE_UNWIND_H'     : 'unwind.h',
}
foreach define, header : check_headers
  if cc.has_header(header)
    winpr_config.set(define, true)
  endif
endforeach

# c11 headers are mandatory (CMake: FATAL_ERROR otherwise)
foreach header : ['inttypes.h', 'stdint.h', 'stdbool.h']
  if not cc.has_header(header)
    error('C11 header ' + header + ' is required')
  endif
endforeach

# Functions
if cc.has_function('strndup', prefix : '#include <string.h>')
  winpr_config.set('WINPR_HAVE_STRNDUP', true)
endif
if cc.has_function('strerror_r', prefix : '#include <string.h>')
  winpr_config.set('WINPR_HAVE_STRERROR_R', true)
endif
if cc.has_function('getlogin_r', prefix : '#include <unistd.h>')
  winpr_config.set('WINPR_HAVE_GETLOGIN_R', true)
endif
if cc.has_function('getpwuid_r', prefix : '#include <pwd.h>')
  winpr_config.set('WINPR_HAVE_GETPWUID_R', true)
endif

# execinfo backtrace family (all three required, mirror CMake)
winpr_have_execinfo = false
if cc.has_header('execinfo.h')
  bt = cc.has_function('backtrace', prefix : '#include <execinfo.h>')
  bts = cc.has_function('backtrace_symbols', prefix : '#include <execinfo.h>')
  btsfd = cc.has_function('backtrace_symbols_fd', prefix : '#include <execinfo.h>')
  if bt and bts and btsfd
    winpr_have_execinfo = true
    winpr_config.set('WINPR_HAVE_EXECINFO_H', true)
  endif
endif

# Booleans reused by the utils module for conditional sources
winpr_have_syslog = cc.has_header('syslog.h')
winpr_have_unwind = cc.has_header('unwind.h')

# eventfd_read/write
if cc.has_header('sys/eventfd.h')
  if cc.has_function('eventfd_read', prefix : '#include <sys/eventfd.h>')
    winpr_config.set('WITH_EVENTFD_READ_WRITE', true)
  endif
endif

# pthread_mutex_timedlock
pthread_dep = cc.find_library('pthread', required : false)
if cc.has_function('pthread_mutex_timedlock', prefix : '#include <pthread.h>', dependencies : pthread_dep)
  winpr_config.set('WINPR_HAVE_PTHREAD_MUTEX_TIMEDLOCK', true)
endif

# struct tm.tm_gmtoff
if cc.has_member('struct tm', 'tm_gmtoff', prefix : '#include <time.h>')
  winpr_config.set('WINPR_HAVE_TM_GMTOFF', true)
endif

# ssize_t / SSIZE_T
if cc.has_type('ssize_t', prefix : '#include <sys/types.h>')
  winpr_config.set('WINPR_HAVE_SSIZE_T', true)
endif
if cc.has_type('SSIZE_T', prefix : '#include <BaseTsd.h>')
  winpr_config.set('WINPR_HAVE_WIN_SSIZE_T', true)
endif

# systemd journald (optional)
if cc.has_header('systemd/sd-journal.h')
  winpr_config.set('WINPR_HAVE_JOURNALD_H', true)
endif

# Option-driven defines
if with_native_sspi
  winpr_config.set('WITH_NATIVE_SSPI', true)
endif
if with_internal_rc4
  winpr_config.set('WITH_INTERNAL_RC4', true)
endif
if with_internal_md4
  winpr_config.set('WITH_INTERNAL_MD4', true)
endif
if with_internal_md5
  winpr_config.set('WITH_INTERNAL_MD5', true)
endif

# JSON support -> WITH_WINPR_JSON; gates WITH_AAD. Master selects one backend
# (jansson > json-c > cJSON) and compiles a matching json/<backend>.c, else a stub.
winpr_json_feature = get_option('with_winpr_json')
winpr_json_dep = dependency('', required : false)
winpr_json_define = ''
winpr_json_src = 'json/json-stub.c'
if winpr_json_feature.allowed()
  jansson_dep = dependency('jansson', required : false)
  jsonc_dep = dependency('json-c', required : false)
  cjson_dep = dependency('libcjson', required : false)
  if jansson_dep.found()
    winpr_json_dep = jansson_dep
    winpr_json_define = 'WITH_JANSSON'
    winpr_json_src = 'json/jansson.c'
  elif jsonc_dep.found()
    winpr_json_dep = jsonc_dep
    winpr_json_define = 'WITH_JSONC'
    winpr_json_src = 'json/json-c.c'
  elif cjson_dep.found()
    winpr_json_dep = cjson_dep
    winpr_json_define = 'WITH_CJSON'
    winpr_json_src = 'json/c-json.c'
  endif
endif
with_winpr_json = winpr_json_dep.found()
if winpr_json_feature.enabled() and not with_winpr_json
  error('with_winpr_json=enabled but neither cJSON nor json-c was found')
endif
if with_winpr_json
  winpr_config.set('WITH_WINPR_JSON', true)
endif

# WinPR debug switches (subset of debug_channels relevant to WinPR)
foreach dbg : ['ntlm', 'threads', 'events', 'mutex']
  if debug_channels.contains(dbg) or with_debug_all
    winpr_config.set('WITH_DEBUG_' + dbg.to_upper(), true)
  endif
endforeach

############################################################
# Template handles for config-header generation
############################################################
winpr_tmpl_version = files('include' / 'config' / 'version.h.in')
winpr_tmpl_buildconfig = files('include' / 'config' / 'build-config.h.in')
winpr_tmpl_buildflags = files('include' / 'config' / 'buildflags.h.in')
winpr_tmpl_config = files('include' / 'config' / 'config.h.in')
winpr_config_cmake_in = files('WinPRConfig.cmake.in')

# WinPR include search paths (source + generated)
winpr_inc = include_directories('include')

############################################################
# Library versioning (CMake: AddTargetWithResourceFile / WITH_LIBRARY_VERSIONING)
############################################################
with_library_versioning = get_option('with_library_versioning')

############################################################
# Sub-builds
# NOTE: libwinpr is processed before include/ (matching winpr/CMakeLists.txt)
# because the utils module's runtime detection (journald, PNG) feeds winpr/config.h.
############################################################
subdir('libwinpr')   # winpr library (populates winpr_config)
subdir('include')    # generates winpr/{version,build-config,buildflags,config}.h

# winpr-tools (CMake: WITH_WINPR_TOOLS; default ON for desktop non-mbedTLS builds)
tools_default = not is_android and not with_mbedtls
winpr_tools_feat = get_option('with_winpr_tools')
with_winpr_tools = winpr_tools_feat.enabled() or (winpr_tools_feat.auto() and tools_default)
winpr_tools_dep = dependency('', required : false)
if with_winpr_tools
  subdir('tools')
endif
