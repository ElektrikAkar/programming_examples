import cpp.speeding_up as spd
import numpy as np
import time
from numba import jit, njit, vectorize
from math import sin, log

# Number crunching plain:
N = 10_000_000
numbers = np.random.rand(N)

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

#--------------

def multi_operation_np(numbers):
    a = 2.34
    return np.sum(10 * np.log(np.sin(np.square(a*numbers)) + 10))

start = time.time()
result = multi_operation_np(numbers)
end = time.time()
print(f"NumPy  result:\t{result}\t Time: {end-start}")

#--------------

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

# ----
start = time.time()
result = spd.multi_operation_cpp(numbers)
end = time.time()
print(f"C++    result:\t{result}\t Time: {end-start}")

start = time.time()
result = spd.multi_operation_cpp_par(numbers)
end = time.time()
print(f"C++    result:\t{result}\t Time: {end-start}, (parallel)")