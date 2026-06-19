# X11 client executable "xfreerdp" (mirrors client/X11/cli/CMakeLists.txt)
xfreerdp = executable(
  'xfreerdp',
  files('xfreerdp.c'),
  include_directories : [freerdp_public_inc, winpr_inc, include_directories('..')],
  link_with : xfreerdp_client_lib,
  dependencies : [freerdp_client_dep, freerdp_dep, winpr_dep],
  install : true,
  install_dir : get_option('bindir'),
)
