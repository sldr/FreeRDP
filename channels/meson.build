# FreeRDP virtual channels (mirrors channels/CMakeLists.txt)
#
# CMake discovers channels via file(GLOB */ChannelOptions.cmake) and a set of
# macros (define_channel / add_channel_client_library / ...). Meson prefers an
# explicit registry: each channel lists its client/server sources + the static
# entry-point symbol. Client channels are built as static_library OBJECT-library
# equivalents and link_whole'd into freerdp-channels-client, whose static
# dispatch table (tables.c) is generated from the collected metadata.
#
# NOTE: drdynvc MUST be first (dynamic channels depend on its options in CMake).
# NOTE: This registry currently covers a representative subset proving the full
#       pattern (all four entry-point kinds, client + server, shared ../common.c
#       sources). Remaining channels (ainput, audin, disp*, geometry, location,
#       parallel, printer, rail*, rdpecam, rdpei, rdpgfx, rdpsnd, remdesk,
#       serial, smartcard, sshagent, telemetry, tsmf, urbdrc, video, drive,
#       encomsp, gfxredir, rdp2tcp, rdpear, rdpemsc) are mechanical additions to
#       this list; subsystem channels (audin/rdpsnd/printer/rdpecam/tsmf) need
#       per-backend sub-libraries like the WinPR subsystem pattern.

with_client_channels = get_option('with_client_channels')
with_server_channels = get_option('with_server_channels')

