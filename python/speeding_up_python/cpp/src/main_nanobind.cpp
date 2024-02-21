#include <nanobind/nanobind.h>
#include <nanobind/stl/vector.h>
#include <nanobind/stl/bind_vector.h>

#include "spd.hpp"

#include <vector>

NB_MAKE_OPAQUE(std::vector<double>);
namespace nb = nanobind;

NB_MODULE(speeding_up_nb, m)
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
  nb::bind_vector<std::vector<double>>(m, "vector_double");
}