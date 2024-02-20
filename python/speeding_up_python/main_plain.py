import cpp.speeding_up as spd
import numpy as np
import time
from numba import jit, njit, prange

# Number crunching plain:
N = 50_000_000
numbers = np.random.rand(N)

def plain_sum_py(numbers):
    total = 0
    for elem in numbers:
        total += elem
    return total

start = time.time()
result = plain_sum_py(numbers)
end = time.time()
print(f"Python result:\t{result}\t Time: {end-start}")

#--------------

def plain_sum_np(numbers):
    return numbers.sum()

start = time.time()
result = plain_sum_np(numbers)
end = time.time()
print(f"NumPy  result:\t{result}\t Time: {end-start}")

#--------------

@njit(fastmath = True)
def plain_sum_numba(numbers):
    total = 0
    for elem in numbers:
        total += elem
    return total


start = time.time()
result = plain_sum_numba(numbers)
end = time.time()
print(f"Numba  result:\t{result}\t Time: {end-start}, (with compilation)")
start = time.time()
result = plain_sum_numba(numbers)
end = time.time()
print(f"Numba  result:\t{result}\t Time: {end-start}, (w/o compilation)")


@njit(fastmath=True, parallel=True)
def plain_sum_numba_par(numbers):
    total = 0
    for i in prange(len(numbers)):
        total += numbers[i]
    return total

start = time.time()
result = plain_sum_numba_par(numbers)
end = time.time()
print(f"Numba  result:\t{result}\t Time: {end-start}, (with compilation, par)")
start = time.time()
result = plain_sum_numba_par(numbers)
end = time.time()
print(f"Numba  result:\t{result}\t Time: {end-start}, (w/o compilation, par)")

# ----
numbers_cpp = spd.vector_double(numbers)  

start = time.time()
result = spd.plain_sum_cpp(numbers_cpp)
end = time.time()
cpp1 = end-start
print(f"C++    result:\t{result}\t Time: {cpp1}")

start = time.time()
result = spd.plain_sum_cpp_par(numbers_cpp)
end = time.time()
cpp2 = end-start
print(f"C++    result:\t{result}\t Time: {cpp2}, (parallel)")

start = time.time()
result = spd.cpp_no_op(numbers_cpp)
end = time.time()
no_op_time = end-start
print(f"C++    result:\t{result}\t\t\t Time: {no_op_time}, (no-op)")
# print(f"C++    result:\t{result}\t Time: {cpp1 - no_op_time}, (no-op subtracted)")
# print(f"C++    result:\t{result}\t Time: {cpp2 - no_op_time}, (parallel, no-op subtracted)")




