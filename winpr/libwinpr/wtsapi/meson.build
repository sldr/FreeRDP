# WinPR wtsapi module (mirrors winpr/libwinpr/wtsapi/CMakeLists.txt)
winpr_srcs += files('wtsapi.c')

if is_windows
  winpr_srcs += files('wtsapi_win32.c')
  if cc.get_id() == 'gcc' or cc.get_id() == 'clang'
    # MinGW only (CMake: if(MINGW) -> ntdll)
    winpr_priv_deps += cc.find_library('ntdll', required : false)
  endif
endif
