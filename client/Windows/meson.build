# Windows native client control library "wfreerdp-client"
# (mirrors client/Windows/CMakeLists.txt)

wf_srcs = files(
  'wf_gdi.c', 'wf_event.c', 'wf_channels.c', 'wf_graphics.c', 'wf_cliprdr.c',
  'wf_rail.c', 'wf_client.c', 'wf_floatbar.c', 'wf_defaults.c',
)

# App resource (icon/version). Compiled via the windows module (rc.exe/windres)
# and shared by the control lib and the cli exe.
windows_mod = import('windows')
wf_rc = windows_mod.compile_resources(
  'resource/wfreerdp.rc',
  include_directories : include_directories('resource'),
)

# Defaults: WITH_WINDOWS_CERT_STORE=ON, WITH_PROGRESS_BAR=ON (CMake defaults).
wf_c_args = ['-DWITH_WINDOWS_CERT_STORE', '-DWITH_PROGRESS_BAR']

wfreerdp_client_lib = static_library(
  'wfreerdp-client',
  wf_srcs, wf_rc,
  include_directories : [freerdp_public_inc, winpr_inc, include_directories('.', 'resource')],
  dependencies : [
    freerdp_client_dep, freerdp_dep, winpr_dep,
    cc.find_library('msimg32'), cc.find_library('credui'),
  ],
  c_args : wf_c_args,
  gnu_symbol_visibility : default_symbol_visibility,
)

subdir('cli')
