# WinPR rpc module (mirrors winpr/libwinpr/rpc/CMakeLists.txt)
winpr_srcs += files('rpc.c')
# OpenSSL include/libs already added at library level when found.

if is_windows
  winpr_pub_deps += cc.find_library('ws2_32')
  winpr_pub_deps += cc.find_library('rpcrt4')
endif
