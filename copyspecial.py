import sys
import re
import os
import shutil
import subprocess
import os
import shutil
import sys

def get_special_paths(dir):
    special_files = []
    # Walk through all directories and files
    for dirpath, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            if '__' in filename:  # Match files with __ in their names
                special_files.append(os.path.abspath(os.path.join(dirpath, filename)))
    print(f"Special files found: {special_files}")  # Debugging line to show identified files
    return special_files
import sys
import os
import shutil
import zipfile
import subprocess

def get_special_paths(dir):
    special_files = []
    pattern = re.compile(r'__\w+__')
    for dirpath, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            if pattern.search(filename):
                special_files.append(os.path.abspath(os.path.join(dirpath, filename)))
    return special_files

def copy_to(paths, dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    for path in paths:
        dest = os.path.join(dir, os.path.basename(path))
        if os.path.abspath(path) != os.path.abspath(dest):  # Avoid copying the same file
            try:
                shutil.copy(path, dest)
                print(f"Successfully copied {path} to {dest}")
            except Exception as e:
                print(f"Error copying {path}: {e}")
        else:
            print(f"Error copying {path}: '{path}' and '{dest}' are the same file")

def zip_to(paths, zippath):
    print(f"Zipping files: {paths}")
    command = ['zip', '-j', zippath] + paths
    print(f"Command to execute: {' '.join(command)}")
    result = subprocess.run(command, capture_output=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr.decode()}")
    else:
        print(f"Successfully created zip file: {zippath}")

def main():
    if len(sys.argv) < 2:
        print("Usage: [--todir dir] [--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    todir = None
    tozip = None
    dirs = []

    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == '--todir':
            todir = sys.argv[i+1]
            i += 2
        elif sys.argv[i] == '--tozip':
            tozip = sys.argv[i+1]
            i += 2
        else:
            dirs.append(sys.argv[i])
            i += 1

    # Gather special files from directories
    all_special_files = []
    for dir in dirs:
        special_files = get_special_paths(dir)
        print(f"Special files found: {special_files}")
        all_special_files.extend(special_files)

    if todir:
        copy_to(all_special_files, todir)
    elif tozip:
        zip_to(all_special_files, tozip)
    else:
        for file in all_special_files:
            print(file)

if __name__ == '__main__':
    main()
