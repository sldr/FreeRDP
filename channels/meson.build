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
channel_registry = [
  {
    'name' : 'drdynvc', 'type' : 'static',
    'client' : {'srcs' : ['drdynvc/client/drdynvc_main.c'], 'entry' : 'VirtualChannelEntryEx'},
    'server' : {'srcs' : ['drdynvc/server/drdynvc_main.c'], 'entry' : 'VirtualChannelEntry'},
  },
  {
    'name' : 'echo', 'type' : 'dynamic',
    'client' : {'srcs' : ['echo/client/echo_main.c'], 'entry' : 'DVCPluginEntry'},
    'server' : {'srcs' : ['echo/server/echo_main.c'], 'entry' : 'DVCPluginEntry'},
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
    'name' : 'rdpdr', 'type' : 'static',
    'client' : {
      'srcs' : ['rdpdr/client/irp.c', 'rdpdr/client/devman.c', 'rdpdr/client/rdpdr_main.c',
                'rdpdr/client/rdpdr_capabilities.c'],
      'entry' : 'VirtualChannelEntryEx',
    },
    'server' : {'srcs' : ['rdpdr/server/rdpdr_main.c'], 'entry' : 'VirtualChannelEntry'},
  },
  {
    'name' : 'rail', 'type' : 'static',
    'client' : {
      'srcs' : ['rail/rail_common.c', 'rail/client/client_rails.c', 'rail/client/rail_main.c',
                'rail/client/rail_orders.c'],
      'entry' : 'VirtualChannelEntryEx',
    },
    'server' : {
      'srcs' : ['rail/rail_common.c', 'rail/server/rail_main.c'],
      'entry' : 'VirtualChannelEntryEx',
    },
  },
]

channels_client_objlibs = []
channels_server_objlibs = []
client_modules_meta = []      # JSON fragments for the dispatch-table generator
channel_common_deps = [freerdp_dep, winpr_dep]

foreach ch : channel_registry
  cname = ch['name']
  channel_inc = include_directories(cname)

  if with_client_channels and ch.has_key('client')
    cl = ch['client']
    libname = '@0@-client'.format(cname)
    channels_client_objlibs += static_library(
      libname,
      files(cl['srcs']),
      include_directories : [freerdp_public_inc, winpr_inc, channel_inc],
      dependencies : channel_common_deps,
      gnu_symbol_visibility : default_symbol_visibility,
    )
    client_modules_meta += '{"channel":"@0@","name":"@1@","entries":["@2@"],"subsystems":[]}'.format(
      cname, libname, cl['entry'])
  endif

  if with_server_channels and ch.has_key('server')
    sv = ch['server']
    channels_server_objlibs += static_library(
      '@0@-server'.format(cname),
      files(sv['srcs']),
      include_directories : [freerdp_public_inc, winpr_inc, channel_inc],
      dependencies : channel_common_deps,
      gnu_symbol_visibility : default_symbol_visibility,
    )
  endif
endforeach

if with_client_channels
  subdir('client')
endif
if with_server_channels
  subdir('server')
endif
