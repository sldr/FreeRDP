# WinPR dsparse module (mirrors winpr/libwinpr/dsparse/CMakeLists.txt)
winpr_srcs += files('dsparse.c')

if is_windows
  winpr_pub_deps += cc.find_library('ntdsapi')
endif
