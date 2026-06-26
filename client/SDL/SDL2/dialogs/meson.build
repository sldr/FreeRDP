# SDL2 dialog widgets (mirrors client/SDL/SDL2/dialogs/CMakeLists.txt).
subdir('res')

sdl2_dialogs_deps = [sdl2_dep, sdl2_ttf_dep, freerdp_dep, winpr_dep]
if with_sdl_image_dialogs
  sdl2_dialogs_deps += dependency('SDL2_image')
endif

sdl2_dialogs_lib = static_library(
  'sdl2-dialogs',
  files(
    'sdl_button.cpp', 'sdl_buttons.cpp', 'sdl_dialogs.cpp', 'sdl_widget.cpp',
    'sdl_input.cpp', 'sdl_input_widgets.cpp', 'sdl_select.cpp',
    'sdl_selectlist.cpp', 'sdl_connection_dialog.cpp',
  ),
  include_directories : [include_directories('.'), sdl_common_inc, sdl_common_res_inc],
  dependencies : sdl2_dialogs_deps,
  link_with : sdl2_client_res_lib,
  cpp_args : sdl_common_cpp_args,
  pic : true,
)
