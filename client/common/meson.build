# freerdp-client shared client library (mirrors client/common/CMakeLists.txt)
#
# The channel client framework (tables.c + addin.c + generic_dynvc.c + every
# client channel) is link_whole'd in via freerdp_channels_client so the static
# dispatch table resolves all channel entry points.

freerdp_client_srcs = files(
  'client.c', 'cmdline.c', 'file.c', 'client_cliprdr_file.c',
  'geometry.c', 'smartcard_cli.c',
)

freerdp_client_deps = [freerdp_dep, winpr_dep]
freerdp_client_incs = [freerdp_public_inc, winpr_inc]
freerdp_client_c_args = []

if with_openssl
  freerdp_client_deps += openssl_dep
endif
if m_dep.found()
  freerdp_client_deps += m_dep
endif

# FUSE clipboard file copy support (CMake: WITH_FUSE; default on for Linux/BSD)
fuse_feat = get_option('with_fuse')
fuse_default = is_unix and not is_darwin and not is_android
if fuse_feat.enabled() or (fuse_feat.auto() and fuse_default)
  fuse_dep = dependency('fuse3', required : fuse_feat.enabled())
  if fuse_dep.found()
    freerdp_client_deps += fuse_dep
    freerdp_client_c_args += ['-DWITH_FUSE', '-D_FILE_OFFSET_BITS=64']
  endif
endif

# WITH_SSO_MIB (default off) — deferred.

freerdp_client_libname = with_library_versioning \
  ? 'freerdp-client@0@'.format(freerdp_version_major) : 'freerdp-client'
freerdp_client_lib_kwargs = with_library_versioning \
  ? {'version' : freerdp_version, 'soversion' : freerdp_version_major} \
  : {'name_prefix' : ''}

freerdp_client_lib = library(
  freerdp_client_libname,
  freerdp_client_srcs,
  include_directories : freerdp_client_incs,
  dependencies : freerdp_client_deps,
  link_whole : with_client_channels ? [freerdp_channels_client] : [],
  c_args : freerdp_client_c_args,
  gnu_symbol_visibility : default_symbol_visibility,
  install : true,
  kwargs : freerdp_client_lib_kwargs,
)

freerdp_client_dep = declare_dependency(
  link_with : freerdp_client_lib,
  include_directories : freerdp_public_inc,
  dependencies : [freerdp_dep, winpr_dep],
)

pkgconfig.generate(
  freerdp_client_lib,
  name : 'FreeRDP-Client',
  description : 'FreeRDP: A Remote Desktop Protocol Implementation (client)',
  url : 'http://www.freerdp.com/',
  version : freerdp_version,
  filebase : 'freerdp-client@0@'.format(freerdp_version_major),
  subdirs : 'freerdp@0@'.format(freerdp_version_major),
  requires : 'freerdp@0@'.format(freerdp_version_major),
)

# CMake find_package(FreeRDP-Client) package
cmake_packages += [{
  'name' : 'FreeRDP-Client',
  'version' : freerdp_version,
  'cmake_subdir' : 'FreeRDP-Client@0@'.format(freerdp_version_major),
  'template' : freerdp_client_config_cmake_in,
  'targets' : 'freerdp-client,@0@,@1@,freerdp|winpr'.format(
    libdir / (shared_lib_prefix + freerdp_client_libname + shared_lib_suffix), freerdp_include_dir),
  'vars' : [
    'FREERDP_VERSION=' + freerdp_version,
    'FREERDP_VERSION_MAJOR=' + freerdp_version_major,
    'FREERDP_VERSION_MINOR=' + freerdp_version_minor,
    'FREERDP_VERSION_REVISION=' + freerdp_version_revision,
    'WITH_SMARTCARD_EMULATE=' + (with_smartcard_emulate ? 'ON' : 'OFF'),
    'PACKAGE_FREERDP_INCLUDE_DIR=${PACKAGE_PREFIX_DIR}/' + freerdp_include_dir,
  ],
}]
