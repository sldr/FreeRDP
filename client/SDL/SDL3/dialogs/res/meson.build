# SDL3 resource manager (mirrors client/SDL/SDL3/dialogs/res/CMakeLists.txt).
sdl3_client_res_lib = static_library(
  'sdl3_client_res',
  files('sdl3_resource_manager.cpp'),
  include_directories : [sdl_common_res_inc, sdl_common_inc],
  dependencies : [sdl3_dep, winpr_dep],
  link_with : sdl_common_res_lib,
  cpp_args : sdl_common_cpp_args,
  pic : true,
)
