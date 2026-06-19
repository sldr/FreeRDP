# WinPR timezone module (mirrors winpr/libwinpr/timezone/CMakeLists.txt)
tz_srcs = ['TimeZoneNameMapUtils.c', 'timezone.c']

# WITH_TIMEZONE_COMPILED defaults ON (compiled-in timezone definitions)
winpr_defs += 'WITH_TIMEZONE_COMPILED'

if not is_windows
  tz_srcs += ['TimeZoneIanaAbbrevMap.c']
endif

if get_option('with_timezone_icu')
  winpr_priv_deps += [dependency('icu-i18n'), dependency('icu-uc')]
  winpr_defs += 'WITH_TIMEZONE_ICU'
else
  tz_srcs += ['WindowsZones.c']
endif

winpr_srcs += files(tz_srcs)
