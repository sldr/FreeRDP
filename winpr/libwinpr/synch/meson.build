# WinPR synch module (mirrors winpr/libwinpr/synch/CMakeLists.txt)
winpr_srcs += files(
  'address.c', 'barrier.c', 'critical.c', 'event.c', 'init.c', 'mutex.c',
  'pollset.c', 'semaphore.c', 'sleep.c', 'timer.c', 'wait.c',
)

if is_freebsd
  epollshim_dep = dependency('epoll-shim', required : false)
  if epollshim_dep.found()
    winpr_priv_deps += epollshim_dep
  endif
endif
