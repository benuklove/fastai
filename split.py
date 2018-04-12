"""Split files for classification

Assumes:
    1. one directory "downloads" contains folders with each classification
    derived from https://github.com/hardikvasa/google-images-download.git
    2. downloads is in the directory "data"

This file runs three functions: create_dirs, move_files, and cleanup.
    - 'create_dirs' creates appropriate directories: train and valid - each
    with their own directories for each class, and a test directory.
    - 'move_files' moves all files from original directories to new ones as
    determined by split percentages.
    - 'cleanup' renames "downloads" to the concatenation of all class names.

Before running split.py, make sure:
    1. no unwanted files in image dataset (erroneous, corrupted, etc)
    2. recommended equal number of images in each folder

"""

import os, shutil, random


# Set desired values:
train_percent = .6
valid_percent = .2
test_percent = .2

# New locations
downloads = "data/downloads/"
traindir = downloads + "train/"
validdir = downloads + "valid/"
testdir = downloads + "test/"
classes = os.listdir(downloads)


def main():
    create_dirs()
    move_files()
    cleanup()

def create_dirs():
    """Create the new directories: train, valid, test,
    along with class subdirectories in train and valid."""

    if not os.path.exists(traindir):
        os.makedirs(traindir)

    if not os.path.exists(validdir):
        os.makedirs(validdir)
        for c in classes:
            tmp_class = validdir + c + '/'
            if not os.path.exists(tmp_class):
                os.makedirs(tmp_class)

    if not os.path.exists(testdir):
        os.makedirs(testdir)

def move_files():
    """Move the files into the appropriate directories."""

    if train_percent + valid_percent + test_percent == 1.0:

        for c in classes:   # ie, classes = ['cats', 'dogs']

            path = downloads + c
            filenames = os.listdir(path)
            for file in filenames:
                os.rename(os.path.join(path, file),
                          os.path.join(path, file.replace(' ', '')))

            src = os.listdir(path)
            count = len(src)
            num_test_files = round(count * test_percent)
            num_valid_files = round(count * valid_percent)

            for _ in range(num_test_files):
                new_src = os.listdir(path)
                choice = random.choice(new_src)
                file = path + '/' + choice
                dst = testdir + choice
                shutil.move(file, dst)

            for _ in range(num_valid_files):
                new_src = os.listdir(path)
                choice = random.choice(new_src)
                file = path + '/' + choice
                dst = validdir + c + '/' + choice
                shutil.move(file, dst)

            remaining = path
            dest = traindir + c
            shutil.move(remaining, dest)

    else:
        print("Splits don't add up to 1.")

def cleanup():
    new_name = 'data/' + ''.join(classes)
    os.rename(downloads, new_name.replace(' ', ''))


if __name__ == "__main__":
    main()
