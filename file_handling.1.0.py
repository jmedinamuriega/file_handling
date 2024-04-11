# Task 1: Directory Inspector:

# Problem Statement:
# Create a Python script that lists all files and subdirectories in a given directory. 
# Your script should prompt the user for the directory path and then display the contents.

# Code Example:
ask="Please enter the directory path: "
error="The path does not exist. Please enter a valid directory path."

import os

def list_directory_contents():
    path = input(ask)
    if os.path.exists(path):
        print("\nContents of the directory:")
        for content in os.listdir(path):
                print(content)
    else:
        print(error)

list_directory_contents()

        
# Expected Outcome:
# The script should correctly list all files and subdirectories in the specified directory. 
# Handle exceptions for invalid paths or inaccessible directories.
# Task 2: File Size Reporter:

# Problem Statement:
# Write a Python program that reports the sizes of all files in a specific directory. The program should ask the user for a directory path and then print each file's name and size within that directory.

# Code Example:
def report_file_sizes():
    directory = input(ask)
    if os.path.exists(directory):
        print("\nFile sizes in the directory:")
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                print(f"{filename}: {os.path.getsize(filepath)} bytes")
    else:
        print(error)

report_file_sizes()

# Expected Outcome:
# Your program should display the name and size (in bytes) of each file in the given directory. Ensure that the program only reports on files, not directories, and handles any errors gracefully.
# Task 3: File Extension Counter:

# Problem Statement:
# Develop a Python script that counts the number of files of each extension type in a directory. For instance, in a directory with five '.txt' files and three '.py' files, the script should report "TXT: 5" and "PY: 3".

# Code Example:
import os
from collections import Counter

def count_file_extensions():
    directory = input(ask)
    if os.path.exists(directory):
        ext_counter = Counter()

        for filename in os.listdir(directory):
            ext = os.path.splitext(filename)[1][1:].upper()
            if ext:
                ext_counter[ext] += 1
        for ext, count in ext_counter.items():
            print(f"{ext}: {count}")
    else:
        print(error)

count_file_extensions()
# Expected Outcome:
# The script should accurately count and display the number of files for each extension type in the specified directory. Handle different cases of file extensions (e.g., '.TXT' and '.txt' should be considered the same).