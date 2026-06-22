# FreeRDP shadow server (mirrors server/shadow/CMakeLists.txt)
# Requires rdtk + winpr-tools (both built earlier). Not built on Apple.

shadow_inc = [freerdp_public_inc, winpr_inc, rdtk_inc]

freerdp_shadow_srcs = files(
  'shadow_client.c', 'shadow_lobby.c', 'shadow_input.c', 'shadow_screen.c',
  'shadow_surface.c', 'shadow_encoder.c', 'shadow_capture.c', 'shadow_channels.c',
  'shadow_encomsp.c', 'shadow_remdesk.c', 'shadow_rdpsnd.c', 'shadow_audin.c',
  'shadow_rdpgfx.c', 'shadow_subsystem.c', 'shadow_mcevent.c', 'shadow_server.c',
)

freerdp_shadow_libname = with_library_versioning \
  ? 'freerdp-shadow@0@'.format(freerdp_version_major) : 'freerdp-shadow'
shadow_lib_kwargs = with_library_versioning \
  ? {'version' : freerdp_version, 'soversion' : freerdp_version_major} \
  : {'name_prefix' : ''}

freerdp_shadow_lib = library(
  freerdp_shadow_libname,
  freerdp_shadow_srcs,
  include_directories : shadow_inc,
  dependencies : [freerdp_server_dep, freerdp_dep, winpr_dep, winpr_tools_dep, rdtk_dep],
  gnu_symbol_visibility : default_symbol_visibility,
  install : true,
  kwargs : shadow_lib_kwargs,
)
freerdp_shadow_dep = declare_dependency(
  link_with : freerdp_shadow_lib,
  include_directories : shadow_inc,
  dependencies : [freerdp_dep, winpr_dep],
)

# Platform capture subsystem -> static lib `freerdp_shadow_subsystem_impl`.
# Needs a real backend: Win (Windows) or X11 (Linux/BSD with X11). Without one
# (e.g. X11 disabled) fall back to the dummy Sample subsystem so shadow still builds.
if get_option('with_shadow_subsystem') and (is_windows or with_x11)
  if is_windows
    subdir('Win')
  else
    subdir('X11')   # not darwin (shadow is skipped on Apple)
  endif
else
  subdir('Sample')
endif

# Subsystem registry lib (CMake: freerdp-shadow-subsystem)
freerdp_shadow_subsystem_libname = with_library_versioning \
  ? 'freerdp-shadow-subsystem@0@'.format(freerdp_version_major) : 'freerdp-shadow-subsystem'
freerdp_shadow_subsystem_lib = library(
  freerdp_shadow_subsystem_libname,
  files('shadow_subsystem_builtin.c'),
  include_directories : shadow_inc,
  link_with : freerdp_shadow_subsystem_impl,
  dependencies : [freerdp_shadow_dep, freerdp_dep, winpr_dep],
  gnu_symbol_visibility : default_symbol_visibility,
  install : true,
  kwargs : shadow_lib_kwargs,
)
freerdp_shadow_subsystem_dep = declare_dependency(
  link_with : freerdp_shadow_subsystem_lib,
  include_directories : shadow_inc,
)

if get_option('with_server_shadow_cli')
  subdir('cli')
endif

pkgconfig.generate(
  freerdp_shadow_lib,
  name : 'FreeRDP-Shadow',
  description : 'FreeRDP: A Remote Desktop Protocol Implementation (shadow)',
  url : 'http://www.freerdp.com/',
  version : freerdp_version,
  filebase : 'freerdp-shadow@0@'.format(freerdp_version_major),
  subdirs : 'freerdp@0@'.format(freerdp_version_major),
  requires : 'freerdp@0@'.format(freerdp_version_major),
)
