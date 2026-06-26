# SDL3 FreeRDP client executable (mirrors client/SDL/SDL3/CMakeLists.txt).
subdir('dialogs')

# Binary name: sdl-freerdp, or sdl3-freerdp when both SDL clients are built
# (CMake: WITH_CLIENT_SDL_VERSIONED renames the target).
sdl3_bin_name = with_sdl_versioned ? 'sdl3-freerdp' : 'sdl-freerdp'

# sdl_config.hpp (CMake: configure_file of sdl_config.hpp.in).
sdl3_config = configuration_data()
sdl3_config.set('SDL_CLIENT_BINARY_NAME', sdl3_bin_name)
sdl3_config.set('FREERDP_VERSION_FULL', freerdp_version_full)
sdl3_config.set('GIT_REVISION', git_revision)
sdl3_config.set('VENDOR', vendor)
sdl3_config.set('SDL_CLIENT_UUID', 'com.freerdp.client.sdl3')
sdl3_config.set('PROJECT_URL', 'https://www.freerdp.com')
configure_file(
  input : 'sdl_config.hpp.in',
  output : 'sdl_config.hpp',
  configuration : sdl3_config,
  format : 'cmake',
)

executable(
  sdl3_bin_name,
  files(
    'sdl_utils.cpp', 'sdl_input.cpp', 'sdl_touch.cpp', 'sdl_pointer.cpp',
    'sdl_disp.cpp', 'sdl_monitor.cpp', 'sdl_freerdp.cpp', 'sdl_channels.cpp',
    'sdl_window.cpp', 'sdl_clip.cpp', 'sdl_context.cpp',
  ),
  include_directories : [
    include_directories('.'), include_directories('dialogs'),
    sdl_common_inc, sdl_common_res_inc, sdl_common_aad_inc,
  ],
  link_with : [
    sdl3_client_res_lib, sdl3_dialogs_lib, sdl_common_aad_lib, sdl_common_prefs_lib,
  ],
  dependencies : [freerdp_client_dep, freerdp_dep, winpr_dep, sdl3_dep, threads_dep],
  cpp_args : sdl_common_cpp_args,
  install : true,
  install_dir : get_option('bindir'),
)
# Man page + .desktop install (install_freerdp_desktop) deferred with WITH_MANPAGES.
