# SDL2 resource manager (mirrors client/SDL/SDL2/dialogs/res/CMakeLists.txt).
sdl2_client_res_lib = static_library(
  'sdl2_client_res',
  files('sdl2_resource_manager.cpp'),
  include_directories : [sdl_common_res_inc, sdl_common_inc],
  dependencies : [sdl2_dep, winpr_dep],
  link_with : sdl_common_res_lib,
  cpp_args : sdl_common_cpp_args,
  pic : true,
)
