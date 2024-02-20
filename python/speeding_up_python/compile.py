import subprocess
import os
import pathlib
import sys

dir_path = pathlib.Path(__file__).parent.resolve()
s_path = os.path.join(dir_path, "cpp")
b_path = os.path.join(s_path, "build")

python_executable = sys.executable

print(python_executable)

# os.environ["CXX"] = "C:/Program Files/LLVM/bin/clang++.exe"
# os.environ["CC"] = "C:/Program Files/LLVM/bin/clang.exe"

subprocess.run(
    ["cmake", "-DPYTHON_EXECUTABLE=" + python_executable, "-S", s_path, "-B", b_path, 
    #  "-DCMAKE_C_COMPILER=" + os.environ["CC"],
    #  "-DCMAKE_CXX_COMPILER=" + os.environ["CXX"],
    # "-G", "Ninja"
    ],
    check=True,
)

subprocess.run(
    [
        "cmake",
        "--build",
        b_path,
        "-j8",
        "--config",
        "Release",
        # "--target",
        # "speeding_up",
    ],
    check=True,
)
