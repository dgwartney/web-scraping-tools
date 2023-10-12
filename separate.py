#!/usr/bin/env python3
import os
import shutil
import sys

# Function to create a new subdirectory and move files into it
def move_files(directory, files, count):
    dirname = f'{directory}/subdir_{count}'
    print(dirname)
    os.mkdir(dirname)
    for file in files:
        fpath = os.path.join(directory,file)
        print(fpath)
        shutil.move(fpath, dirname)

# Path to the directory containing the files
directory = sys.argv[1]

# List all the files in the directory
files = os.listdir(directory)

# Counter to keep track of current subdirectory count
count = 1

# Iterate over the files and move them into separate subdirectories
while len(files) > 0:
    # Select the next 10 files
    batch = files[:15]
    files = files[15:]
    
    # Move the batch of files into a new subdirectory
    move_files(directory, batch, count)
    count += 1

