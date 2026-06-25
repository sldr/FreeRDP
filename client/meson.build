# FreeRDP clients (mirrors client/CMakeLists.txt)

# CMake package template lives here at client/; common/ (where the descriptor is
# assembled) can't reference it with files('../'), so expose the handle now.
freerdp_client_config_cmake_in = files('FreeRDP-ClientConfig.cmake.in')

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
