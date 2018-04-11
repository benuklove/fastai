"""Split files for classification

Assumes one folder - "downloads" contains folders with each classification
derived from https://github.com/hardikvasa/google-images-download.git

What this does:


Before running split.py, make sure:
1. no unwanted files in image dataset (erroneous, corrupted, etc)
2. recommended equal number of images in each folder
"""


import os, shutil

train_percent = .6
valid_percent = .2
test_percent = .2
num_classes = 2

def main():
    move_files()

def create_dirs():
    downloads = "data/downloads/"
    classes = os.listdir(downloads)
    print(list(enumerate(os.listdir(downloads))))

    traindir = downloads + "train/"
    validdir = downloads + "valid/"
    testdir = downloads + "test/"

    if not os.path.exists(traindir):
        os.makedirs(traindir)
        for c in classes:
            tmp_class = traindir + c + '/'
            if not os.path.exists(tmp_class):
                os.makedirs(tmp_class)
    if not os.path.exists(validdir):
        os.makedirs(validdir)
        for c in classes:
            tmp_class = validdir + c + '/'
            if not os.path.exists(tmp_class):
                os.makedirs(tmp_class)
    if not os.path.exists(testdir):
        os.makedirs(testdir)

def move_files():
    create_dirs()


origin = "data/testing/"
moveto = "data/donetesting/"

# if not os.path.exists(origin):
#     os.makedirs(origin)
# if not os.path.exists(moveto):
#     os.makedirs(moveto)

# files = os.listdir(origin)
# print(files)
# files.sort()
# print(files)
# for f in files:
#     print(f)
#     src = origin+f
#     dst = moveto+f
    # shutil.move(src,dst)

if __name__ == "__main__":
    main()