# Channel registry. srcs are relative to this directory (channels/).
# drdynvc first (dynamic channels depend on it). Subsystem CLIENT channels
# (audin/rdpsnd/printer/rdpecam/tsmf/urbdrc) are deferred — they need per-backend
# sub-libraries (alsa/pulse/oss/sndio/winmm/mac/cups/v4l/libusb). Their simple
# SERVER sides are included here.
channel_registry = [
  {
    'name' : 'drdynvc', 'type' : 'static',
    'client' : {'srcs' : ['drdynvc/client/drdynvc_main.c'], 'entry' : 'VirtualChannelEntryEx'},
    'server' : {'srcs' : ['drdynvc/server/drdynvc_main.c'], 'entry' : 'VirtualChannelEntry'},
  },
  {
    'name' : 'ainput', 'type' : 'dynamic',
    'client' : {'srcs' : ['ainput/client/ainput_main.c'], 'entry' : 'DVCPluginEntry'},
    'server' : {'srcs' : ['ainput/server/ainput_main.c'], 'entry' : 'DVCPluginEntry'},
  },
  {
    'name' : 'audin', 'type' : 'dynamic',
    'client' : {'srcs' : ['audin/client/audin_main.c'], 'entries' : ['DVCPluginEntry'], 'audio' : true},
    'server' : {'srcs' : ['audin/server/audin.c'], 'entry' : 'DVCPluginEntry'},
  },
  {
    'name' : 'cliprdr', 'type' : 'static',
    'client' : {
      'srcs' : ['cliprdr/client/cliprdr_format.c', 'cliprdr/client/cliprdr_main.c',
                'cliprdr/cliprdr_common.c'],
      'entry' : 'VirtualChannelEntryEx',
    },
    'server' : {
      'srcs' : ['cliprdr/server/cliprdr_main.c', 'cliprdr/cliprdr_common.c'],
      'entry' : 'VirtualChannelEntry',
    },
  },
  {
    'name' : 'disp', 'type' : 'dynamic',
    'client' : {'srcs' : ['disp/client/disp_main.c', 'disp/disp_common.c'], 'entry' : 'DVCPluginEntry'},
    'server' : {'srcs' : ['disp/server/disp_main.c', 'disp/disp_common.c'], 'entry' : 'DVCPluginEntry'},
  },
  {
    'name' : 'drive', 'type' : 'static',
    'client' : {'srcs' : ['drive/client/drive_file.c', 'drive/client/drive_main.c'], 'entry' : 'DeviceServiceEntry'},
  },
  {
    'name' : 'echo', 'type' : 'dynamic',
    'client' : {'srcs' : ['echo/client/echo_main.c'], 'entry' : 'DVCPluginEntry'},
    'server' : {'srcs' : ['echo/server/echo_main.c'], 'entry' : 'DVCPluginEntry'},
  },
  {
    'name' : 'encomsp', 'type' : 'static',
    'client' : {'srcs' : ['encomsp/client/encomsp_main.c'], 'entry' : 'VirtualChannelEntryEx'},
    'server' : {'srcs' : ['encomsp/server/encomsp_main.c'], 'entry' : 'VirtualChannelEntry'},
  },
  {
    'name' : 'geometry', 'type' : 'dynamic',
    'client' : {'srcs' : ['geometry/client/geometry_main.c'], 'entry' : 'DVCPluginEntry'},
  },
  {
    'name' : 'gfxredir', 'type' : 'dynamic',
    'common' : ['gfxredir/common/gfxredir_common.c'],
    'server' : {'srcs' : ['gfxredir/server/gfxredir_main.c'], 'entry' : 'DVCPluginEntry'},
  },
  {
    'name' : 'location', 'type' : 'dynamic',
    'client' : {'srcs' : ['location/client/location_main.c'], 'entry' : 'DVCPluginEntry'},
    'server' : {'srcs' : ['location/server/location_main.c'], 'entry' : 'DVCPluginEntry'},
  },
  {
    'name' : 'parallel', 'type' : 'static',
    'client' : {'srcs' : ['parallel/client/parallel_main.c'], 'entry' : 'DeviceServiceEntry'},
  },
  {
    'name' : 'rail', 'type' : 'static',
    'client' : {
      'srcs' : ['rail/rail_common.c', 'rail/client/client_rails.c', 'rail/client/rail_main.c',
                'rail/client/rail_orders.c'],
      'entry' : 'VirtualChannelEntryEx',
    },
    'server' : {'srcs' : ['rail/rail_common.c', 'rail/server/rail_main.c'], 'entry' : 'VirtualChannelEntryEx'},
  },
  {
    'name' : 'rdp2tcp', 'type' : 'static',
    'client' : {'srcs' : ['rdp2tcp/client/rdp2tcp_main.c'], 'entry' : 'VirtualChannelEntryEx'},
  },
  {
    'name' : 'rdpdr', 'type' : 'static',
    'client' : {
      'srcs' : ['rdpdr/client/irp.c', 'rdpdr/client/devman.c', 'rdpdr/client/rdpdr_main.c',
                'rdpdr/client/rdpdr_capabilities.c'],
      'entry' : 'VirtualChannelEntryEx',
    },
    'server' : {'srcs' : ['rdpdr/server/rdpdr_main.c'], 'entry' : 'VirtualChannelEntry'},
  },
  {
    'name' : 'rdpei', 'type' : 'dynamic',
    'client' : {'srcs' : ['rdpei/client/rdpei_main.c', 'rdpei/rdpei_common.c'], 'entry' : 'DVCPluginEntry'},
    'server' : {'srcs' : ['rdpei/server/rdpei_main.c', 'rdpei/rdpei_common.c'], 'entry' : 'VirtualChannelEntry'},
  },
  {
    'name' : 'rdpemsc', 'type' : 'dynamic',
    'server' : {'srcs' : ['rdpemsc/server/mouse_cursor_main.c'], 'entry' : 'DVCPluginEntry'},
  },
  {
    'name' : 'rdpgfx', 'type' : 'dynamic',
    'client' : {
      'srcs' : ['rdpgfx/client/rdpgfx_main.c', 'rdpgfx/client/rdpgfx_codec.c', 'rdpgfx/rdpgfx_common.c'],
      'entry' : 'DVCPluginEntry',
    },
    'server' : {'srcs' : ['rdpgfx/server/rdpgfx_main.c', 'rdpgfx/rdpgfx_common.c'], 'entry' : 'DVCPluginEntry'},
  },
  {
    'name' : 'rdpsnd', 'type' : 'static',
    'common' : ['rdpsnd/common/rdpsnd_common.c'],
    'client' : {
      'srcs' : ['rdpsnd/client/rdpsnd_main.c'],
      'entries' : ['VirtualChannelEntryEx', 'DVCPluginEntry'], 'audio' : true,
    },
    'server' : {'srcs' : ['rdpsnd/server/rdpsnd_main.c'], 'entry' : 'VirtualChannelEntry'},
  },
  {
    'name' : 'remdesk', 'type' : 'static',
    'common' : ['remdesk/common/remdesk_common.c'],
    'client' : {'srcs' : ['remdesk/client/remdesk_main.c'], 'entry' : 'VirtualChannelEntryEx'},
    'server' : {'srcs' : ['remdesk/server/remdesk_main.c'], 'entry' : 'VirtualChannelEntry'},
  },
  {
    'name' : 'serial', 'type' : 'static',
    'client' : {'srcs' : ['serial/client/serial_main.c'], 'entry' : 'DeviceServiceEntry'},
  },
  {
    'name' : 'smartcard', 'type' : 'static',
    'client' : {'srcs' : ['smartcard/client/smartcard_main.c'], 'entry' : 'DeviceServiceEntry'},
  },
  {
    'name' : 'sshagent', 'type' : 'dynamic',
    'client' : {'srcs' : ['sshagent/client/sshagent_main.c'], 'entry' : 'DVCPluginEntry'},
  },
  {
    'name' : 'telemetry', 'type' : 'dynamic',
    'server' : {'srcs' : ['telemetry/server/telemetry_main.c'], 'entry' : 'DVCPluginEntry'},
  },
  {
    'name' : 'video', 'type' : 'dynamic',
    'client' : {'srcs' : ['video/client/video_main.c'], 'entry' : 'DVCPluginEntry'},
  },
]

