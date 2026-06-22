# X11 shadow capture subsystem (mirrors server/shadow/X11/CMakeLists.txt)
x11_shadow_deps = [freerdp_dep, winpr_dep, dependency('x11', required : true)]
x11_shadow_c_args = ['-DWITH_X11', '-DWITH_SHADOW_X11']

# Optional X extensions (each adds a WITH_* define when present).
foreach ext : [['xext', 'WITH_XEXT'], ['xinerama', 'WITH_XINERAMA'],
               ['xdamage', 'WITH_XDAMAGE'], ['xfixes', 'WITH_XFIXES'],
               ['xtst', 'WITH_XTEST']]
  dep = dependency(ext[0], required : false)
  if dep.found()
    x11_shadow_deps += dep
    x11_shadow_c_args += '-D' + ext[1]
  endif
endforeach
if cc.has_header('X11/extensions/XShm.h')
  x11_shadow_c_args += '-DWITH_XSHM'
endif

# PAM authentication (CMake: FindPAM, optional)
pam_feat = get_option('with_pam')
pam_dep = cc.find_library('pam', required : pam_feat.enabled(),
                          has_headers : ['security/pam_appl.h'])
if pam_dep.found()
  x11_shadow_deps += pam_dep
  x11_shadow_c_args += '-DWITH_PAM'
endif

freerdp_shadow_subsystem_impl = static_library(
  'freerdp-shadow-subsystem-impl',
  files('x11_shadow.c'),
  include_directories : [freerdp_public_inc, winpr_inc],
  dependencies : x11_shadow_deps,
  c_args : x11_shadow_c_args,
  gnu_symbol_visibility : default_symbol_visibility,
)
