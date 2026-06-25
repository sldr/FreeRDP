# Downstream find_package() smoke-test for the Meson-generated CMake package files.
#
# Validates that a third-party CMake project can consume an installed FreeRDP/WinPR
# tree via find_package() + the imported targets the Meson build emits (the
# *Config.cmake / *ConfigVersion.cmake / *Targets.cmake parity with CMake's
# install(EXPORT)). Point CMAKE_PREFIX_PATH at the Meson install prefix.
cmake_minimum_required(VERSION 3.13)
project(freerdp-meson-consumer C)

find_package(WinPR REQUIRED)
find_package(FreeRDP REQUIRED)
find_package(FreeRDP-Client REQUIRED)

message(STATUS "Found WinPR ${WinPR_VERSION_MAJOR}.${WinPR_VERSION_MINOR}.${WinPR_VERSION_REVISION}")
message(STATUS "Found FreeRDP ${FreeRDP_VERSION_MAJOR}.${FreeRDP_VERSION_MINOR}.${FreeRDP_VERSION_REVISION}")
message(STATUS "FreeRDP_INCLUDE_DIR=${FreeRDP_INCLUDE_DIR}")

foreach(tgt winpr freerdp freerdp-client)
  if(NOT TARGET ${tgt})
    message(FATAL_ERROR "Imported target '${tgt}' was not defined by find_package()")
  endif()
endforeach()

add_executable(consumer main.c)
# freerdp-client's interface pulls in freerdp + winpr (includes + link) transitively.
target_link_libraries(consumer freerdp-client)
