# Windows shadow capture subsystem (mirrors server/shadow/Win/CMakeLists.txt)
freerdp_shadow_subsystem_impl = static_library(
  'freerdp-shadow-subsystem-impl',
  files('win_dxgi.c', 'win_rdp.c', 'win_shadow.c', 'win_wds.c'),
  include_directories : [freerdp_public_inc, winpr_inc],
  dependencies : [freerdp_client_dep, freerdp_dep, winpr_dep],
  c_args : ['-DWITH_SHADOW_WIN'],
  gnu_symbol_visibility : default_symbol_visibility,
)
