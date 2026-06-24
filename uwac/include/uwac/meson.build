# Generated UWAC config headers (mirrors uwac/templates/CMakeLists.txt)
uwac_gen_install_dir = uwac_include_dir / 'uwac'

uwac_version_data = configuration_data()
uwac_version_data.set('UWAC_VERSION_MAJOR', uwac_version_major)
uwac_version_data.set('UWAC_VERSION_MINOR', uwac_version_minor)
uwac_version_data.set('UWAC_VERSION_REVISION', uwac_version_revision)
uwac_version_data.set('UWAC_VERSION_SUFFIX', '')
uwac_version_data.set('UWAC_API_VERSION', uwac_api_version)
uwac_version_data.set('UWAC_VERSION', uwac_version)
uwac_version_data.set('UWAC_VERSION_FULL', uwac_version_full)
uwac_version_data.set('GIT_REVISION', git_revision)
configure_file(input : uwac_tmpl_version, output : 'version.h',
  configuration : uwac_version_data, format : 'cmake',
  install : true, install_dir : uwac_gen_install_dir)

uwac_buildconfig_data = configuration_data()
uwac_buildconfig_data.set('WINPR_DATA_PATH', freerdp_data_path)
uwac_buildconfig_data.set('WINPR_KEYMAP_PATH', '')
uwac_buildconfig_data.set('WINPR_PLUGIN_PATH', freerdp_plugin_path)
uwac_buildconfig_data.set('WINPR_INSTALL_PREFIX', freerdp_install_prefix)
uwac_buildconfig_data.set('WINPR_LIBRARY_PATH', freerdp_library_path)
uwac_buildconfig_data.set('WINPR_ADDIN_PATH', freerdp_addin_path)
uwac_buildconfig_data.set('WINPR_PROXY_PLUGINDIR', freerdp_proxy_plugindir)
uwac_buildconfig_data.set('CMAKE_SHARED_LIBRARY_SUFFIX', shared_lib_suffix)
uwac_buildconfig_data.set('CMAKE_SHARED_LIBRARY_PREFIX', shared_lib_prefix)
uwac_buildconfig_data.set('VENDOR', vendor)
uwac_buildconfig_data.set('PRODUCT', product)
configure_file(input : uwac_tmpl_buildconfig, output : 'build-config.h',
  configuration : uwac_buildconfig_data, format : 'cmake',
  install : true, install_dir : uwac_gen_install_dir)

uwac_buildflags_data = configuration_data()
uwac_buildflags_data.set('CURRENT_C_FLAGS', ' '.join(common_c_args))
uwac_buildflags_data.set('CMAKE_C_COMPILER_ID', cc.get_id())
uwac_buildflags_data.set('CMAKE_C_COMPILER_VERSION', cc.version())
uwac_buildflags_data.set('TARGET_ARCH', target_arch)
uwac_buildflags_data.set('UWAC_BUILD_CONFIG', ' '.join(freerdp_build_config_list))
uwac_buildflags_data.set('CURRENT_BUILD_CONFIG', get_option('buildtype'))
configure_file(input : uwac_tmpl_buildflags, output : 'buildflags.h',
  configuration : uwac_buildflags_data, format : 'cmake',
  install : true, install_dir : uwac_gen_install_dir)

configure_file(input : uwac_tmpl_config, output : 'config.h',
  configuration : uwac_config, format : 'cmake',
  install : true, install_dir : uwac_gen_install_dir)
