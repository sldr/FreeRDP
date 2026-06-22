# Dummy shadow capture subsystem (mirrors server/shadow/Sample/CMakeLists.txt),
# used when WITH_SHADOW_SUBSYSTEM is off.
freerdp_shadow_subsystem_impl = static_library(
  'freerdp-shadow-subsystem-impl',
  files('sample_shadow.c'),
  include_directories : [freerdp_public_inc, winpr_inc],
  dependencies : [freerdp_dep, winpr_dep],
  gnu_symbol_visibility : default_symbol_visibility,
)
