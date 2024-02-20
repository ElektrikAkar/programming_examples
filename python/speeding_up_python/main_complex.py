import cpp.speeding_up as spd
import numpy as np
import time
from numba import jit, njit, vectorize
from math import sin, log

N = 10_000_000
numbers = np.random.rand(N)

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

#--------------

def complex_operation_np(numbers):
    a = np.where(numbers < 0.5, 2.34, 1.44)
    values = np.sin(np.square(a * numbers))
    values[np.arange(N) % 7 == 0] += 5
    return np.sum(10 * np.log(values + 10))

start = time.time()
result = complex_operation_np(numbers)
end = time.time()
print(f"NumPy  result:\t{result}\t Time: {end-start}")

#--------------

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

# ----
start = time.time()
result = spd.complex_operation_cpp(numbers)
end = time.time()
print(f"C++    result:\t{result}\t Time: {end-start}")

start = time.time()
result = spd.complex_operation_cpp_par(numbers)
end = time.time()
print(f"C++    result:\t{result}\t Time: {end-start}, (parallel)")