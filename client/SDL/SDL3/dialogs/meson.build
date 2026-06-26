# SDL3 dialog widgets (mirrors client/SDL/SDL3/dialogs/CMakeLists.txt).
# Hard-requires SDL3_ttf (text rendering); SDL3_image is optional.
subdir('res')

sdl3_dialogs_deps = [sdl3_dep, sdl3_ttf_dep, freerdp_dep, winpr_dep]
if with_sdl_image_dialogs
  sdl3_dialogs_deps += dependency('SDL3_image')
endif

sdl3_dialogs_lib = static_library(
  'sdl3-dialogs',
  files(
    'sdl_button.cpp', 'sdl_buttons.cpp', 'sdl_dialogs.cpp', 'sdl_widget.cpp',
    'sdl_widget_list.cpp', 'sdl_input_widget.cpp', 'sdl_input_widget_pair.cpp',
    'sdl_input_widget_pair_list.cpp', 'sdl_select.cpp', 'sdl_select_list.cpp',
    'sdl_selectable_widget.cpp', 'sdl_connection_dialog.cpp',
    'sdl_connection_dialog_wrapper.cpp', 'sdl_blend_mode_guard.cpp',
    'sdl_connection_dialog_hider.cpp',
  ),
  include_directories : [include_directories('.'), sdl_common_inc, sdl_common_res_inc],
  dependencies : sdl3_dialogs_deps,
  link_with : sdl3_client_res_lib,
  cpp_args : sdl_common_cpp_args,
  pic : true,
)
