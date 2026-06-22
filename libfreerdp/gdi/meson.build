# libfreerdp gdi module (mirrors libfreerdp/gdi/CMakeLists.txt)
# CMake uses file(GLOB "*.[ch]"); enumerated here (Meson prefers explicit lists).
libfreerdp_incs += include_directories('.')

if get_option('with_debug_all') or debug_channels.contains('gfx')
  # WITH_GFX_FRAME_DUMP is a separate option (default off); not enabled here.
endif

libfreerdp_srcs += files(
  'bitmap.c', 'brush.c', 'clipping.c', 'dc.c', 'drawing.c', 'gdi.c',
  'gfx.c', 'graphics.c', 'line.c', 'pen.c', 'region.c', 'shape.c', 'video.c',
)
