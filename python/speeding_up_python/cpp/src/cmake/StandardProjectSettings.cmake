# default build type.
set(default_build_type "Release")

# Set a default build type if none was specified
if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  message(STATUS "Setting build type to '${default_build_type}' as none was specified.")
  set(CMAKE_BUILD_TYPE "${default_build_type}" CACHE
    STRING "Choose the type of build." FORCE)
  # Set the possible values of build type for cmake-gui, ccmake
  set_property(
    CACHE CMAKE_BUILD_TYPE
    PROPERTY STRINGS
             "Debug"
             "Release"
             "MinSizeRel"
             "RelWithDebInfo")
endif()

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON) # export compiler flags for code completion engines
# Generate compile_commands.json to make it easier to work with clang based tools

option(ENABLE_IPO "Enable Interprocedural Optimization, aka Link Time Optimization (LTO)" ON)

if(ENABLE_IPO)
  include(CheckIPOSupported)
  check_ipo_supported(
    RESULT
    result
    OUTPUT
    output)
  if(result)
    set(CMAKE_INTERPROCEDURAL_OPTIMIZATION TRUE)
  else()
    message(STATUS "IPO is not supported: ${output}") #SEND_ERROR or STATUS?
  endif()
endif()

if(MSVC)
  message(STATUS "Building for MSVC")
  add_compile_options("$<$<CONFIG:Release>:/O2>")
  add_compile_options("$<$<CONFIG:Release>:/fp:fast>")
elseif(CMAKE_CXX_COMPILER_ID MATCHES ".*Clang")
  message(STATUS "Building for Clang")
  add_compile_options("$<$<CONFIG:Release>:-march=native>") # "-Weffc++" -Ofast -march=native -g -fno-omit-frame-pointer -gdwarf-2 (flto not good) -Wextra -pedantic
  add_compile_options("$<$<CONFIG:Release>:-Ofast>")
  add_compile_options("$<$<CONFIG:Release>:-ffast-math>")
 # add_compile_options("$<$<CONFIG:Release>:-fopenmp>")
elseif(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
  message(STATUS "Building for GCC")
  add_compile_options("$<$<CONFIG:Release>:-march=native>") 
  add_compile_options("$<$<CONFIG:Release>:-Ofast>")
  add_compile_options("$<$<CONFIG:Release>:-ffast-math>")
#  add_compile_options("$<$<CONFIG:Release>:-fopenmp>")
else()
  message(STATUS "Building for an unknown compiler")
endif()

message(STATUS "Host system: ${CMAKE_HOST_SYSTEM}")
message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")