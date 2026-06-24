# FreeRDP clients (mirrors client/CMakeLists.txt)

if get_option('with_client_common')
  subdir('common')
endif

# Platform client frontends
if get_option('with_client') and is_windows
  subdir('Windows')
endif
if get_option('with_client') and with_x11
  subdir('X11')
endif
if get_option('with_client') and with_uwac
  subdir('Wayland')
endif
# Further frontends:
#   SDL2/SDL3 (WITH_CLIENT_SDL), Mac (APPLE && !IOS)

if get_option('with_client') and get_option('with_sample')
  subdir('Sample')
endif
