# libfreerdp primitives module (mirrors libfreerdp/primitives/CMakeLists.txt)
# Object library (freerdp-primitives) with SIMD sources split per ISA.

primitives_base_srcs = [
  'prim_add.c', 'prim_andor.c', 'prim_alphaComp.c', 'prim_colors.c',
  'prim_copy.c', 'prim_set.c', 'prim_shift.c', 'prim_sign.c', 'prim_YUV.c',
  'prim_YCoCg.c', 'primitives.c',
  # OpenCL primitive (always compiled; #if-guarded on WITH_OPENCL)
  'opencl/prim_YUV_opencl.c',
]
primitives_deps = [winpr_dep]

# OpenCL program header generation (CMake: file_to_hex_array, default WITH_OPENCL=OFF)
# Deferred: requires the ConvertFileToHexArray equivalent; OpenCL is experimental.
if get_option('with_opencl').enabled()
  error('OpenCL primitives support is not yet ported to the Meson build')
endif

# SIMD groups (CMake: set_simd_source_file_properties per level).
primitives_simd_groups = {
  'sse3' : [
    'sse/prim_colors_sse2.c', 'sse/prim_set_sse2.c', 'sse/prim_add_sse3.c',
    'sse/prim_alphaComp_sse3.c', 'sse/prim_andor_sse3.c', 'sse/prim_shift_sse3.c',
  ],
  'ssse3' : ['sse/prim_sign_ssse3.c', 'sse/prim_YCoCg_ssse3.c'],
  'sse4.1' : ['sse/prim_copy_sse4_1.c', 'sse/prim_YUV_sse4.1.c'],
  'neon' : ['neon/prim_colors_neon.c', 'neon/prim_YCoCg_neon.c', 'neon/prim_YUV_neon.c'],
}
if get_option('with_avx2')
  primitives_simd_groups += {'avx2' : ['sse/prim_copy_avx2.c']}
endif

primitives_simd_libs = []
foreach level, group_srcs : primitives_simd_groups
  args = (get_option('with_simd') and simd_flags.has_key(level)) \
    ? cc.get_supported_arguments(simd_flags[level]) : []
  primitives_simd_libs += static_library(
    'freerdp-primitives-' + level.replace('.', '_'),
    files(group_srcs),
    include_directories : libfreerdp_incs,
    dependencies : [winpr_dep],
    c_args : args,
    gnu_symbol_visibility : default_symbol_visibility,
  )
endforeach

freerdp_primitives = static_library(
  'freerdp-primitives',
  files(primitives_base_srcs),
  include_directories : libfreerdp_incs,
  dependencies : primitives_deps,
  link_whole : primitives_simd_libs,
  gnu_symbol_visibility : default_symbol_visibility,
)
libfreerdp_objlibs += freerdp_primitives
