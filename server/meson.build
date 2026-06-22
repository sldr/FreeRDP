# FreeRDP servers (mirrors server/CMakeLists.txt)

subdir('common')

if get_option('with_sample')
  subdir('Sample')
endif

# Proxy server (requires the client common library, like CMake links freerdp-client).
if get_option('with_proxy') and get_option('with_client_common')
  subdir('proxy')
endif

# Further 5b work: shadow (X11/Win/Mac, needs rdtk), Windows platform server.
