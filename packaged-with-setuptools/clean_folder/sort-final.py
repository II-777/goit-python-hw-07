from datetime import datetime
from pathlib import Path
import argparse
import shutil
import re

TARGET_DIR = ''  # Global variable assigned during initial checks

def initial_checks() -> None:
    '''Entry point of the program. Contains pre-execution checks for validity of the input.'''
    global TARGET_DIR  # Declare TARGET_DIR as a global variable
    parser = argparse.ArgumentParser(description='Sort files in a directory.')
    parser.add_argument('TARGET_DIR', type=str, help='Target directory to sort')
    args = parser.parse_args()

    target_dir = args.TARGET_DIR
    if not Path(target_dir).exists():
        print(f'[-] Error. TARGET_DIR does not exist: "{target_dir}"')
        exit(1)

    TARGET_DIR = target_dir  # Assign the value to the global variable

def main():
    initial_checks()
    print("Global variable TARGET_DIR:", TARGET_DIR)

if __name__ == '__main__':
    main()


