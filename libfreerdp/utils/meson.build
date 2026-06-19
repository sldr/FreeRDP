# libfreerdp utils module (mirrors libfreerdp/utils/CMakeLists.txt)
libfreerdp_srcs += files(
  'encoded_types.c', 'helpers.c', 'passphrase.c', 'cliprdr_utils.c',
  'rdpdr_utils.c', 'pcap.c', 'profiler.c', 'ringbuffer.c', 'signal.c',
  'string.c', 'gfx.c', 'drdynvc.c', 'smartcard_operations.c',
  'smartcard_pack.c', 'smartcard_call.c', 'stopwatch.c', 'http.c',
)

if is_windows
  libfreerdp_priv_deps += cc.find_library('ws2_32')
  libfreerdp_priv_deps += cc.find_library('credui')
  libfreerdp_priv_deps += cc.find_library('cfgmgr32')
endif

if m_dep.found()
  libfreerdp_priv_deps += m_dep
endif
