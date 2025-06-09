# Import some additional packages
import sys, os, subprocess

# Settings
# Directories
SRC_DIR = "src"
SRC_FILE = "main.c"
BUILD_DIR = "Build"

# Timeouts
COMPILE_TIMEOUT = 10.0
RUN_TIMEOUT = 10.0

# Create the absolute paths
cwd_path = os.getcwd()
src_path = os.path.join(cwd_path, SRC_DIR, SRC_FILE)
bin_path = os.path.join(cwd_path, BUILD_DIR, "bin")
build_dir = os.path.join(cwd_path, BUILD_DIR)
print("src_path:", src_path)
print("bin_path:", bin_path)
print("build_dir:", build_dir)

# Compile the project
print("Create build directory")
try:
	ret = subprocess.run(["mkdir", build_dir],
					  stdout = subprocess.PIPE,
					  timeout = RUN_TIMEOUT)
except Exception as e:
	print("ERROR: Could not crate the build directory.", str(e))
	exit(1)

# Parse output
output = ret.stdout.decode('utf-8')
print(output)

print("Building...")
try:
	ret = subprocess.run(["gcc", src_path, "-o", bin_path],
					  stdout = subprocess.PIPE,
					  stderr = subprocess.PIPE,
					  timeout = COMPILE_TIMEOUT)
except Exception as e:
	print("ERROR: Compilation failed.", str(e))
	exit(1)

# Parse output
output = ret.stdout.decode('utf-8')
print(output)
output = ret.stderr.decode('utf-8')
print(output)

# Check the successful compiled state
if ret.returncode != 0:
	print("Compilation failed.")
	exit(1)
print("Compilation succeed.")

# Try to run the compiled binary
print("Running...")
try:
	ret = subprocess.run([bin_path],
					  stdout = subprocess.PIPE,
					  timeout = RUN_TIMEOUT)
except Exception as e:
	print("ERROR: Runtime failed.", str(e))
	exit(1)

# Parse output
output = ret.stdout.decode('utf-8')
print(output)

# Test succeed
print("Compilation succeed.")
exit(0)
