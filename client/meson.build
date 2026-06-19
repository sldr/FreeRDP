# FreeRDP clients (mirrors client/CMakeLists.txt)

if get_option('with_client_common')
  subdir('common')
endif

# Platform client frontends
if get_option('with_client') and is_windows
  subdir('Windows')
endif
# Further frontends (Phase 5b cont.):
#   SDL2/SDL3 (WITH_CLIENT_SDL), X11 (WITH_X11), Wayland (WITH_WAYLAND),
#   Mac (APPLE && !IOS)

if get_option('with_client') and get_option('with_sample')
  subdir('Sample')
endif
