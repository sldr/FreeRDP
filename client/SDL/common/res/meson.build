# SDL compiled-in resources (mirrors client/SDL/common/res/CMakeLists.txt).
# The font (and, with SDL_image dialogs, the SVG icons) are hex-encoded into
# generated C++ via meson/gen_sdl_resource.py, replacing CMake's
# file_to_hex_array() + resource.{hpp,cpp}.in + the resource-init.cpp writer.

# Resources hex-encoded into the build (CMake: SDL_USE_COMPILED_RESOURCES, ON).
# The font is always compiled in; SVG icons only with SDL_image dialogs. Input
# order must match the types CSV (the generator pairs them positionally).
sdl_res_inputs = [sdl_font_file]
sdl_res_types = ['fonts']
sdl_res_outputs = ['OpenSans_VariableFont_wdth_wght_ttf.hpp',
                   'OpenSans_VariableFont_wdth_wght_ttf.cpp']

if with_sdl_image_dialogs
  sdl_res_inputs += sdl_svg_files
  foreach svg : ['FreeRDP_Icon.svg', 'icon_info.svg', 'icon_warning.svg', 'icon_error.svg']
    sdl_res_types += 'images'
    cls = svg.replace('.', '_')
    sdl_res_outputs += [cls + '.hpp', cls + '.cpp']
  endforeach
endif
sdl_res_outputs += 'resource-init.cpp'

sdl_res_gen = custom_target(
  'sdl-common-resources',
  input : sdl_res_inputs,
  output : sdl_res_outputs,
  command : [
    python, gen_sdl_resource_py, 'all', '@OUTDIR@', 'sdl-freerdp',
    sdl_res_hpp_in, sdl_res_cpp_in, ','.join(sdl_res_types), '@INPUT@',
  ],
  depend_files : [sdl_res_hpp_in, sdl_res_cpp_in],
)

sdl_common_res_lib = static_library(
  'sdl-common-client-res',
  [files('sdl_resource_manager.cpp', 'sdl_resource_file.cpp'), sdl_res_gen],
  include_directories : [sdl_common_res_inc, sdl_common_inc],
  dependencies : [winpr_dep],
  cpp_args : sdl_common_cpp_args + ['-DSDL_USE_COMPILED_RESOURCES'],
  pic : true,
)
