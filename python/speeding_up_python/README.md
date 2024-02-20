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

| File                                | Language | Result             | Time (s) | Remarks            |
|-------------------------------------|----------|--------------------|----------|--------------------|
| main_plain.py                       | Python   | 25000189.45161482  | 2.811162 |                    |
|                                     | NumPy    | 25000189.45161797  | 0.036000 |                    |
|                                     | Numba    | 25000189.45161791  | 0.436512 | (with compilation) |
|                                     | Numba    | 25000189.45161791  | 0.022000 | (w/o compilation)  |
|                                     | C++      | 25000189.45161595  | 1.297324 |                    |
|                                     | C++      | 25000189.45161777  | 1.307082 | (parallel)         |
| main_multi.py                       | Python   | 232163171.2363516  | 3.139642 |                    |
|                                     | NumPy    | 232163171.2363152  | 0.204023 |                    |
|                                     | Numba    | 232163171.2363138  | 0.630266 | (with compilation) |
|                                     | Numba    | 232163171.2363138  | 0.121713 | (w/o compilation)  |
|                                     | C++      | 232163171.2363042  | 0.327600 |                    |
|                                     | C++      | 232163171.2363156  | 0.270731 |   (parallel)       |
| main_complex.py                     | Python   | 241740875.3327055  | 4.008218 |                    |
|                                     | NumPy    | 241740875.3327394  | 0.265061 |                    |
|                                     | Numba    | 241740875.3327055  | 0.679205 | (with compilation) |
|                                     | Numba    | 241740875.3327055  | 0.137952 | (w/o compilation)  |
|                                     | C++      | 241740875.3327055  | 0.413956 |                    |
|                                     | C++      | 241740875.3327395  | 0.287907 | (parallel)         |
| Native C++ (Plain sum)              | C++      | 2.49974e+07        | 0.019150 |                    |
|                                     | C++      | 2.49974e+07        | 0.007704 | (parallel)         |
| Native C++ (Multi sum)              | C++      | 2.32159e+08        | 0.074541 |                    |
|                                     | C++      | 2.32159e+08        | 0.012331 | (parallel)         |
| Native C++ (Complex sum)            | C++      | 2.41743e+08        | 0.142452 |                    |
|                                     | C++      | 2.41743e+08        | 0.017471 | (parallel)         |
 