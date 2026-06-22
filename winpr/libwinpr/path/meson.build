# WinPR path module (mirrors winpr/libwinpr/path/CMakeLists.txt)
winpr_srcs += files('path.c', 'shell.c')

if is_windows
  # MSVC or MinGW
  winpr_pub_deps += cc.find_library('shlwapi')
endif
