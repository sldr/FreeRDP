# WinPR sspi module (mirrors winpr/libwinpr/sspi/CMakeLists.txt)
sspi_srcs = [
  'CredSSP/credssp.c',
  'NTLM/ntlm_av_pairs.c', 'NTLM/ntlm_compute.c', 'NTLM/ntlm_message.c', 'NTLM/ntlm.c',
  'Kerberos/kerberos.c',
  'Negotiate/negotiate.c',
  'Schannel/schannel_openssl.c', 'Schannel/schannel.c',
  'sspi_winpr.c', 'sspi_export.c', 'sspi_gss.c', 'sspi.c',
]

# WITH_DEBUG_SCHANNEL (default off) handled via debug options if needed.

# Kerberos (CMake: WITH_KRB5, default ON for non-Windows/Apple/Android)
krb5_default = not (is_windows or is_android or is_darwin)
krb5_feat = get_option('with_krb5')
with_krb5 = krb5_feat.enabled() or (krb5_feat.auto() and krb5_default)
if with_krb5
  # MIT first (krb5/mit-krb5), then Heimdal.
  krb5_dep = dependency('mit-krb5', required : false)
  krb5_flavour = 'MIT'
  if not krb5_dep.found()
    krb5_dep = dependency('krb5', required : false)
  endif
  if not krb5_dep.found()
    krb5_dep = dependency('heimdal-krb5', required : false)
    krb5_flavour = 'Heimdal'
  endif
  if not krb5_dep.found()
    if krb5_feat.enabled()
      error('with_krb5=enabled but no MIT or Heimdal Kerberos found')
    endif
    with_krb5 = false
  endif
  if with_krb5
    winpr_priv_deps += krb5_dep
    winpr_defs += 'WITH_KRB5'
    if krb5_flavour == 'MIT'
      winpr_defs += 'WITH_KRB5_MIT'
      sspi_srcs += 'Kerberos/krb5glue_mit.c'
    else
      winpr_defs += 'WITH_KRB5_HEIMDAL'
      sspi_srcs += 'Kerberos/krb5glue_heimdal.c'
    endif
  endif
endif

winpr_srcs += files(sspi_srcs)

if is_windows
  winpr_pub_deps += cc.find_library('ws2_32')
endif
