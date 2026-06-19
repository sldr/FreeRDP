# WinPR crt module (mirrors winpr/libwinpr/crt/CMakeLists.txt)
crt_srcs = [
  'alignment.c', 'conversion.c', 'buffer.c', 'memory.c',
  'unicode.c', 'string.c', 'assert.c',
]

if get_option('with_unicode_builtin')
  crt_srcs += 'unicode_builtin.c'
else
  if is_android
    crt_srcs += 'unicode_android.c'
  elif not is_darwin and not is_windows
    # ICU required for Unicode conversion on Linux/BSD
    winpr_priv_deps += [
      dependency('icu-i18n'), dependency('icu-uc'), dependency('icu-io'),
    ]
    crt_srcs += 'unicode_icu.c'
  elif is_darwin
    crt_srcs += 'unicode_apple.m'
    winpr_priv_deps += dependency('appleframeworks', modules : ['Foundation'])
  endif
endif

winpr_srcs += files(crt_srcs)