# Device-redirection subsystem clients (printer/urbdrc). Backend deps are resolved
# here; a subsystem is only built when its dependency is present.
# (rdpecam and tsmf are deferred: they hard-require FFmpeg+SWScale+V4L / are deprecated.)
cups_dep = dependency('cups', version : '>=2.0', required : false)
# CUPS historically ships cups-config (not pkg-config), so dependency('cups') can
# report found via the runtime lib while the dev header is absent. Require the header.
have_cups = cups_dep.found() and cc.has_header('cups/cups.h', dependencies : cups_dep)
libusb_dep = dependency('libusb-1.0', required : false)

printer_subsystems = []
if have_cups
  printer_subsystems += {'name' : 'cups', 'srcs' : ['printer/client/cups/printer_cups.c'], 'deps' : [cups_dep]}
endif
if is_windows
  printer_subsystems += {'name' : 'win', 'srcs' : ['printer/client/win/printer_win.c'], 'deps' : []}
endif
channel_registry += [{
  'name' : 'printer', 'type' : 'static',
  'client' : {
    'srcs' : ['printer/client/printer_main.c'],
    'entry' : 'DeviceServiceEntry',
    'subsystems' : printer_subsystems,
  },
}]

# urbdrc requires libusb (CMake: find_package(libusb-1.0 REQUIRED) at channel level).
urbdrc_entry = {
  'name' : 'urbdrc', 'type' : 'dynamic',
  'common' : ['urbdrc/common/msusb.c', 'urbdrc/common/urbdrc_helpers.c'],
}
if libusb_dep.found()
  urbdrc_entry += {
    'client' : {
      'srcs' : ['urbdrc/client/data_transfer.c', 'urbdrc/client/urbdrc_main.c'],
      'entry' : 'DVCPluginEntry',
      'subsystems' : [{
        'name' : 'libusb',
        'srcs' : ['urbdrc/client/libusb/libusb_udevman.c', 'urbdrc/client/libusb/libusb_udevice.c'],
        'deps' : [libusb_dep, threads_dep],
      }],
    },
  }
endif
channel_registry += [urbdrc_entry]

# rdpewa: WebAuthn redirection (since 3.x). Client needs libcbor + libfido2.
rdpewa_entry = {'name' : 'rdpewa', 'type' : 'dynamic'}
libcbor_dep = dependency('libcbor', required : false)
libfido2_dep = dependency('libfido2', required : false)
if libcbor_dep.found() and libfido2_dep.found()
  rdpewa_entry += {
    'client' : {
      'srcs' : ['rdpewa/client/rdpewa_main.c', 'rdpewa/client/rdpewa_cbor.c',
                'rdpewa/client/rdpewa_fido.c'],
      'entry' : 'DVCPluginEntry',
      'deps' : [libcbor_dep, libfido2_dep],
    },
  }
endif
channel_registry += [rdpewa_entry]

# rdpear: Kerberos extended auth (non-Windows/Apple/Android, MIT krb5 only).
rdpear_entry = {
  'name' : 'rdpear', 'type' : 'dynamic',
  'common' : ['rdpear/common/ndr.c', 'rdpear/common/rdpear_asn1.c', 'rdpear/common/rdpear_common.c'],
}
if not is_windows and not is_android and not is_darwin
  rdpear_krb5 = dependency('mit-krb5', required : false)
  if not rdpear_krb5.found()
    rdpear_krb5 = dependency('krb5', required : false)  # MIT on most distros
  endif
  if rdpear_krb5.found()
    rdpear_entry += {
      'client' : {
        'srcs' : ['rdpear/client/rdpear_main.c'],
        'entry' : 'DVCPluginEntry', 'deps' : [rdpear_krb5],
      },
    }
  endif
