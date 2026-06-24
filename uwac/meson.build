# UWAC: Using Wayland As Client (mirrors uwac/CMakeLists.txt)
# Deprecated-3x library used by the Wayland client. Versioned independently (0.2.0).

uwac_version_major = '0'
uwac_version_minor = '2'
uwac_version_revision = '0'
uwac_version = '@0@.@1@.@2@'.format(uwac_version_major, uwac_version_minor, uwac_version_revision)
uwac_version_full = uwac_version
uwac_api_version = uwac_version_major
uwac_include_dir = 'include' / 'uwac@0@'.format(uwac_api_version)

uwac_inc = include_directories('include')

# Region backend: PIXMAN or (unified build) FreeRDP. Default = FreeRDP.
uwac_have_pixman_region = false

# Feature detection (CMake: check_* -> uwac config.h)
uwac_config = configuration_data()
if cc.has_member('struct tm', 'tm_gmtoff', prefix : '#include <time.h>')
  uwac_config.set('UWAC_HAVE_TM_GMTOFF', true)
endif
if cc.has_header('poll.h')
  uwac_config.set('UWAC_HAVE_POLL_H', true)
endif
if cc.has_header('syslog.h')
  uwac_config.set('UWAC_HAVE_SYSLOG_H', true)
endif
if cc.has_function('strerror_r', prefix : '#include <string.h>')
  uwac_config.set('UWAC_HAVE_STRERROR_R', true)
endif
if uwac_have_pixman_region
  uwac_config.set('UWAC_HAVE_PIXMAN_REGION', true)
endif

# Wayland protocol XMLs (codegen happens in libuwac via wayland-scanner)
uwac_proto_names = [
  'xdg-shell', 'viewporter', 'xdg-decoration-unstable-v1', 'server-decoration',
  'ivi-application', 'fullscreen-shell-unstable-v1',
  'keyboard-shortcuts-inhibit-unstable-v1',
]
uwac_proto_xml = {}
foreach p : uwac_proto_names
  uwac_proto_xml += {p : files('protocols' / p + '.xml')}
endforeach

# Config-header template handles
uwac_tmpl_version = files('templates' / 'version.h.in')
uwac_tmpl_buildconfig = files('templates' / 'build-config.h.in')
uwac_tmpl_buildflags = files('templates' / 'buildflags.h.in')
uwac_tmpl_config = files('templates' / 'config.h.in')

subdir('libuwac')   # protocol codegen + uwac library
subdir('include')   # generated config headers
