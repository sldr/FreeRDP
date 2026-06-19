# libfreerdp crypto module (mirrors libfreerdp/crypto/CMakeLists.txt)
libfreerdp_srcs += files(
  'er.c', 'der.c', 'ber.c', 'per.c', 'base64.c', 'x509_utils.c',
  'cert_common.c', 'privatekey.c', 'certificate.c', 'certificate_data.c',
  'certificate_store.c', 'crypto.c', 'tls.c', 'opensslcompat.c',
)

if with_openssl
  libfreerdp_priv_deps += openssl_dep
endif
if with_mbedtls
  libfreerdp_priv_deps += mbedtls_dep
endif
if is_windows
  libfreerdp_priv_deps += cc.find_library('ws2_32')
endif
