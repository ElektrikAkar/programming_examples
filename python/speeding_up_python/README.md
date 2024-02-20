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

python/speeding_up_python/main_plain.py
Python result:  25000189.451614816       Time: 2.811161994934082
NumPy  result:  25000189.45161797        Time: 0.03600001335144043
Numba  result:  25000189.45161791        Time: 0.4365115165710449, (with compilation)
Numba  result:  25000189.45161791        Time: 0.02200031280517578, (w/o compilation)
C++    result:  25000189.451615952       Time: 1.2973244190216064
C++    result:  25000189.451617766       Time: 1.307081699371338, (parallel)

python/speeding_up_python/main_multi.py
Python result:  232163171.23635164       Time: 3.139641761779785
NumPy  result:  232163171.2363152        Time: 0.20402264595031738
Numba  result:  232163171.23631382       Time: 0.6302661895751953, (with compilation)
Numba  result:  232163171.23631382       Time: 0.12171316146850586, (w/o compilation)
C++    result:  232163171.23630416       Time: 0.32759976387023926
C++    result:  232163171.2363156        Time: 0.27073073387145996, (parallel)


python/speeding_up_python/main_complex.py
Python result:  241740875.3327055        Time: 4.0082175731658936
NumPy  result:  241740875.33273938       Time: 0.2650606632232666
Numba  result:  241740875.33270553       Time: 0.6792054176330566, (with compilation)
Numba  result:  241740875.33270553       Time: 0.13795161247253418, (w/o compilation)
C++    result:  241740875.3327055        Time: 0.4139556884765625
C++    result:  241740875.3327395        Time: 0.2879066467285156, (parallel)



Native C++ results: 

Plain sum:
C++    result: 2.49974e+07      Time: 0.0191504 (native)
C++    result: 2.49974e+07      Time: 0.007704 (native, par)


Multi sum:
C++    result: 2.32159e+08      Time: 0.0745408 (native)
C++    result: 2.32159e+08      Time: 0.0123312 (native, par)


Complex sum:
C++    result: 2.41743e+08      Time: 0.142452 (native)
C++    result: 2.41743e+08      Time: 0.0174707 (native, par)