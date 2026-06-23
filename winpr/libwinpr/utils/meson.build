# WinPR utils module (mirrors winpr/libwinpr/utils/CMakeLists.txt)

# winpr_include_directory_add(".") / CMAKE_CURRENT_SOURCE_DIR
winpr_incs += include_directories('.')

collections_srcs = [
  'collections/Object.c', 'collections/Queue.c', 'collections/Stack.c',
  'collections/PubSub.c', 'collections/BitStream.c', 'collections/ArrayList.c',
  'collections/LinkedList.c', 'collections/HashTable.c',
  'collections/ListDictionary.c', 'collections/CountdownEvent.c',
  'collections/BufferPool.c', 'collections/ObjectPool.c',
  'collections/StreamPool.c', 'collections/MessageQueue.c',
  'collections/MessagePipe.c',
]

wlog_srcs = [
  'wlog/wlog.c', 'wlog/Layout.c', 'wlog/Message.c', 'wlog/DataMessage.c',
  'wlog/ImageMessage.c', 'wlog/PacketMessage.c', 'wlog/Appender.c',
  'wlog/FileAppender.c', 'wlog/BinaryAppender.c', 'wlog/CallbackAppender.c',
  'wlog/ConsoleAppender.c', 'wlog/UdpAppender.c',
]
if winpr_have_syslog
  wlog_srcs += 'wlog/SyslogAppender.c'
endif

# systemd journald appender (CMake: WITH_SYSTEMD, default = libsystemd found)
systemd_feat = get_option('with_systemd')
if systemd_feat.allowed()
  libsystemd_dep = dependency('libsystemd', required : systemd_feat.enabled())
  if libsystemd_dep.found()
    winpr_priv_deps += libsystemd_dep
    wlog_srcs += 'wlog/JournaldAppender.c'
    winpr_config.set('WINPR_HAVE_JOURNALD_H', true)
  endif
endif

asn1_srcs = ['asn1/asn1.c']

utils_srcs = [
  'atexit.c', 'ini.c', 'sam.c', 'ntlm.c', 'image.c', 'print.c', 'stream.c',
  'strlst.c', 'debug.c', 'winpr.c', 'cmdline.c', 'ssl.c',
]

# Backtrace backends
if winpr_have_execinfo
  winpr_defs += 'USE_EXECINFO'
  utils_srcs += 'execinfo/debug.c'
endif
if winpr_have_unwind
  winpr_defs += 'USE_UNWIND'
  utils_srcs += 'unwind/debug.c'
endif
if is_windows
  utils_srcs += 'windows/debug.c'
endif

# JSON backend (resolved in winpr/meson.build)
if winpr_json_define != ''
  winpr_defs += winpr_json_define
  winpr_priv_deps += winpr_json_dep
endif

# json/json.c always + the selected backend (json/<backend>.c or json-stub.c)
winpr_srcs += files('json/json.c', winpr_json_src)
winpr_srcs += files(utils_srcs + collections_srcs + wlog_srcs + asn1_srcs)

if is_unix
  winpr_priv_deps += m_dep
  # backtrace() may live in libexecinfo (e.g. musl/BSD) rather than libc
  execinfo_lib = cc.find_library('execinfo', required : false)
  if execinfo_lib.found()
    winpr_priv_deps += execinfo_lib
  endif
endif

if is_windows
  winpr_pub_deps += cc.find_library('dbghelp')
endif
