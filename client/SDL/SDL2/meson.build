# SDL2 FreeRDP client executable (mirrors client/SDL/SDL2/CMakeLists.txt).
# Deprecated/experimental; built only when 3.x-deprecated code is enabled.
subdir('dialogs')

sdl2_bin_name = with_sdl_versioned ? 'sdl2-freerdp' : 'sdl-freerdp'

sdl2_config = configuration_data()
sdl2_config.set('SDL_CLIENT_BINARY_NAME', sdl2_bin_name)
sdl2_config.set('FREERDP_VERSION_FULL', freerdp_version_full)
sdl2_config.set('GIT_REVISION', git_revision)
sdl2_config.set('VENDOR', vendor)
sdl2_config.set('SDL_CLIENT_UUID', 'com.freerdp.client.sdl2')
sdl2_config.set('PROJECT_URL', 'https://www.freerdp.com')
configure_file(
  input : 'sdl_config.hpp.in',
  output : 'sdl_config.hpp',
  configuration : sdl2_config,
  format : 'cmake',
)

executable(
  sdl2_bin_name,
  files(
    'sdl_utils.cpp', 'sdl_kbd.cpp', 'sdl_touch.cpp', 'sdl_pointer.cpp',
    'sdl_disp.cpp', 'sdl_monitor.cpp', 'sdl_freerdp.cpp', 'sdl_channels.cpp',
    'sdl_window.cpp',
  ),
  include_directories : [
    include_directories('.'), include_directories('dialogs'),
    sdl_common_inc, sdl_common_res_inc, sdl_common_aad_inc,
  ],
  link_with : [
    sdl2_client_res_lib, sdl2_dialogs_lib, sdl_common_aad_lib, sdl_common_prefs_lib,
  ],
  dependencies : [freerdp_client_dep, freerdp_dep, winpr_dep, sdl2_dep, threads_dep],
  cpp_args : sdl_common_cpp_args,
  install : true,
  install_dir : get_option('bindir'),
)
