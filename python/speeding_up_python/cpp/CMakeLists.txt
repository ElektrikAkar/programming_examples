cmake_minimum_required(VERSION 3.15...3.27)
project(speeding_up) 

find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)

include(src/cmake/StandardProjectSettings.cmake)
include(src/cmake/Dependencies.cmake)

pybind11_add_module(speeding_up 
        src/main.cpp)

nanobind_add_module(speeding_up_nb
    src/main_nanobind.cpp)

add_executable(speeding_up_test
src/test_main.cpp
)

find_package(OpenMP)
if(OpenMP_CXX_FOUND)
    target_link_libraries(speeding_up PUBLIC OpenMP::OpenMP_CXX)
    target_link_libraries(speeding_up_test PUBLIC OpenMP::OpenMP_CXX)
    target_link_libraries(speeding_up_nb PUBLIC OpenMP::OpenMP_CXX)

endif()


# Set output directory for the compiled module for all build configurations
foreach(OUTPUTCONFIG ${CMAKE_CONFIGURATION_TYPES})
    string(TOUPPER ${OUTPUTCONFIG} OUTPUTCONFIG)
    set_target_properties(speeding_up PROPERTIES
        LIBRARY_OUTPUT_DIRECTORY_${OUTPUTCONFIG} "${CMAKE_CURRENT_SOURCE_DIR}/"
        RUNTIME_OUTPUT_DIRECTORY_${OUTPUTCONFIG} "${CMAKE_CURRENT_SOURCE_DIR}/"
        ARCHIVE_OUTPUT_DIRECTORY_${OUTPUTCONFIG} "${CMAKE_CURRENT_SOURCE_DIR}/"
    )

    set_target_properties(speeding_up_test PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY_${OUTPUTCONFIG} "${CMAKE_CURRENT_SOURCE_DIR}/"
    RUNTIME_OUTPUT_DIRECTORY_${OUTPUTCONFIG} "${CMAKE_CURRENT_SOURCE_DIR}/"
    ARCHIVE_OUTPUT_DIRECTORY_${OUTPUTCONFIG} "${CMAKE_CURRENT_SOURCE_DIR}/"
    )

    set_target_properties(speeding_up_nb PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY_${OUTPUTCONFIG} "${CMAKE_CURRENT_SOURCE_DIR}/"
    RUNTIME_OUTPUT_DIRECTORY_${OUTPUTCONFIG} "${CMAKE_CURRENT_SOURCE_DIR}/"
    ARCHIVE_OUTPUT_DIRECTORY_${OUTPUTCONFIG} "${CMAKE_CURRENT_SOURCE_DIR}/"
    )
endforeach(OUTPUTCONFIG CMAKE_CONFIGURATION_TYPES)