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

# CMake find_package(FreeRDP-Server) package
cmake_packages += [{
  'name' : 'FreeRDP-Server',
  'version' : freerdp_version,
  'cmake_subdir' : 'FreeRDP-Server@0@'.format(freerdp_version_major),
  'template' : freerdp_server_config_cmake_in,
  'targets' : 'freerdp-server,@0@,@1@,freerdp|winpr'.format(
    libdir / (shared_lib_prefix + freerdp_server_libname + shared_lib_suffix), freerdp_include_dir),
  'vars' : [
    'FREERDP_VERSION=' + freerdp_version,
    'FREERDP_VERSION_MAJOR=' + freerdp_version_major,
    'FREERDP_VERSION_MINOR=' + freerdp_version_minor,
    'FREERDP_VERSION_REVISION=' + freerdp_version_revision,
    'PACKAGE_FREERDP_INCLUDE_DIR=${PACKAGE_PREFIX_DIR}/' + freerdp_include_dir,
  ],
}]
