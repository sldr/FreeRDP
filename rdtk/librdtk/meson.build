# librdtk (mirrors rdtk/librdtk/CMakeLists.txt)
rdtk_libname = with_library_versioning ? 'rdtk@0@'.format(rdtk_version_major) : 'rdtk'
rdtk_lib_kwargs = with_library_versioning \
  ? {'version' : rdtk_version, 'soversion' : rdtk_version_major} \
  : {'name_prefix' : ''}

rdtk_lib = library(
  rdtk_libname,
  files(
    'rdtk_resources.c', 'rdtk_surface.c', 'rdtk_font.c', 'rdtk_button.c',
    'rdtk_label.c', 'rdtk_nine_patch.c', 'rdtk_text_field.c', 'rdtk_engine.c',
  ),
  include_directories : rdtk_inc,
  dependencies : [winpr_dep],
  c_args : ['-DRDTK_EXPORTS'],
  gnu_symbol_visibility : default_symbol_visibility,
  install : true,
  kwargs : rdtk_lib_kwargs,
)

rdtk_dep = declare_dependency(
  link_with : rdtk_lib,
  include_directories : rdtk_inc,
  dependencies : [winpr_dep],
)

pkgconfig.generate(
  rdtk_lib,
  name : 'RdTk',
  description : 'RdTk: Remote Desktop Toolkit',
  url : 'http://www.freerdp.com/',
  version : rdtk_version,
  filebase : 'rdtk@0@'.format(rdtk_version_major),
  subdirs : 'rdtk@0@'.format(rdtk_version_major),
)
