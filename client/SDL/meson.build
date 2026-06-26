# FreeRDP SDL client (mirrors client/SDL/CMakeLists.txt) — C++ frontend.
#
# Builds the modern SDL3 client (`sdl-freerdp`) and, unless 3.x-deprecated code
# is disabled, the experimental SDL2 client. Resources (the OpenSans font, and
# optionally SVG icons) are compiled in via a hex-array generator that replaces
# the CMake file_to_hex_array() + configure_file() pipeline.

add_languages('cpp', native : false, required : true)
sdl_cxx = meson.get_compiler('cpp')

# SDL libraries (CMake: find_package(SDL3) / find_package(SDL2 2.0.20)).
sdl3_dep = dependency('sdl3', required : false)
sdl2_dep = dependency('sdl2', version : '>=2.0.20', required : false)

sdl3_feat = get_option('with_client_sdl3')
sdl2_feat = get_option('with_client_sdl2')

with_client_sdl3 = sdl3_feat.enabled() or (sdl3_feat.auto() and sdl3_dep.found())
with_client_sdl2 = not without_freerdp_3x_deprecated \
  and (sdl2_feat.enabled() or (sdl2_feat.auto() and sdl2_dep.found()))

if with_client_sdl3 and not sdl3_dep.found()
  error('with_client_sdl3=enabled but SDL3 development package not found')
endif
if with_client_sdl2 and not sdl2_dep.found()
  error('with_client_sdl2=enabled but SDL2 (>=2.0.20) development package not found')
endif

# The dialog widgets hard-require SDL_ttf (CMake: find_sdl_component(SDLx_ttf)).
# SDL_image is optional (WITH_SDL_IMAGE_DIALOGS, default OFF).
with_sdl_image_dialogs = get_option('with_sdl_image_dialogs')
with_webview = get_option('with_webview')

sdl3_ttf_dep = dependency('SDL3_ttf', required : false)
if with_client_sdl3 and not sdl3_ttf_dep.found()
  if sdl3_feat.enabled()
    error('SDL3 client requires SDL3_ttf (install the SDL3_ttf development package)')
  endif
  message('SDL3 found but SDL3_ttf missing — skipping SDL3 client (set with_client_sdl3=enabled to force)')
  with_client_sdl3 = false
endif

sdl2_ttf_dep = dependency('SDL2_ttf', required : false)
if with_client_sdl2 and not sdl2_ttf_dep.found()
  if sdl2_feat.enabled()
    error('SDL2 client requires SDL2_ttf (install the SDL2_ttf development package)')
  endif
  message('SDL2 found but SDL2_ttf missing — skipping SDL2 client')
  with_client_sdl2 = false
endif

if not (with_client_sdl2 or with_client_sdl3)
  message('No usable SDL toolkit (SDL3/SDL2 + _ttf) found — SDL client not built')
  subdir_done()
endif

# Both clients built -> version-suffix the binaries to avoid a name clash.
with_sdl_versioned = get_option('with_client_sdl_versioned') \
  or (with_client_sdl2 and with_client_sdl3)

# Shared compile defs (CMake top-level options; console default ON on Windows).
sdl_common_cpp_args = ['-DWITH_WIN_CONSOLE']
if with_sdl_image_dialogs
  sdl_common_cpp_args += '-DWITH_SDL_IMAGE_DIALOGS'
endif

# Include search paths shared by common + the per-version clients.
sdl_common_inc = include_directories('common')
sdl_common_res_inc = include_directories('common' / 'res')
sdl_common_aad_inc = include_directories('common' / 'aad')

# Resource generator (gen_sdl_resource_py defined at root) + its templates.
sdl_res_hpp_in = files('common' / 'res' / 'resource.hpp.in')
sdl_res_cpp_in = files('common' / 'res' / 'resource.cpp.in')

subdir('common')

if with_client_sdl3
  subdir('SDL3')
endif
if with_client_sdl2
  subdir('SDL2')
endif
