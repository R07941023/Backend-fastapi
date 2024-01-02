import sys, os
sys.path.append(os.getcwd())
import subprocess
from glob import glob

def run_tests():
    test_files = glob("./src/main/python/unittest/test_*.py", recursive=True)
    if not test_files:
        print("No test files found.")
        return

    command = f"pytest {' '.join(test_files)}"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    run_tests()