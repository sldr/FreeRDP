# SDL client shared code (mirrors client/SDL/common/CMakeLists.txt).

subdir('aad')   # sdl-common-aad-view (dummy unless WITH_WEBVIEW)
subdir('res')   # sdl-common-client-res (compiled-in fonts/images)

sdl_common_prefs_srcs = files('sdl_prefs.cpp', 'sdl_common_utils.cpp')
if is_windows
  sdl_common_prefs_srcs += files('sdl_win32_console.cpp')
endif

sdl_common_prefs_lib = static_library(
  'sdl-common-prefs',
  sdl_common_prefs_srcs,
  include_directories : sdl_common_inc,
  dependencies : [freerdp_dep, winpr_dep],
  cpp_args : sdl_common_cpp_args,
  pic : true,
)
