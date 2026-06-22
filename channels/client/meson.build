# freerdp-channels-client framework (mirrors channels/client/CMakeLists.txt)
#
# Builds the static channel dispatch table (tables.c) from the metadata
# collected in channels/meson.build, then assembles freerdp-channels-client from
# tables.c + addin.c + generic_dynvc.c and link_whole's in every client channel.

# Generate tables.c (replaces the CMake string-building + tables.c.in).
# The collected static-channel metadata is passed straight to the generator as a
# JSON string argument (no intermediate file).
channels_meta_json = '{"modules":[' + ','.join(client_modules_meta) + ']}'
channels_tables_c = custom_target(
  'channel-tables',
  output : 'tables.c',
  command : [python, gen_channel_tables_py, channels_meta_json, tmpl_channel_tables, '@OUTPUT@'],
  depend_files : [tmpl_channel_tables],
)

freerdp_channels_client = static_library(
  'freerdp-channels-client',
  channels_tables_c,
  files('addin.c', 'generic_dynvc.c'),
  include_directories : [freerdp_public_inc, winpr_inc, include_directories('.')],
  dependencies : [freerdp_dep, winpr_dep] + channels_client_link_deps,
  link_whole : channels_client_objlibs,
  gnu_symbol_visibility : default_symbol_visibility,
)

# Reused by the client frontends (Phase 5).
freerdp_channels_client_dep = declare_dependency(
  link_with : freerdp_channels_client,
  include_directories : include_directories('.'),
)
