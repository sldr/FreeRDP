# Wayland client "wlfreerdp" (mirrors client/Wayland/CMakeLists.txt)
wlfreerdp = executable(
  'wlfreerdp',
  files(
    'wlfreerdp.c', 'wlf_disp.c', 'wlf_pointer.c', 'wlf_input.c',
    'wlf_cliprdr.c', 'wlf_channels.c',
  ),
  include_directories : [freerdp_public_inc, winpr_inc, uwac_inc],
  dependencies : [freerdp_client_dep, freerdp_dep, winpr_dep, uwac_dep, wayland_client_dep],
  install : true,
  install_dir : get_option('bindir'),
)
# Man page (generate_and_install_freerdp_man_from_template) deferred with WITH_MANPAGES.
