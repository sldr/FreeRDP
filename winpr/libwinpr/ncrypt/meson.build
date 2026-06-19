# WinPR ncrypt module (mirrors winpr/libwinpr/ncrypt/CMakeLists.txt)
ncrypt_srcs = ['ncrypt.c']
if with_pkcs11
  ncrypt_srcs += 'ncrypt_pkcs11.c'
endif
winpr_srcs += files(ncrypt_srcs)

if is_windows
  winpr_pub_deps += cc.find_library('ncrypt')
endif
