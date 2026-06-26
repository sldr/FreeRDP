# SDL AAD login view (mirrors client/SDL/common/aad/CMakeLists.txt).
# WITH_WEBVIEW pulls in an external webview library via CMake FetchContent, which
# has no Meson equivalent here; without it the view is a dummy stub (CMake default).
if with_webview
  error('with_webview is not supported by the Meson build (CMake FetchContent webview); ' +
        'build without it for the dummy AAD view')
endif

sdl_common_aad_lib = static_library(
  'sdl-common-aad-view',
  files('dummy.cpp'),
  include_directories : sdl_common_inc,
  dependencies : [winpr_dep],
  pic : true,
)
