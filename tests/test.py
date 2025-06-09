# Import some additional packages
import os, subprocess

# Settings
# Directories
SRC_DIR = "test/src"
SRC_FILE = "main.c"
BUILD_DIR = "test/Build"

# Timeouts
COMPILE_TIMEOUT = 10.0
RUN_TIMEOUT = 10.0

# Create the absolute paths
src_path = os.path.join(SRC_DIR, SRC_FILE)
bin_path = os.path.join(BUILD_DIR, "bin")

# Compile the project
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
