/**
 * @file test_main.cpp
 * @brief Source file for testing benchmark functions in C++
 *
 * @date 20 Feb 2024
 * @author Volkan Kumtepeli
 */


#include "spd.hpp"

#include <vector>
#include <iostream>
#include <random>
#include <chrono>
#include <numeric>

std::vector<double> generate_random_numbers(int n)
{
  std::vector<double> numbers;
  numbers.reserve(n);

  std::random_device rd;
  std::mt19937 gen(rd());
  std::uniform_real_distribution<> dis(0.0, 1.0);

  for (int i = 0; i < n; ++i)
    numbers.push_back(dis(gen));

  return numbers;
}


int main()
{
  std::cout << "Plain sum:\n";
  {
    constexpr int N = 50'000'000;
    auto numbers = generate_random_numbers(N);

    auto start = std::chrono::high_resolution_clock::now();
    auto sum = plain_sum_cpp(numbers);
    auto end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> elapsed = end - start;
    std::cout << "C++    result: " << sum
              << "\tTime: " << elapsed.count() << " (native)\n";


    start = std::chrono::high_resolution_clock::now();
    sum = plain_sum_cpp_par(numbers);
    end = std::chrono::high_resolution_clock::now();

    elapsed = end - start;
    std::cout << "C++    result: " << sum
              << "\tTime: " << elapsed.count() << " (native, par)\n";
  }


  std::cout << "\n\nMulti sum:\n";
  {
    constexpr int N = 10'000'000;
    auto numbers = generate_random_numbers(N);

    auto start = std::chrono::high_resolution_clock::now();
    auto sum = multi_operation_cpp(numbers);
    auto end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> elapsed = end - start;
    std::cout << "C++    result: " << sum
              << "\tTime: " << elapsed.count() << " (native)\n";


    start = std::chrono::high_resolution_clock::now();
    sum = multi_operation_cpp_par(numbers);
    end = std::chrono::high_resolution_clock::now();

    elapsed = end - start;
    std::cout << "C++    result: " << sum
              << "\tTime: " << elapsed.count() << " (native, par)\n";
  }

  std::cout << "\n\nComplex sum:\n";
  {
    constexpr int N = 10'000'000;
    auto numbers = generate_random_numbers(N);

    auto start = std::chrono::high_resolution_clock::now();
    auto sum = complex_operation_cpp(numbers);
    auto end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> elapsed = end - start;
    std::cout << "C++    result: " << sum
              << "\tTime: " << elapsed.count() << " (native)\n";


    start = std::chrono::high_resolution_clock::now();
    sum = complex_operation_cpp_par(numbers);
    end = std::chrono::high_resolution_clock::now();

    elapsed = end - start;
    std::cout << "C++    result: " << sum
              << "\tTime: " << elapsed.count() << " (native, par)\n";
  }

  return EXIT_SUCCESS;
}