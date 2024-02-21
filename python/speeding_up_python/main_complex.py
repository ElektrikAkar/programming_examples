import cpp.speeding_up as spd
import cpp.speeding_up_nb as spd_nb
import numpy as np
import time
from numba import jit, njit, prange
from math import sin, log

N = 10_000_000
numbers = np.random.rand(N)
numbers_cpp = spd.vector_double(numbers)  
numbers_cpp_nb = spd_nb.vector_double(numbers)  


def complex_operation_py(numbers):
    total = 0
    for i in range(numbers.size):
        value = numbers[i]
        a = 2.34 if value < 0.5 else 1.44
        value = sin((a * value)**2)
        if i % 7 == 0:
            value += 5    

        total += 10 * log(value + 10)
    return total

start = time.time()
result = complex_operation_py(numbers)
end = time.time()
print(f"Python result:\t{result}\t Time: {end-start}")

#%%

def complex_operation_np(numbers):
    a = np.where(numbers < 0.5, 2.34, 1.44)
    values = np.sin(np.square(a * numbers))
    values[np.arange(N) % 7 == 0] += 5
    return np.sum(10 * np.log(values + 10))

start = time.time()
result = complex_operation_np(numbers)
end = time.time()
print(f"NumPy  result:\t{result}\t Time: {end-start}")

#%%

@njit(fastmath = True)
def complex_operation_numba(numbers):
    total = 0
    for i in range(numbers.size):
        value = numbers[i]
        a = 2.34 if value < 0.5 else 1.44
        value = sin((a * value)**2)
        if i % 7 == 0:
            value += 5    

        total += 10 * log(value + 10)
    return total


start = time.time()
result = complex_operation_numba(numbers)
end = time.time()
print(f"Numba  result:\t{result}\t Time: {end-start}, (with compilation)")
start = time.time()
result = complex_operation_numba(numbers)
end = time.time()
print(f"Numba  result:\t{result}\t Time: {end-start}, (w/o compilation)")

#%%
@njit(fastmath = True, parallel=True)
def complex_operation_numba_par(numbers):
    total = 0
    for i in prange(numbers.size):
        value = numbers[i]
        a = 2.34 if value < 0.5 else 1.44
        value = sin((a * value)**2)
        if i % 7 == 0:
            value += 5    

        total += 10 * log(value + 10)
    return total

start = time.time()
result = complex_operation_numba_par(numbers)
end = time.time()
print(f"Numba  result:\t{result}\t Time: {end-start}, (with compilation)")
start = time.time()
result = complex_operation_numba_par(numbers)
end = time.time()
print(f"Numba  result:\t{result}\t Time: {end-start}, (w/o compilation)")

#%%
start = time.time()
result = spd.complex_operation_cpp(numbers_cpp)
end = time.time()
cpp1 = end-start
print(f"C++    result:\t{result}\t Time: {cpp1}")

start = time.time()
result = spd.complex_operation_cpp_par(numbers_cpp)
end = time.time()
cpp2 = end-start
print(f"C++    result:\t{result}\t Time: {cpp2}, (parallel)")

#%%
start = time.time()
result = spd_nb.complex_operation_cpp(numbers_cpp_nb)
end = time.time()
cpp1 = end-start
print(f"C++    result:\t{result}\t Time: {cpp1} (nanobind)")

start = time.time()
result = spd_nb.complex_operation_cpp_par(numbers_cpp_nb)
end = time.time()
cpp2 = end-start
print(f"C++    result:\t{result}\t Time: {cpp2}, (nanobind, parallel)")