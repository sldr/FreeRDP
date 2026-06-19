# WinPR sysinfo module (mirrors winpr/libwinpr/sysinfo/CMakeLists.txt)
if is_android
  subdir('cpufeatures')
endif

winpr_srcs += files('sysinfo.c')

if not is_windows and not is_darwin and not is_android and not is_openbsd
  rt_sysinfo_dep = cc.find_library('rt', required : false)
  if rt_sysinfo_dep.found()
    winpr_priv_deps += rt_sysinfo_dep
  endif
endif
