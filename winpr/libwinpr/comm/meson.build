# WinPR comm module (mirrors winpr/libwinpr/comm/CMakeLists.txt)
# Only built on non-Windows platforms.
if not is_windows
  comm_srcs = ['comm.c']
  if not is_darwin
    # Serial port support (CMake: WINPR_HAVE_SERIAL_SUPPORT, not on Apple/Emscripten)
    winpr_defs += 'WINPR_HAVE_SERIAL_SUPPORT'
    comm_srcs += [
      'comm_io.c', 'comm_ioctl.c', 'comm_serial_sys.c',
      'comm_sercx_sys.c', 'comm_sercx2_sys.c',
    ]
  else
    comm_srcs += ['comm_ioctl_dummy.c']
  endif
  winpr_srcs += files(comm_srcs)
endif
