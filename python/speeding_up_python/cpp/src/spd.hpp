/**
 * @file spd.hpp
 * @brief File for holding C++ functions for number crunching
 *
 * @date 20 Feb 2024
 * @author Volkan Kumtepeli
 */

#pragma once

#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <omp.h>

double plain_sum_cpp(std::vector<double> const &numbers)
{
  return std::reduce(numbers.cbegin(), numbers.cend());
}

template <typename T>
constexpr inline auto sqr(T x) { return x * x; }

double multi_operation_cpp(std::vector<double> const &numbers)
{

  auto ops = [](double elem) {
    constexpr double a = 2.34;
    return 10 * std::log(std::sin(sqr(a * elem)) + 10);
  };

  return std::transform_reduce(numbers.cbegin(), numbers.cend(), 0.0, std::plus{}, ops);
}


double complex_operation_cpp(std::vector<double> const &numbers)
{
  const auto N = numbers.size();
  double total = 0.0;
  for (size_t i = 0; i < N; ++i) {
    const double a = numbers[i] < 0.5 ? 2.34 : 1.44;
    auto value = std::sin(sqr(a * numbers[i]));

    if (i % 7 == 0)
      value += 5;

    total += 10 * std::log(value + 10);
  }

  return total;
}

// ---- parallel versions -------

double plain_sum_cpp_par(std::vector<double> const &numbers)
{
  const int N = numbers.size();
  double total = 0.0;
#pragma omp parallel for reduction(+ : total)
  for (int i = 0; i < N; ++i)
    total += numbers[i];

  return total;
}


double multi_operation_cpp_par(std::vector<double> const &numbers)
{
  auto ops = [](double elem) {
    constexpr double a = 2.34;
    return 10 * std::log(std::sin(sqr(a * elem)) + 10);
  };

  const int N = numbers.size();
  double total = 0.0;

#pragma omp parallel for reduction(+ : total)
  for (int i = 0; i < N; ++i)
    total += ops(numbers[i]);

  return total;
}


double complex_operation_cpp_par(std::vector<double> const &numbers)
{
  const int N = numbers.size();
  double total = 0.0;

#pragma omp parallel for reduction(+ : total)
  for (int i = 0; i < N; ++i) {
    const double a = numbers[i] < 0.5 ? 2.34 : 1.44;
    auto value = std::sin(sqr(a * numbers[i]));

    if (i % 7 == 0)
      value += 5;

    total += 10 * std::log(value + 10);
  }

  return total;
}