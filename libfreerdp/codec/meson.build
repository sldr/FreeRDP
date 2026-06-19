# libfreerdp codec module (mirrors libfreerdp/codec/CMakeLists.txt)
# Built as an object library (freerdp-codecs) -> Meson static_library link_whole'd
# into libfreerdp. SIMD sources are split into per-ISA static libraries so each
# gets the right compile flags (CMake set_simd_source_file_properties).

codec_srcs = [
  'bulk.c', 'dsp.c', 'color.c', 'audio.c', 'planar.c', 'bitmap.c',
  'interleaved.c', 'progressive.c', 'rfx_decode.c', 'rfx_dwt.c',
  'rfx_encode.c', 'rfx_quantization.c', 'rfx_rlgr.c', 'rfx.c', 'region.c',
  'nsc.c', 'nsc_encode.c', 'ncrush.c', 'xcrush.c', 'mppc.c', 'zgfx.c',
  'clear.c', 'jpeg.c', 'h264.c', 'yuv.c',
]
codec_deps = [winpr_dep]

if with_dsp_ffmpeg
  codec_srcs += 'dsp_ffmpeg.c'
  codec_deps += [avcodec_dep, avutil_dep]
  if swresample_dep.found()
    codec_deps += swresample_dep
  endif
endif
if with_soxr
  codec_deps += soxr_dep
endif
if with_gsm
  codec_deps += gsm_dep
endif
if with_lame
  codec_deps += lame_dep
endif
if with_fdk_aac
  codec_srcs += ['dsp_fdk_impl.c', 'dsp_fdk_aac.c']
endif
if with_faad2
  codec_deps += faad2_dep
endif
if with_faac
  codec_deps += faac_dep
endif
if with_openh264
  codec_srcs += 'h264_openh264.c'
  if not with_openh264_loading
    codec_deps += openh264_dep
  endif
endif
if with_video_ffmpeg
  codec_srcs += 'h264_ffmpeg.c'
  codec_deps += [avcodec_dep, avutil_dep]
endif
if is_windows and with_media_foundation
  codec_srcs += 'h264_mf.c'
endif

# SIMD groups (always compiled; flags applied only when WITH_SIMD).
codec_simd_groups = {
  'sse3' : ['sse/rfx_sse2.c', 'sse/nsc_sse2.c'],
  'neon' : ['neon/rfx_neon.c', 'neon/nsc_neon.c'],
}
codec_simd_libs = []
foreach level, group_srcs : codec_simd_groups
  args = (get_option('with_simd') and simd_flags.has_key(level)) \
    ? cc.get_supported_arguments(simd_flags[level]) : []
  codec_simd_libs += static_library(
    'freerdp-codec-' + level.replace('.', '_'),
    files(group_srcs),
    include_directories : libfreerdp_incs,
    dependencies : [winpr_dep],
    c_args : args,
    gnu_symbol_visibility : default_symbol_visibility,
  )
endforeach

freerdp_codecs = static_library(
  'freerdp-codecs',
  files(codec_srcs),
  include_directories : libfreerdp_incs,
  dependencies : codec_deps,
  link_whole : codec_simd_libs,
  gnu_symbol_visibility : default_symbol_visibility,
)
libfreerdp_objlibs += freerdp_codecs
libfreerdp_priv_deps += codec_deps
