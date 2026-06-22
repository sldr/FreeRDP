# libfreerdp (mirrors libfreerdp/CMakeLists.txt)
#
# Same accumulation model as WinPR: submodule meson.build files append to the
# arrays declared here (CMake freerdp_module_add / freerdp_library_add /
# freerdp_object_library_add via PARENT_SCOPE).

# Accumulators
libfreerdp_srcs = []
libfreerdp_deps = [winpr_dep]      # PUBLIC (CMake: LIBFREERDP_PUB_LIBS winpr)
libfreerdp_priv_deps = []          # PRIVATE (CMake: LIBFREERDP_LIBS)
libfreerdp_incs = [freerdp_public_inc, winpr_inc]
libfreerdp_defs = []
libfreerdp_objlibs = []            # static libs link_whole'd in (OBJECT lib equiv)

# Resource root (CMake: FREERDP_RESOURCE_ROOT) for *_FROM_FILE json resources
freerdp_resource_root = prefix / datadir / product
if get_option('with_resource_versioning')
  freerdp_resource_root += freerdp_version_major
endif

############################################################
# Screen-scaling backend (CMake libfreerdp/CMakeLists.txt: SWScale / Cairo)
############################################################
with_swscale = get_option('with_swscale')
with_cairo = get_option('with_cairo')
swscale_dep = dependency('', required : false)
if with_swscale
  swscale_dep = dependency('libswscale', required : true)
  libfreerdp_priv_deps += swscale_dep
endif
if with_cairo
  cairo_dep = dependency('cairo', required : true)
  libfreerdp_priv_deps += cairo_dep
endif
if not with_swscale and not with_cairo
  warning('Both WITH_SWSCALE and WITH_CAIRO are off: compiling without image scaling support')
endif

############################################################
# FFmpeg (CMake top-level: AVUTIL/AVCODEC; codec adds SWSCALE/SWRESAMPLE)
############################################################
avutil_dep = dependency('libavutil', required : false)
avcodec_dep = dependency('libavcodec', required : false)
swresample_dep = dependency('libswresample', required : false)
# CMake's FindFFmpeg sets SWRESAMPLE_FOUND/AVRESAMPLE_FOUND in config.h; dsp_ffmpeg.c
# #errors without one. Modern FFmpeg uses libswresample (avresample is removed).
if swresample_dep.found()
  config_h.set('SWRESAMPLE_FOUND', true)
endif
ffmpeg_found = avutil_dep.found() and avcodec_dep.found()
with_dsp_ffmpeg = get_option('with_dsp_ffmpeg') and ffmpeg_found
with_video_ffmpeg = get_option('with_video_ffmpeg') and ffmpeg_found
with_vaapi = get_option('with_vaapi') and with_video_ffmpeg

############################################################
# Optional audio codecs (CMake: find_feature in root CMakeLists.txt)
############################################################
openh264_feat = get_option('with_openh264')
openh264_dep = dependency('openh264', required : openh264_feat.enabled())
with_openh264 = openh264_dep.found() and openh264_feat.allowed()
with_openh264_loading = get_option('with_openh264_loading')

opus_feat = get_option('with_opus')
opus_dep = dependency('opus', required : opus_feat.enabled())
with_opus = opus_dep.found() and opus_feat.allowed()

soxr_feat = get_option('with_soxr')
soxr_dep = dependency('soxr', required : soxr_feat.enabled())
with_soxr = soxr_dep.found() and soxr_feat.allowed()

fdk_aac_feat = get_option('with_fdk_aac')
fdk_aac_dep = dependency('fdk-aac', required : fdk_aac_feat.enabled())
with_fdk_aac = fdk_aac_dep.found() and fdk_aac_feat.allowed()

# GSM / LAME / FAAD2 / FAAC usually have no pkg-config: probe library + header.
gsm_feat = get_option('with_gsm')
gsm_dep = cc.find_library('gsm', required : gsm_feat.enabled(), has_headers : ['gsm/gsm.h'])
with_gsm = gsm_dep.found() and gsm_feat.allowed()

lame_feat = get_option('with_lame')
lame_dep = cc.find_library('mp3lame', required : lame_feat.enabled(), has_headers : ['lame/lame.h'])
with_lame = lame_dep.found() and lame_feat.allowed()

faad2_feat = get_option('with_faad2')
faad2_dep = cc.find_library('faad', required : faad2_feat.enabled(), has_headers : ['neaacdec.h'])
with_faad2 = faad2_dep.found() and faad2_feat.allowed()

