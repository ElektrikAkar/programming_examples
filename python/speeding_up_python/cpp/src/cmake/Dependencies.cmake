# This cmake file is to add external dependency projects.
# Adapted from https://github.com/cpp-best-practices/cmake_tecomplate/tree/main
include(src/cmake/CPM.cmake)

CPMAddPackage(
  NAME pybind11
  URL "https://github.com/pybind/pybind11/archive/refs/tags/v2.11.1.tar.gz"
)