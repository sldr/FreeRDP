# freerdp-shadow-cli (mirrors server/shadow/cli/CMakeLists.txt)
freerdp_shadow_cli = executable(
  'freerdp-shadow-cli',
  files('shadow.c'),
  include_directories : shadow_inc,
  dependencies : [freerdp_shadow_subsystem_dep, freerdp_shadow_dep, freerdp_dep, winpr_dep],
  install : true,
  install_dir : get_option('bindir'),
)
# Man page (generate_and_install_freerdp_man_from_template) deferred with WITH_MANPAGES.
