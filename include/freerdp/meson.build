# Generated FreeRDP config headers.
#
# This nested meson.build exists so that configure_file()/custom_target()
# output lands under build/include/freerdp/ (Meson output names cannot contain
# path separators). Mirrors the cleaning_configure_file() calls in
# include/CMakeLists.txt.

gen_install_dir = freerdp_include_dir / 'freerdp'

# version.h  (CMake: config/version.h.in)
configure_file(
  input : tmpl_version_h,
  output : 'version.h',
  configuration : version_data,
  format : 'cmake',
  install : true,
  install_dir : gen_install_dir,
)

# build-config.h  (CMake: config/build-config.h.in)
configure_file(
  input : tmpl_buildconfig_h,
  output : 'build-config.h',
  configuration : buildconfig_data,
  format : 'cmake',
  install : true,
  install_dir : gen_install_dir,
)

# config.h  (CMake: config/config.h.in)
configure_file(
  input : tmpl_config_h,
  output : 'config.h',
  configuration : config_h,
  format : 'cmake',
  install : true,
  install_dir : gen_install_dir,
)

# buildflags.h  (CMake: config/buildflags.h.in)
# Built here so the accumulated FREERDP_BUILD_CONFIG list is complete.
buildflags_data = configuration_data()
buildflags_data.set('CURRENT_C_FLAGS', ' '.join(common_c_args))
buildflags_data.set('CMAKE_C_COMPILER_ID', cc.get_id())
buildflags_data.set('CMAKE_C_COMPILER_VERSION', cc.version())
buildflags_data.set('TARGET_ARCH', target_arch)
buildflags_data.set('FREERDP_BUILD_CONFIG', ' '.join(freerdp_build_config_list))
buildflags_data.set('CURRENT_BUILD_CONFIG', get_option('buildtype'))
configure_file(
  input : tmpl_buildflags_h,
  output : 'buildflags.h',
  configuration : buildflags_data,
  format : 'cmake',
  install : true,
  install_dir : gen_install_dir,
)

# settings_keys.h  (CMake: parsed from settings_types_private.h)
settings_keys_h = custom_target(
  'settings_keys.h',
  output : 'settings_keys.h',
  command : [
    python, gen_settings_py,
    settings_types_private_h, tmpl_settings_keys_h, '@OUTPUT@',
  ],
  depend_files : [settings_types_private_h, tmpl_settings_keys_h],
  install : true,
  install_dir : gen_install_dir,
)
