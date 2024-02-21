import cpp.speeding_up as spd
import cpp.speeding_up_nb as spd_nb
import numpy as np
import time
from numba import jit, njit, prange

import jax.numpy as jnp
import jax

# Number crunching plain:
N = 50_000_000
numbers = np.random.rand(N)
numbers_cpp = spd.vector_double(numbers)  
numbers_cpp_nb = spd_nb.vector_double(numbers)  
numbers_jax = jnp.array(numbers)

def plain_sum_py(numbers):
    total = 0
    for elem in numbers:
        total += elem
    return total

start = time.time()
result = plain_sum_py(numbers)
end = time.time()
print(f"Python result:\t{result}\t Time: {end-start}")

#%%

def plain_sum_np(numbers):
    return numbers.sum()

start = time.time()
result = plain_sum_np(numbers)
end = time.time()
print(f"NumPy  result:\t{result}\t Time: {end-start}")

#%%

plain_sum_jax = jax.jit(plain_sum_np)
result = plain_sum_jax(numbers_jax)
start = time.time()
result = plain_sum_jax(numbers_jax)
end = time.time()
print(f"Jax    result:\t{result}\t\t Time: {end-start}")

#%%

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

#%%

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

#%%
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

#%%
# Nanobind version
start = time.time()
result = spd_nb.plain_sum_cpp(numbers_cpp_nb)
end = time.time()
cpp1 = end-start
print(f"C++    result:\t{result}\t Time: {cpp1}, (nanobind)")

start = time.time()
result = spd_nb.plain_sum_cpp_par(numbers_cpp_nb)
end = time.time()
cpp2 = end-start
print(f"C++    result:\t{result}\t Time: {cpp2}, (nanobind, parallel)")

