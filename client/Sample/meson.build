# Sample client binary "sfreerdp" (mirrors client/Sample/CMakeLists.txt)
sfreerdp = executable(
  'sfreerdp',
  files('tf_channels.c', 'tf_freerdp.c'),
  include_directories : [freerdp_public_inc, winpr_inc],
  dependencies : [freerdp_client_dep, freerdp_dep, winpr_dep],
  install : true,
  install_dir : get_option('bindir'),
)
