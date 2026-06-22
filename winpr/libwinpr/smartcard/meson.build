# WinPR smartcard module (mirrors winpr/libwinpr/smartcard/CMakeLists.txt)
smartcard_srcs = ['smartcard.c']

# WITH_WINPR_PCSC comes from the (deferred) PCSCWinPR detection.

# WITH_SMARTCARD_PCSC defaults ON
winpr_defs += 'WITH_SMARTCARD_PCSC'
smartcard_srcs += 'smartcard_pcsc.c'

if get_option('with_smartcard_inspect')
  winpr_defs += 'WITH_SMARTCARD_INSPECT'
  smartcard_srcs += 'smartcard_inspect.c'
endif

if is_windows
  smartcard_srcs += 'smartcard_windows.c'
endif

winpr_srcs += files(smartcard_srcs)
