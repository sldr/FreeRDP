# Generated RdTk config headers (mirrors rdtk/templates/CMakeLists.txt configure calls)
rdtk_gen_install_dir = rdtk_include_dir / 'rdtk'
configure_file(input : rdtk_tmpl_version, output : 'version.h',
  configuration : rdtk_version_data, format : 'cmake',
  install : true, install_dir : rdtk_gen_install_dir)
configure_file(input : rdtk_tmpl_buildconfig, output : 'build-config.h',
  configuration : rdtk_buildconfig_data, format : 'cmake',
  install : true, install_dir : rdtk_gen_install_dir)
configure_file(input : rdtk_tmpl_buildflags, output : 'buildflags.h',
  configuration : rdtk_buildflags_data, format : 'cmake',
  install : true, install_dir : rdtk_gen_install_dir)
# rdtk config.h.in has no substitutions (just include guards) -> copy verbatim.
configure_file(input : rdtk_tmpl_config, output : 'config.h', copy : true,
  install : true, install_dir : rdtk_gen_install_dir)
