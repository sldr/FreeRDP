# RdTk: Remote Desktop Toolkit (mirrors rdtk/CMakeLists.txt)
# Small UI toolkit used by the shadow server. Versioned independently (0.2.0).

rdtk_version_major = '0'
rdtk_version_minor = '2'
rdtk_version_revision = '0'
rdtk_version = '@0@.@1@.@2@'.format(rdtk_version_major, rdtk_version_minor, rdtk_version_revision)
rdtk_version_full = rdtk_version
rdtk_api_version = rdtk_version_major
rdtk_include_dir = 'include' / 'rdtk@0@'.format(rdtk_api_version)

rdtk_inc = include_directories('include')

# Config-header data
rdtk_version_data = configuration_data()
rdtk_version_data.set('RDTK_VERSION_MAJOR', rdtk_version_major)
rdtk_version_data.set('RDTK_VERSION_MINOR', rdtk_version_minor)
rdtk_version_data.set('RDTK_VERSION_REVISION', rdtk_version_revision)
rdtk_version_data.set('RDTK_VERSION_SUFFIX', '')
rdtk_version_data.set('RDTK_API_VERSION', rdtk_api_version)
rdtk_version_data.set('RDTK_VERSION', rdtk_version)
rdtk_version_data.set('RDTK_VERSION_FULL', rdtk_version_full)
rdtk_version_data.set('GIT_REVISION', git_revision)

rdtk_buildconfig_data = configuration_data()
rdtk_buildconfig_data.set('WINPR_DATA_PATH', freerdp_data_path)
rdtk_buildconfig_data.set('WINPR_KEYMAP_PATH', '')
rdtk_buildconfig_data.set('WINPR_PLUGIN_PATH', freerdp_plugin_path)
rdtk_buildconfig_data.set('WINPR_INSTALL_PREFIX', freerdp_install_prefix)
rdtk_buildconfig_data.set('WINPR_LIBRARY_PATH', freerdp_library_path)
rdtk_buildconfig_data.set('WINPR_ADDIN_PATH', freerdp_addin_path)
rdtk_buildconfig_data.set('CMAKE_SHARED_LIBRARY_SUFFIX', shared_lib_suffix)
rdtk_buildconfig_data.set('CMAKE_SHARED_LIBRARY_PREFIX', shared_lib_prefix)
rdtk_buildconfig_data.set('VENDOR', vendor)
rdtk_buildconfig_data.set('PRODUCT', product)

rdtk_buildflags_data = configuration_data()
rdtk_buildflags_data.set('CMAKE_CURRENT_C_FLAGS', ' '.join(common_c_args))
rdtk_buildflags_data.set('CMAKE_C_COMPILER_ID', cc.get_id())
rdtk_buildflags_data.set('CMAKE_C_COMPILER_VERSION', cc.version())
rdtk_buildflags_data.set('TARGET_ARCH', target_arch)
rdtk_buildflags_data.set('RDTK_BUILD_CONFIG', ' '.join(freerdp_build_config_list))
rdtk_buildflags_data.set('CURRENT_BUILD_CONFIG', get_option('buildtype'))

rdtk_tmpl_version = files('templates' / 'version.h.in')
rdtk_tmpl_buildconfig = files('templates' / 'build-config.h.in')
rdtk_tmpl_buildflags = files('templates' / 'buildflags.h.in')
rdtk_tmpl_config = files('templates' / 'config.h.in')

subdir('include')    # generates rdtk/{version,build-config,buildflags,config}.h
subdir('librdtk')    # rdtk library
