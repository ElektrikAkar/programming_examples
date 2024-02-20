#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>


#include "spd.hpp"

PYBIND11_MODULE(speeding_up, m)
{
  m.doc() = "pybind11 example benchmark"; // module docstring

  m.def("plain_sum_cpp", &plain_sum_cpp, "A function that sums N random numbers");
  m.def("multi_operation_cpp", &multi_operation_cpp, "A function that performs multi operations on N random numbers");
  m.def("complex_operation_cpp", &complex_operation_cpp, "A function that performs conditional operations on N random numbers");

  // Parallel versions:
  m.def("plain_sum_cpp_par", &plain_sum_cpp_par, "A function that sums N random numbers (parallel)");
  m.def("multi_operation_cpp_par", &multi_operation_cpp_par, "A function that performs multi operations on N random numbers (parallel)");
  m.def("complex_operation_cpp_par", &complex_operation_cpp_par, "A function that performs conditional operations on N random numbers (parallel)");

  m.def("cpp_no_op", &cpp_no_op, "A function that does nothing");
}