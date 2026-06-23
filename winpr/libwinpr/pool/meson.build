# WinPR pool module (mirrors winpr/libwinpr/pool/CMakeLists.txt)
winpr_srcs += files(
  'synch.c', 'work.c', 'timer.c', 'io.c', 'cleanup_group.c',
  'pool.c', 'callback.c', 'callback_cleanup.c',
)
# Default threadpool sizing (CMake: pool/CMakeLists.txt winpr_definition_add, since 3.x).
winpr_defs += ['WINPR_THREADPOOL_DEFAULT_MAX_COUNT=16', 'WINPR_THREADPOOL_DEFAULT_MIN_COUNT=4']
# Thread + dl libs are already in winpr_priv_deps.
