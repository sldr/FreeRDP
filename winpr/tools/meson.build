# winpr-tools library + CLI helpers (mirrors winpr/tools/CMakeLists.txt)

winpr_tools_deps = [winpr_dep]
if with_openssl
  winpr_tools_deps += openssl_dep
endif
if with_mbedtls
  winpr_tools_deps += mbedtls_dep
endif

winpr_tools_libname = with_library_versioning \
  ? 'winpr-tools@0@'.format(winpr_version_major) : 'winpr-tools'
winpr_tools_lib_kwargs = with_library_versioning \
  ? {'version' : winpr_version, 'soversion' : winpr_version_major} \
  : {'name_prefix' : ''}

winpr_tools_lib = library(
  winpr_tools_libname,
  files('makecert/makecert.c'),
  include_directories : winpr_inc,
  dependencies : winpr_tools_deps,
  gnu_symbol_visibility : default_symbol_visibility,
  install : true,
  kwargs : winpr_tools_lib_kwargs,
)

winpr_tools_dep = declare_dependency(
  link_with : winpr_tools_lib,
  include_directories : winpr_inc,
  dependencies : [winpr_dep],
)

pkgconfig.generate(
  winpr_tools_lib,
  name : 'WinPR-tools',
  description : 'WinPR: Windows Portable Runtime (tools)',
  url : 'http://www.freerdp.com/',
  version : winpr_version,
  filebase : 'winpr-tools@0@'.format(winpr_version_major),
  subdirs : 'winpr@0@'.format(winpr_version_major),
  requires : 'winpr@0@'.format(winpr_version_major),
)

# CMake find_package(WinPR-tools) package
cmake_packages += [{
  'name' : 'WinPR-tools',
  'version' : winpr_version,
  'cmake_subdir' : 'WinPR-tools@0@'.format(winpr_version_major),
  'template' : files('WinPR-toolsConfig.cmake.in'),
  'targets' : 'winpr-tools,@0@,@1@,winpr'.format(
    libdir / (shared_lib_prefix + winpr_tools_libname + shared_lib_suffix), winpr_include_dir),
  'vars' : [
    'FREERDP_VERSION=' + winpr_version,
    'WINPR_VERSION_MAJOR=' + winpr_version_major,
    'WINPR_VERSION_MINOR=' + winpr_version_minor,
    'WINPR_VERSION_REVISION=' + winpr_version_revision,
    'PACKAGE_WINPR_INCLUDE_DIR=${PACKAGE_PREFIX_DIR}/' + winpr_include_dir,
  ],
}]

# CLI tools (CMake: WITH_WINPR_TOOLS_CLI, default ON)
executable('winpr-makecert', files('makecert-cli/main.c'),
  include_directories : winpr_inc,
  dependencies : [winpr_tools_dep, winpr_dep],
  install : true, install_dir : bindir)

executable('winpr-hash', files('hash-cli/hash.c'),
  include_directories : winpr_inc,
  dependencies : [winpr_dep],
  install : true, install_dir : bindir)
