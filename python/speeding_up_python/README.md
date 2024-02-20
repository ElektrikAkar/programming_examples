# Speeding up Python
Some benchmark files for Numba vs Numpy vs Python vs C++ etc. 
Date: 2024/02/20

# Usage: 

- Run `compile.py`
- Run `main_*.py` (relevant files)
- Run `cpp/speeding_up_test.exe`


```bash
cmake -S ./cpp -B ./cpp/build && cmake --build ./cpp/build
```

```bash
conda install -c conda-forge pybind11
```

# Some results:
- Device: Intel i7-12800H 2.40 GHz

| File                                | Language | Result             | Time (s) | Gain   | Remarks            |
|-------------------------------------|----------|--------------------|----------|--------|--------------------|
| main_plain.py                       | Python   | 25000189.45161482  | 2.811162 | 364.90 |                    |
|                                     | NumPy    | 25000189.45161797  | 0.036000 | 4.67   |                    |
|                                     | Numba    | 25000189.45161791  | 0.436512 | 56.66  | (with compilation) |
|                                     | Numba    | 25000189.45161791  | 0.022000 | 2.86   | (w/o compilation)  |
|                                     | C++      | 25000189.45161595  | 1.297324 | 168.40 |                    |
|                                     | C++      | 25000189.45161777  | 1.307082 | 169.66 | (parallel)         |
| main_multi.py                       | Python   | 232163171.2363516  | 3.139642 | 254.61 |                    |
|                                     | NumPy    | 232163171.2363152  | 0.204023 | 16.55  |                    |
|                                     | Numba    | 232163171.2363138  | 0.630266 | 51.11  | (with compilation) |
|                                     | Numba    | 232163171.2363138  | 0.121713 | 9.87   | (w/o compilation)  |
|                                     | C++      | 232163171.2363042  | 0.327600 | 26.57  |                    |
|                                     | C++      | 232163171.2363156  | 0.270731 | 21.96  |   (parallel)       |
| main_complex.py                     | Python   | 241740875.3327055  | 4.008218 | 229.42 |                    |
|                                     | NumPy    | 241740875.3327394  | 0.265061 | 15.17  |                    |
|                                     | Numba    | 241740875.3327055  | 0.679205 | 38.88  | (with compilation) |
|                                     | Numba    | 241740875.3327055  | 0.137952 | 7.90   | (w/o compilation)  |
|                                     | C++      | 241740875.3327055  | 0.413956 | 23.69  |                    |
|                                     | C++      | 241740875.3327395  | 0.287907 | 16.48  | (parallel)         |
| Native C++ (Plain sum)              | C++      | 2.49974e+07        | 0.019150 | 2.49   |                    |
|                                     | C++      | 2.49974e+07        | 0.007704 | 1.00   | (parallel)         |
| Native C++ (Multi sum)              | C++      | 2.32159e+08        | 0.074541 | 6.05   |                    |
|                                     | C++      | 2.32159e+08        | 0.012331 | 1.00   | (parallel)         |
| Native C++ (Complex sum)            | C++      | 2.41743e+08        | 0.142452 | 8.15   |                    |
|                                     | C++      | 2.41743e+08        | 0.017471 | 1.00   | (parallel)         |
 