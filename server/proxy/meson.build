# FreeRDP proxy server (mirrors server/proxy/CMakeLists.txt)

with_proxy_emulate_smartcard = get_option('with_proxy_emulate_smartcard')
if with_proxy_emulate_smartcard
  config_h.set('WITH_PROXY_EMULATE_SMARTCARD', true)
endif

# pf_channels OBJECT lib (CMake: $<TARGET_OBJECTS:pf_channels>) -> compiled in directly.
proxy_srcs = [
  'pf_context.c', 'pf_channel.c', 'pf_client.c', 'pf_input.c', 'pf_update.c',
  'pf_server.c', 'pf_config.c', 'pf_modules.c', 'pf_utils.c',
  'channels/pf_channel_rdpdr.c', 'channels/pf_channel_drdynvc.c',
]
if with_proxy_emulate_smartcard
  proxy_srcs += 'channels/pf_channel_smartcard.c'
endif

proxy_inc = [freerdp_public_inc, winpr_inc, include_directories('.', 'modules')]

freerdp_proxy_libname = with_library_versioning \
  ? 'freerdp-server-proxy@0@'.format(freerdp_version_major) : 'freerdp-server-proxy'
freerdp_proxy_lib_kwargs = with_library_versioning \
  ? {'version' : freerdp_version, 'soversion' : freerdp_version_major} \
  : {'name_prefix' : ''}

freerdp_proxy_lib = library(
  freerdp_proxy_libname,
  files(proxy_srcs),
  include_directories : proxy_inc,
  dependencies : [freerdp_client_dep, freerdp_server_dep, freerdp_dep, winpr_dep],
  gnu_symbol_visibility : default_symbol_visibility,
  install : true,
  kwargs : freerdp_proxy_lib_kwargs,
)

freerdp_proxy_dep = declare_dependency(
  link_with : freerdp_proxy_lib,
  include_directories : include_directories('.', 'modules'),
  dependencies : [freerdp_dep, winpr_dep],
)

pkgconfig.generate(
  freerdp_proxy_lib,
  name : 'FreeRDP-Proxy',
  description : 'FreeRDP: A Remote Desktop Protocol Implementation (proxy)',
  url : 'http://www.freerdp.com/',
  version : freerdp_version,
  filebase : 'freerdp-server-proxy@0@'.format(freerdp_version_major),
  subdirs : 'freerdp@0@'.format(freerdp_version_major),
  requires : 'freerdp@0@'.format(freerdp_version_major),
)

if get_option('with_proxy_app')
  subdir('cli')
endif

if get_option('with_proxy_modules')
  config_h.set('WITH_PROXY_MODULES', true)
  subdir('modules')
endif
