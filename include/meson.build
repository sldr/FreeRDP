# FreeRDP public headers + generated config headers
# Mirrors include/CMakeLists.txt
#
# In CMake this directory is processed last so that every WITH_*/CHANNEL_*
# variable is known. The Meson port accumulates those into `config_h` across
# the sub-builds and generates the headers here.

# include_directories('.') exposes both the source include/ tree (for the
# checked-in public headers, e.g. <freerdp/types.h>) and the corresponding
# build/include/ tree (for the generated headers, e.g. <freerdp/config.h>).
freerdp_public_inc = include_directories('.')

# Generate the config headers into build/include/freerdp/ so that
# <freerdp/config.h> resolves through freerdp_public_inc.
subdir('freerdp')

# Install the checked-in public headers (*.h) into include/freerdp3/freerdp.
install_subdir('freerdp',
  install_dir : freerdp_include_dir,
  exclude_files : ['meson.build', 'settings_types_private.h'],
)
