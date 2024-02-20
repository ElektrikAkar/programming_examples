import cpp.speeding_up as spd
import numpy as np
import time
from numba import jit, njit, vectorize

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


# ----
start = time.time()
result = spd.plain_sum_cpp(numbers)
end = time.time()
print(f"C++    result:\t{result}\t Time: {end-start}")

start = time.time()
result = spd.plain_sum_cpp_par(numbers)
end = time.time()
print(f"C++    result:\t{result}\t Time: {end-start}, (parallel)")