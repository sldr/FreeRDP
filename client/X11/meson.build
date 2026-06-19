# X11 native client "xfreerdp-client" (mirrors client/X11/CMakeLists.txt)

x11_dep = dependency('x11', required : true)

xf_srcs = files(
  'xf_utils.c', 'xf_gfx.c', 'xf_rail.c', 'xf_input.c', 'xf_event.c',
  'xf_floatbar.c', 'xf_channels.c', 'xf_cliprdr.c', 'xf_monitor.c',
  'xf_disp.c', 'xf_graphics.c', 'xf_keyboard.c', 'keyboard_x11.c',
  'xkb_layout_ids.c', 'xf_video.c', 'xf_window.c', 'xf_client.c',
)

xf_deps = [freerdp_client_dep, freerdp_dep, winpr_dep, x11_dep]
xf_c_args = []
xf_incs = [
  freerdp_public_inc, winpr_inc,
  include_directories('.'),
  include_directories('..' / '..' / 'resources'),
]

# Optional X11 extensions (CMake: WITH_XSHM/XINERAMA/XEXT/XCURSOR/XV/XI/XRENDER/
# XRANDR/XFIXES). Each defaults ON and adds a WITH_* define when found.
x11_extensions = [
  ['xext', 'WITH_XEXT'],
  ['xinerama', 'WITH_XINERAMA'],
  ['xcursor', 'WITH_XCURSOR'],
  ['xv', 'WITH_XV'],
  ['xi', 'WITH_XI'],
  ['xrender', 'WITH_XRENDER'],
  ['xrandr', 'WITH_XRANDR'],
  ['xfixes', 'WITH_XFIXES'],
]
foreach ext : x11_extensions
  dep = dependency(ext[0], required : false)
  if dep.found()
    xf_deps += dep
    xf_c_args += '-D' + ext[1]
  endif
endforeach

# XShm lives in libXext; gate the define on its header.
if cc.has_header('X11/extensions/XShm.h')
  xf_c_args += '-DWITH_XSHM'
endif

xfreerdp_client_lib = static_library(
  'xfreerdp-client',
  xf_srcs,
  include_directories : xf_incs,
  dependencies : xf_deps,
  c_args : xf_c_args,
  gnu_symbol_visibility : default_symbol_visibility,
)

subdir('cli')
