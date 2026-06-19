# WinPR crypto module (mirrors winpr/libwinpr/crypto/CMakeLists.txt)
crypto_srcs = ['hash.c', 'rand.c', 'cipher.c', 'cert.c', 'crypto.c']
if with_internal_rc4
  crypto_srcs += 'rc4.c'
endif
if with_internal_md4
  crypto_srcs += 'md4.c'
endif
if with_internal_md5
  crypto_srcs += ['md5.c', 'hmac_md5.c']
endif
winpr_srcs += files(crypto_srcs)

if is_windows
  winpr_pub_deps += cc.find_library('crypt32')
endif
