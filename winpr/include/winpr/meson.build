# Generated WinPR config headers (mirrors the cleaning_configure_file() calls
# in winpr/include/CMakeLists.txt). Nested so output lands in build/include/winpr/.

winpr_gen_install_dir = winpr_include_dir / 'winpr'

# version.h
winpr_version_data = configuration_data()
winpr_version_data.set('WINPR_VERSION_MAJOR', winpr_version_major)
winpr_version_data.set('WINPR_VERSION_MINOR', winpr_version_minor)
winpr_version_data.set('WINPR_VERSION_REVISION', winpr_version_revision)
winpr_version_data.set('WINPR_VERSION_SUFFIX', winpr_version_suffix)
winpr_version_data.set('WINPR_API_VERSION', winpr_api_version)
winpr_version_data.set('WINPR_VERSION', winpr_version)
winpr_version_data.set('WINPR_VERSION_FULL', winpr_version_full)
winpr_version_data.set('GIT_REVISION', git_revision)
configure_file(
  input : winpr_tmpl_version, output : 'version.h',
  configuration : winpr_version_data, format : 'cmake',
  install : true, install_dir : winpr_gen_install_dir,
)

# build-config.h (WinPR reuses the FreeRDP install path layout)
winpr_buildconfig_data = configuration_data()
winpr_buildconfig_data.set('WINPR_DATA_PATH', freerdp_data_path)
winpr_buildconfig_data.set('WINPR_KEYMAP_PATH', '')
winpr_buildconfig_data.set('WINPR_PLUGIN_PATH', freerdp_plugin_path)
winpr_buildconfig_data.set('CMAKE_INSTALL_PREFIX', freerdp_install_prefix)
winpr_buildconfig_data.set('CMAKE_INSTALL_FULL_SYSCONFDIR', prefix / get_option('sysconfdir'))
winpr_buildconfig_data.set('WINPR_LIBRARY_PATH', freerdp_library_path)
winpr_buildconfig_data.set('WINPR_ADDIN_PATH', freerdp_addin_path)
winpr_buildconfig_data.set('CMAKE_SHARED_LIBRARY_SUFFIX', shared_lib_suffix)
winpr_buildconfig_data.set('CMAKE_SHARED_LIBRARY_PREFIX', shared_lib_prefix)
winpr_buildconfig_data.set('VENDOR', vendor)
winpr_buildconfig_data.set('PRODUCT', product)
winpr_buildconfig_data.set('WINPR_PROXY_PLUGINDIR', freerdp_proxy_plugindir)
configure_file(
  input : winpr_tmpl_buildconfig, output : 'build-config.h',
  configuration : winpr_buildconfig_data, format : 'cmake',
  install : true, install_dir : winpr_gen_install_dir,
)

# buildflags.h
winpr_buildflags_data = configuration_data()
winpr_buildflags_data.set('CURRENT_C_FLAGS', ' '.join(common_c_args))
winpr_buildflags_data.set('CMAKE_C_COMPILER_ID', cc.get_id())
winpr_buildflags_data.set('CMAKE_C_COMPILER_VERSION', cc.version())
winpr_buildflags_data.set('TARGET_ARCH', target_arch)
winpr_buildflags_data.set('WINPR_BUILD_CONFIG', ' '.join(freerdp_build_config_list))
winpr_buildflags_data.set('CURRENT_BUILD_CONFIG', get_option('buildtype'))
configure_file(
  input : winpr_tmpl_buildflags, output : 'buildflags.h',
  configuration : winpr_buildflags_data, format : 'cmake',
  install : true, install_dir : winpr_gen_install_dir,
)

# config.h (feature detection populated in winpr/meson.build)
configure_file(
  input : winpr_tmpl_config, output : 'config.h',
  configuration : winpr_config, format : 'cmake',
  install : true, install_dir : winpr_gen_install_dir,
)
