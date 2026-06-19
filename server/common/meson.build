# freerdp-server shared library (mirrors server/common/CMakeLists.txt)
# The channel server framework is link_whole'd in via freerdp_channels_server.

freerdp_server_libname = with_library_versioning \
  ? 'freerdp-server@0@'.format(freerdp_version_major) : 'freerdp-server'
freerdp_server_lib_kwargs = with_library_versioning \
  ? {'version' : freerdp_version, 'soversion' : freerdp_version_major} \
  : {'name_prefix' : ''}

freerdp_server_lib = library(
  freerdp_server_libname,
  files('server.c'),
  include_directories : [freerdp_public_inc, winpr_inc],
  dependencies : [freerdp_dep, winpr_dep],
  link_whole : with_server_channels ? [freerdp_channels_server] : [],
  gnu_symbol_visibility : default_symbol_visibility,
  install : true,
  kwargs : freerdp_server_lib_kwargs,
)

freerdp_server_dep = declare_dependency(
  link_with : freerdp_server_lib,
  include_directories : freerdp_public_inc,
  dependencies : [freerdp_dep, winpr_dep],
)

pkgconfig.generate(
  freerdp_server_lib,
  name : 'FreeRDP-Server',
  description : 'FreeRDP: A Remote Desktop Protocol Implementation (server)',
  url : 'http://www.freerdp.com/',
  version : freerdp_version,
  filebase : 'freerdp-server@0@'.format(freerdp_version_major),
  subdirs : 'freerdp@0@'.format(freerdp_version_major),
  requires : 'freerdp@0@'.format(freerdp_version_major),
)
