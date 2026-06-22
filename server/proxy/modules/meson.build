# Proxy plugin modules (mirrors server/proxy/modules/CMakeLists.txt)
# These are C++ runtime-loadable plugins (shared_module), installed to the proxy
# plugin directory. CMake discovers them via file(GLOB); enumerated here.

# Enable C++ only if a compiler is available (the modules are optional).
if not add_languages('cpp', native : false, required : false)
  warning('No C++ compiler found: skipping proxy modules')
  subdir_done()
endif

# Proxy headers (CMake: include_directories(server/proxy) + .../modules)
proxy_mod_inc = [
  freerdp_public_inc, winpr_inc,
  include_directories('..'),   # server/proxy
  include_directories('.'),    # server/proxy/modules
]

shared_module('proxy-demo-plugin', files('demo/demo.cpp'),
  include_directories : proxy_mod_inc, dependencies : [winpr_dep],
  name_prefix : '', install : true, install_dir : freerdp_proxy_plugindir)

shared_module('proxy-bitmap-filter-plugin', files('bitmap-filter/bitmap-filter.cpp'),
  include_directories : proxy_mod_inc, dependencies : [winpr_dep, freerdp_dep],
  name_prefix : '', install : true, install_dir : freerdp_proxy_plugindir)

shared_module('proxy-dyn-channel-dump-plugin', files('dyn-channel-dump/dyn-channel-dump.cpp'),
  include_directories : proxy_mod_inc,
  dependencies : [winpr_dep, freerdp_dep, freerdp_client_dep, freerdp_server_dep, freerdp_proxy_dep],
  name_prefix : '', install : true, install_dir : freerdp_proxy_plugindir)
