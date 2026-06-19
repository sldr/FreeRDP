# libfreerdp core module (mirrors libfreerdp/core/CMakeLists.txt)

# linux 5.11+ AF_VSOCK fields (CMake: HAVE_AF_VSOCK_H -> config.h)
if cc.has_header_symbol('linux/vm_sockets.h', 'VMADDR_FLAG_TO_HOST',
                        prefix : '#include <ctype.h>\n#include <sys/socket.h>')
  config_h.set('HAVE_AF_VSOCK_H', true)
endif

# CMake: freerdp_definition_add(EXT_PATH="${FREERDP_EXTENSION_PATH}")
libfreerdp_defs += 'EXT_PATH="@0@"'.format(prefix / libdir / freerdp_extension_postfix)

core_srcs = [
  'state.c', 'utils.c', 'streamdump.c', 'activation.c', 'gcc.c', 'mcs.c',
  'nla.c', 'smartcardlogon.c', 'nego.c', 'info.c', 'input.c', 'license.c',
  'errinfo.c', 'errbase.c', 'errconnect.c', 'security.c', 'settings.c',
  'orders.c', 'freerdp.c', 'graphics.c', 'client.c', 'server.c', 'codecs.c',
  'metrics.c', 'capabilities.c', 'connection.c', 'redirection.c',
  'autodetect.c', 'heartbeat.c', 'multitransport.c', 'timezone.c',
  'childsession.c', 'rdp.c', 'tcp.c', 'proxy.c', 'tpdu.c', 'tpkt.c',
  'fastpath.c', 'surface.c', 'transport.c', 'update.c', 'message.c',
  'channels.c', 'window.c', 'listener.c', 'peer.c', 'display.c',
  'credssp_auth.c', 'rdstls.c', 'aad.c', 'timer.c',
]

gateway_srcs = [
  'gateway/tsg.c', 'gateway/rdg.c', 'gateway/rpc.c', 'gateway/rpc_bind.c',
  'gateway/rpc_client.c', 'gateway/rpc_fault.c', 'gateway/rts.c',
  'gateway/rts_signature.c', 'gateway/http.c', 'gateway/websocket.c',
  'gateway/wst.c', 'gateway/arm.c', 'gateway/ncacn_http.c',
]

libfreerdp_srcs += files(core_srcs + gateway_srcs)

if with_openssl
  libfreerdp_priv_deps += openssl_dep
endif
if is_windows
  libfreerdp_priv_deps += cc.find_library('ws2_32')
endif
