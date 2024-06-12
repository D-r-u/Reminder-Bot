import sys
from cx_Freeze import setup, Executable

# Define the build options
build_exe_options = {
    "packages": [],
    "excludes": [],
    "include_files": []
}

# Base option for creating a windowed application
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# Define the executable
executables = [
    Executable(
        script="Rembo.py",
        base=base,
        icon="icon.ico"
    )
]

# Setup configuration
setup(
    name="MyApplication",
    version="1.0",
    description="My GUI application!",
    options={"build_exe": build_exe_options},
    executables=executables
)
