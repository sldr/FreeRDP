# Windows native client executable "wfreerdp" (mirrors client/Windows/cli/CMakeLists.txt)
# WITH_WIN_CONSOLE defaults OFF -> GUI subsystem.

wfreerdp = executable(
  'wfreerdp',
  files('wfreerdp.c'), wf_rc,
  include_directories : [freerdp_public_inc, winpr_inc, include_directories('..')],
  link_with : wfreerdp_client_lib,
  dependencies : [freerdp_client_dep, freerdp_dep, winpr_dep],
  win_subsystem : 'windows',
  install : true,
  install_dir : get_option('bindir'),
)
