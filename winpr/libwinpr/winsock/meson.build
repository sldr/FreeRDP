# WinPR winsock module (mirrors winpr/libwinpr/winsock/CMakeLists.txt)
winpr_srcs += files('winsock.c')

if is_windows
  winpr_pub_deps += cc.find_library('ws2_32')
endif