endif
channel_registry += [rdpear_entry]

# rdpecam: camera redirection. Server is portable; client requires V4L (Linux) +
# FFmpeg + SWScale, with a v4l subsystem that needs libusb.
rdpecam_entry = {
  'name' : 'rdpecam', 'type' : 'dynamic',
  'server' : {
    'srcs' : ['rdpecam/server/camera_device_enumerator_main.c', 'rdpecam/server/camera_device_main.c'],
    'entry' : 'DVCPluginEntry',
  },
}
if cc.has_header('linux/videodev2.h') and with_swscale and ffmpeg_found and swscale_dep.found()
  rdpecam_client = {
    'srcs' : ['rdpecam/client/camera_device_enum_main.c', 'rdpecam/client/camera_device_main.c',
              'rdpecam/client/encoding.c'],
    'entry' : 'DVCPluginEntry',
    'deps' : [swscale_dep, avcodec_dep, avutil_dep],
    'c_args' : ['-DWITH_V4L', '-DWITH_INPUT_FORMAT_H264', '-DWITH_INPUT_FORMAT_MJPG'],
  }
  if libusb_dep.found()
    rdpecam_client += {
      'subsystems' : [{
        'name' : 'v4l',
        'srcs' : ['rdpecam/client/v4l/camera_v4l.c', 'rdpecam/client/v4l/uvc_h264.c'],
        'deps' : [libusb_dep],
        'c_args' : ['-DWITH_V4L'],
      }],
    }
  endif
  rdpecam_entry += {'client' : rdpecam_client}
endif
channel_registry += [rdpecam_entry]

channel_common_deps = [freerdp_dep, winpr_dep]

############################################################
# Audio backends for subsystem channels audin/rdpsnd
# (CMake: WITH_ALSA/PULSE/OSS/SNDIO/WINMM/MACAUDIO -> add_channel_client_subsystem).
# Each backend builds <channel>/client/<be>/<channel>_<be>.<ext>.
############################################################
audio_backends = []
alsa_feat = get_option('with_alsa')
if (alsa_feat.enabled() or alsa_feat.auto()) and is_unix and not is_darwin
  alsa_dep = dependency('alsa', required : alsa_feat.enabled())
  if alsa_dep.found()
    audio_backends += {'name' : 'alsa', 'ext' : 'c', 'deps' : [alsa_dep]}
  endif
endif
pulse_feat = get_option('with_pulse')
if (pulse_feat.enabled() or pulse_feat.auto()) and is_unix and not is_darwin
  pulse_dep = dependency('libpulse', required : pulse_feat.enabled())
  if pulse_dep.found()
    audio_backends += {'name' : 'pulse', 'ext' : 'c',
                       'deps' : [pulse_dep, dependency('libpulse-simple', required : false)]}
  endif
endif
oss_feat = get_option('with_oss')
if (oss_feat.enabled() or oss_feat.auto()) and is_unix and not is_darwin
  # Platform-specific OSS header (CMake: FindOSS.cmake).
  if is_freebsd
    oss_hdr = 'sys/soundcard.h'
  elif is_openbsd
    oss_hdr = 'machine/soundcard.h'
  else
    oss_hdr = 'linux/soundcard.h'
  endif
  if cc.has_header(oss_hdr)
    # Generate oss-includes.h (CMake: cmake/oss-includes.h.in) into build/channels/
    # so the OSS backend's #include <oss-includes.h> resolves.
    oss_cfg = configuration_data()
    oss_cfg.set('OSS_HDR_NAME', oss_hdr)
    configure_file(input : tmpl_oss_includes, output : 'oss-includes.h',
                   configuration : oss_cfg)
    audio_backends += {'name' : 'oss', 'ext' : 'c', 'deps' : [],
                       'extra_inc' : [include_directories('.')]}
  endif
endif
sndio_feat = get_option('with_sndio')
if (sndio_feat.enabled() or sndio_feat.auto()) and is_openbsd
  sndio_dep = cc.find_library('sndio', required : sndio_feat.enabled())
  if sndio_dep.found()
    audio_backends += {'name' : 'sndio', 'ext' : 'c', 'deps' : [sndio_dep]}
  endif
endif
if get_option('with_winmm') and is_windows
  audio_backends += {'name' : 'winmm', 'ext' : 'c', 'deps' : [cc.find_library('winmm')]}
endif
if get_option('with_macaudio') and is_darwin
  audio_backends += {'name' : 'mac', 'ext' : 'm',
                     'deps' : [dependency('appleframeworks', modules : ['AudioToolbox', 'CoreAudio'])]}
