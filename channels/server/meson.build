# freerdp-channels-server framework (mirrors channels/server/CMakeLists.txt)
#
# Assembles freerdp-channels-server from channels.c and link_whole's in every
# server channel collected in channels/meson.build.

freerdp_channels_server = static_library(
  'freerdp-channels-server',
  files('channels.c'),
  include_directories : [freerdp_public_inc, winpr_inc, include_directories('.')],
  dependencies : [freerdp_dep, winpr_dep],
  link_whole : channels_server_objlibs,
  gnu_symbol_visibility : default_symbol_visibility,
)

# Reused by the server binaries (Phase 5).
freerdp_channels_server_dep = declare_dependency(
  link_with : freerdp_channels_server,
  include_directories : include_directories('.'),
)
