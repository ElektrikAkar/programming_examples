import subprocess
import os
import pathlib
import sys

dir_path = pathlib.Path(__file__).parent.resolve()
s_path = os.path.join(dir_path, "cpp")
b_path = os.path.join(s_path, "build")

python_executable = sys.executable

print(python_executable)

subprocess.run(
    ["cmake", "-DPYTHON_EXECUTABLE=" + python_executable, "-S", s_path, "-B", b_path],
    check=True,
)

subprocess.run(
    [
        "cmake",
        "--build",
        b_path,
        "-j4",
        "--config",
        "Release",
        "--target",
        "speeding_up",
    ],
    check=True,
)
