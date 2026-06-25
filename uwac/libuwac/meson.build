# libuwac (mirrors uwac/libuwac/CMakeLists.txt)
# Generates Wayland protocol glue with wayland-scanner, then builds the uwac lib.

# Protocol code (.c) + client headers (.h) via wayland-scanner.
uwac_proto_targets = []
foreach p : uwac_proto_names
  xml = uwac_proto_xml[p]
  uwac_proto_targets += custom_target(
    p + '-protocol.c',
    input : xml, output : p + '-protocol.c',
    command : [wayland_scanner_prog, 'private-code', '@INPUT@', '@OUTPUT@'],
  )
  uwac_proto_targets += custom_target(
    p + '-client-protocol.h',
    input : xml, output : p + '-client-protocol.h',
    command : [wayland_scanner_prog, 'client-header', '@INPUT@', '@OUTPUT@'],
  )
endforeach

uwac_srcs = [
  'uwac-display.c', 'uwac-input.c', 'uwac-clipboard.c', 'uwac-os.c',
  'uwac-output.c', 'uwac-tools.c', 'uwac-utils.c', 'uwac-window.c',
]

uwac_deps = [wayland_client_dep, xkbcommon_dep]
if wayland_cursor_dep.found()
  uwac_deps += wayland_cursor_dep
endif
if m_dep.found()
  uwac_deps += m_dep
endif
# Region backend (CMake: pixman OR freerdp). Default = freerdp in the unified build.
if uwac_have_pixman_region
  uwac_deps += dependency('pixman-1')
else
  uwac_deps += freerdp_dep
endif
if is_freebsd
  uwac_epollshim = dependency('epoll-shim', required : false)
  if uwac_epollshim.found()
    uwac_deps += uwac_epollshim
  endif
endif

uwac_libname = with_library_versioning ? 'uwac@0@'.format(uwac_api_version) : 'uwac'
uwac_lib_kwargs = with_library_versioning \
  ? {'version' : uwac_version, 'soversion' : uwac_api_version} \
  : {'name_prefix' : ''}

uwac_lib = library(
  uwac_libname,
  files(uwac_srcs), uwac_proto_targets,
  include_directories : [uwac_inc, include_directories('.')],
  dependencies : uwac_deps,
  c_args : ['-DBUILD_IVI', '-DBUILD_FULLSCREEN_SHELL', '-DENABLE_XKBCOMMON'],
  gnu_symbol_visibility : default_symbol_visibility,
  install : true,
  kwargs : uwac_lib_kwargs,
)

uwac_dep = declare_dependency(
  link_with : uwac_lib,
  include_directories : uwac_inc,
)

pkgconfig.generate(
  uwac_lib,
  name : 'uwac',
  description : 'UWAC: Using Wayland As Client',
  url : 'http://www.freerdp.com/',
  version : uwac_version,
  filebase : 'uwac@0@'.format(uwac_api_version),
  subdirs : 'uwac@0@'.format(uwac_api_version),
)

# CMake find_package(uwac) package (template includes uwac.cmake, not uwacTargets.cmake)
cmake_packages += [{
  'name' : 'uwac',
  'version' : uwac_version,
  'cmake_subdir' : 'uwac@0@'.format(uwac_api_version),
  'template' : uwac_config_cmake_in,
  'targets_file' : 'uwac.cmake',
  'targets' : 'uwac,@0@,@1@'.format(
    libdir / (shared_lib_prefix + uwac_libname + shared_lib_suffix), uwac_include_dir),
  'vars' : [
    'UWAC_VERSION_MAJOR=' + uwac_version_major,
    'UWAC_VERSION_MINOR=' + uwac_version_minor,
    'UWAC_VERSION_REVISION=' + uwac_version_revision,
    'PACKAGE_UWAC_INCLUDE_DIR=${PACKAGE_PREFIX_DIR}/' + uwac_include_dir,
  ],
}]
