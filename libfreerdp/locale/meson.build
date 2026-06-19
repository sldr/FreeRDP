# libfreerdp locale module (mirrors libfreerdp/locale/CMakeLists.txt)
locale_srcs = ['keyboard_layout.c', 'keyboard.c', 'locale.c']

# WITH_KEYBOARD_LAYOUT_FROM_FILE (depends on WITH_WINPR_JSON, default OFF) — skipped.

if is_darwin
  if not is_ios
    locale_srcs += 'keyboard_apple.c'
    libfreerdp_priv_deps += dependency('appleframeworks', modules : ['Carbon'])
  endif
  libfreerdp_priv_deps += dependency('appleframeworks', modules : ['CoreFoundation'])
endif

if with_x11 and not without_freerdp_3x_deprecated
  x11_dep = dependency('x11', required : true)
  libfreerdp_defs += 'WITH_X11'
  libfreerdp_priv_deps += x11_dep
  locale_srcs += ['keyboard_x11.c', 'xkb_layout_ids.c']

  if is_sunos
    libfreerdp_defs += 'WITH_SUN'
    locale_srcs += ['keyboard_sun.c']
  endif

  xkbfile_dep = dependency('xkbfile', required : false)
  if xkbfile_dep.found() and not is_darwin
    libfreerdp_defs += 'WITH_XKBFILE'
    libfreerdp_priv_deps += xkbfile_dep
    locale_srcs += ['keyboard_xkbfile.c']
  endif
endif

if with_wayland and not without_freerdp_3x_deprecated
  libfreerdp_defs += 'WITH_WAYLAND'
endif

libfreerdp_srcs += files(locale_srcs)
