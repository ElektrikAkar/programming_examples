import cpp.speeding_up as spd
import cpp.speeding_up_nb as spd_nb
import numpy as np
import time
from numba import jit, njit, prange
from math import sin, log

# Number crunching plain:
N = 10_000_000
numbers = np.random.rand(N)
numbers_cpp = spd.vector_double(numbers)  
numbers_cpp_nb = spd_nb.vector_double(numbers)  

def multi_operation_py(numbers):
    total = 0
    a = 2.34
    for elem in numbers:
        total += 10 * log(sin((a*elem)**2) + 10)
    return total

start = time.time()
result = multi_operation_py(numbers)
end = time.time()
print(f"Python result:\t{result}\t Time: {end-start}")

#%%

def multi_operation_np(numbers):
    a = 2.34
    return np.sum(10 * np.log(np.sin(np.square(a*numbers)) + 10))

start = time.time()
result = multi_operation_np(numbers)
end = time.time()
print(f"NumPy  result:\t{result}\t Time: {end-start}")

#%%

@njit(fastmath = True)
def multi_operation_numba(numbers):
    total = 0
    a = 2.34
    for elem in numbers:
        total += 10 * log(sin((a*elem)**2) + 10)
    return total


start = time.time()
result = multi_operation_numba(numbers)
end = time.time()
print(f"Numba  result:\t{result}\t Time: {end-start}, (with compilation)")
start = time.time()
result = multi_operation_numba(numbers)
end = time.time()
print(f"Numba  result:\t{result}\t Time: {end-start}, (w/o compilation)")

#%%

@njit(fastmath=True, parallel=True)
def multi_operation_numba_par(numbers):
    total = 0
    a = 2.34
    for i in prange(len(numbers)):
        total += 10 * log(sin((a*numbers[i])**2) + 10)
    return total

start = time.time()
result = multi_operation_numba_par(numbers)
end = time.time()
print(f"Numba  result:\t{result}\t Time: {end-start}, (with compilation, par)")
start = time.time()
result = multi_operation_numba_par(numbers)
end = time.time()
print(f"Numba  result:\t{result}\t Time: {end-start}, (w/o compilation, par)")


#%%
start = time.time()
result = spd.multi_operation_cpp(numbers_cpp)
end = time.time()
cpp1 = end-start
print(f"C++    result:\t{result}\t Time: {cpp1}")

start = time.time()
result = spd.multi_operation_cpp_par(numbers_cpp)
end = time.time()
cpp2 = end-start
print(f"C++    result:\t{result}\t Time: {cpp2}, (parallel)")

#%%
start = time.time()
result = spd_nb.multi_operation_cpp(numbers_cpp_nb)
end = time.time()
cpp1 = end-start
print(f"C++    result:\t{result}\t Time: {cpp1}, (nanobind)")

start = time.time()
result = spd_nb.multi_operation_cpp_par(numbers_cpp_nb)
end = time.time()
cpp2 = end-start
print(f"C++    result:\t{result}\t Time: {cpp2}, (nanobind, parallel)")


# %%
