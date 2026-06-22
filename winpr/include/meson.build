# WinPR public headers + generated config headers (mirrors winpr/include/CMakeLists.txt)

# Exposes both source include/ and build/include/ so that both the checked-in
# public headers and the generated <winpr/config.h> resolve.
winpr_public_inc = include_directories('.')

# Generate config headers into build/include/winpr/.
subdir('winpr')

# Install the checked-in public headers (*.h) into include/winpr3/winpr.
install_subdir('winpr',
  install_dir : winpr_include_dir,
  exclude_files : ['meson.build'],
)