endif

channels_client_objlibs = []
channels_server_objlibs = []
client_modules_meta = []      # JSON fragments for the dispatch-table generator
# External link deps from subsystem backends (alsa/pulse/...). They must be
# attached to the channels-client framework directly: Meson does not reliably
# propagate external deps through a two-level link_whole chain
# (subsystem.a -> channels-client.a -> libfreerdp-client.so).
channels_client_link_deps = []

foreach ch : channel_registry
  cname = ch['name']
  cupper = cname.to_upper()
  channel_inc = include_directories(cname)
  # Some channels keep shared code in a common/ subdir (CMake: add_subdirectory(common)
  # + include_directories(common)). Compile those sources into each side and add
  # the common/ dir to the include path.
  common_files = ch.has_key('common') ? files(ch['common']) : []
  # A channel's common/ dir holds shared headers (and sometimes sources); add it
  # to the include path whenever it exists (CMake: include_directories(common)).
  common_inc = fs.is_dir(cname / 'common') ? [include_directories(cname / 'common')] : []
  client_inc = [freerdp_public_inc, winpr_inc, channel_inc] + common_inc
  channel_built = false

  if with_client_channels and ch.has_key('client')
    cl = ch['client']
    entries = cl.has_key('entries') ? cl['entries'] : [cl['entry']]
    libname = '@0@-client'.format(cname)
    channels_client_objlibs += static_library(
      libname,
      files(cl['srcs']) + common_files,
      include_directories : client_inc,
      dependencies : channel_common_deps + cl.get('deps', []),
      c_args : cl.get('c_args', []),
      gnu_symbol_visibility : default_symbol_visibility,
    )
    channels_client_link_deps += cl.get('deps', [])

    # Subsystem backends. Two sources: the audio backend set (audin/rdpsnd via
    # 'audio':true) and explicit per-channel subsystems (printer/urbdrc/... via
    # 'subsystems': [{name, srcs, deps[, extra_inc]}]).
    subsystems = []
    if cl.get('audio', false)
      foreach be : audio_backends
        subsystems += {
          'name' : be['name'],
          'srcs' : ['@0@/client/@1@/@0@_@1@.@2@'.format(cname, be['name'], be['ext'])],
          'deps' : be['deps'],
          'extra_inc' : be.get('extra_inc', []),
        }
      endforeach
    endif
    subsystems += cl.get('subsystems', [])

    subsystem_names = []
    foreach ss : subsystems
      channels_client_objlibs += static_library(
        '@0@-client-@1@'.format(cname, ss['name']),
        files(ss['srcs']),
        include_directories : client_inc + [include_directories(cname / 'client')] + ss.get('extra_inc', []),
        dependencies : channel_common_deps + ss['deps'],
        c_args : ss.get('c_args', []),
        gnu_symbol_visibility : default_symbol_visibility,
      )
      channels_client_link_deps += ss['deps']
      subsystem_names += ss['name']
    endforeach

    entries_json = '["' + '","'.join(entries) + '"]'
    subs_json = subsystem_names.length() > 0 \
      ? '["' + '","'.join(subsystem_names) + '"]' : '[]'
    client_modules_meta += '{"channel":"@0@","name":"@1@","entries":@2@,"subsystems":@3@}'.format(
      cname, libname, entries_json, subs_json)

    config_h.set('CHANNEL_@0@_CLIENT'.format(cupper), true)
    channel_built = true
  endif

  if with_server_channels and ch.has_key('server')
    sv = ch['server']
    channels_server_objlibs += static_library(
      '@0@-server'.format(cname),
      files(sv['srcs']) + common_files,
      include_directories : [freerdp_public_inc, winpr_inc, channel_inc] + common_inc,
      dependencies : channel_common_deps,
      gnu_symbol_visibility : default_symbol_visibility,
    )
    config_h.set('CHANNEL_@0@_SERVER'.format(cupper), true)
    channel_built = true
  endif

  # Base channel define (CMake: #cmakedefine CHANNEL_<NAME>) + a couple of
  # plugin-level aliases used by config.h.in.
  if channel_built
    config_h.set('CHANNEL_@0@'.format(cupper), true)
    if cname == 'rdpdr'
      config_h.set('WITH_RDPDR', true)
    elif cname == 'gfxredir'
      config_h.set('WITH_CHANNEL_GFXREDIR', true)
    endif
  endif
endforeach

if with_client_channels
  subdir('client')
endif
if with_server_channels
  subdir('server')
endif