faac_feat = get_option('with_faac')
faac_dep = cc.find_library('faac', required : faac_feat.enabled(), has_headers : ['faac.h'])
with_faac = faac_dep.found() and faac_feat.allowed()

if with_opus
  libfreerdp_priv_deps += opus_dep
endif
if with_fdk_aac
  libfreerdp_priv_deps += fdk_aac_dep
  libfreerdp_defs += 'WITH_FDK_AAC'
endif

# Derived H264 graphics flag (CMake root: WITH_GFX_H264)
with_media_foundation = is_windows and get_option('with_media_foundation')
with_gfx_h264 = with_openh264 or with_media_foundation or with_video_ffmpeg

# Azure AD (CMake: WITH_AAD depends on WITH_WINPR_JSON)
aad_feat = get_option('with_aad')
with_aad = with_winpr_json and aad_feat.allowed()
if aad_feat.enabled() and not with_winpr_json
  error('with_aad=enabled requires WinPR JSON support (with_winpr_json)')
endif

############################################################
# Propagate codec feature flags into config.h (generated later in include/)
############################################################
foreach name, val : {
    'WITH_DSP_FFMPEG'      : with_dsp_ffmpeg,
    'WITH_VIDEO_FFMPEG'    : with_video_ffmpeg,
    'WITH_VAAPI'           : with_vaapi,
    'WITH_OPENH264'        : with_openh264,
    'WITH_OPENH264_LOADING': with_openh264 and with_openh264_loading,
    'WITH_OPUS'            : with_opus,
    'WITH_SOXR'            : with_soxr,
    'WITH_GSM'             : with_gsm,
    'WITH_LAME'            : with_lame,
    'WITH_FAAD2'           : with_faad2,
    'WITH_FAAC'            : with_faac,
    'WITH_GFX_H264'        : with_gfx_h264,
    'WITH_AAD'             : with_aad,
  }
  if val
    config_h.set(name, true)
  endif
endforeach

############################################################
# Submodules (CMake: FREERDP_SUBMODULES + codec + primitives)
############################################################
foreach m : ['emu', 'utils', 'common', 'gdi', 'cache', 'crypto', 'locale', 'core']
  subdir(m)
endforeach
subdir('codec')
subdir('primitives')

############################################################
# Build libfreerdp (CMake: AddTargetWithResourceFile + install)
############################################################
freerdp_libname = with_library_versioning ? 'freerdp@0@'.format(freerdp_version_major) : 'freerdp'
freerdp_lib_kwargs = {}
if with_library_versioning
  freerdp_lib_kwargs += {'version' : freerdp_version, 'soversion' : freerdp_version_major}
else
  freerdp_lib_kwargs += {'name_prefix' : ''}
endif

libfreerdp_def_args = []
foreach d : libfreerdp_defs
  libfreerdp_def_args += '-D' + d
endforeach
if get_option('with_full_config_path')
  libfreerdp_def_args += '-DWITH_FULL_CONFIG_PATH'
endif
if get_option('with_resource_versioning')
  libfreerdp_def_args += '-DWITH_RESOURCE_VERSIONING'
endif

freerdp_lib = library(
  freerdp_libname,
  libfreerdp_srcs,
  include_directories : libfreerdp_incs,
  link_whole : libfreerdp_objlibs,
  dependencies : libfreerdp_deps + libfreerdp_priv_deps,
  c_args : libfreerdp_def_args,
  gnu_symbol_visibility : default_symbol_visibility,
  install : true,
  kwargs : freerdp_lib_kwargs,
)

# Public dependency reused by channels / clients / servers.
freerdp_dep = declare_dependency(
  link_with : freerdp_lib,
  include_directories : freerdp_public_inc,
  dependencies : [winpr_dep],
)

############################################################
# pkg-config (CMake: freerdp.pc.in)
############################################################
pkgconfig = import('pkgconfig')
freerdp_pc_priv_libs = []
if with_smartcard_emulate
  freerdp_pc_priv_libs += '-lz'
endif
pkgconfig.generate(
  freerdp_lib,
  name : 'FreeRDP',
  description : 'FreeRDP: A Remote Desktop Protocol Implementation',
  url : 'http://www.freerdp.com/',
  version : freerdp_version,
  filebase : 'freerdp@0@'.format(freerdp_version_major),
  subdirs : 'freerdp@0@'.format(freerdp_version_major),
  requires : 'winpr@0@'.format(winpr_version_major),
  libraries_private : freerdp_pc_priv_libs,
)
