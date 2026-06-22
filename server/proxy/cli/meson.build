# freerdp-proxy application (mirrors server/proxy/cli/CMakeLists.txt)
freerdp_proxy_app = executable(
  'freerdp-proxy',
  files('freerdp_proxy.c'),
  include_directories : [freerdp_public_inc, winpr_inc, include_directories('..')],
  dependencies : [freerdp_proxy_dep, freerdp_dep, winpr_dep],
  install : true,
  install_dir : get_option('bindir'),
)
# Man page (generate_and_install_freerdp_man_from_template) deferred with WITH_MANPAGES.
