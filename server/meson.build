# FreeRDP servers (mirrors server/CMakeLists.txt)

# CMake package template lives here at server/; common/ (where the descriptor is
# assembled) can't reference it with files('../'), so expose the handle now.
freerdp_server_config_cmake_in = files('FreeRDP-ServerConfig.cmake.in')

subdir('common')

if get_option('with_sample')
  subdir('Sample')
endif

# Proxy server (requires the client common library, like CMake links freerdp-client).
if get_option('with_proxy') and get_option('with_client_common')
  subdir('proxy')
endif

# Shadow server (CMake skips it on Apple — "Mac shadow server no longer compiles").
if get_option('with_shadow') and not is_darwin
  subdir('shadow')
endif

# Further 5b work: Windows platform server.
