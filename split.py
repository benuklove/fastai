# before running split.py, make sure:
# 1. no unwanted files in image dataset (erroneous, corrupted, etc)
# 2. equal number of images in each folder

import os, shutil


origin = "data/testing/"
moveto = "data/donetesting/"

if not os.path.exists(origin):
    os.makedirs(origin)
if not os.path.exists(moveto):
    os.makedirs(moveto)

files = os.listdir(origin)
files.sort()
for f in files:
    src = origin+f
    dst = moveto+f
    shutil.move(src,dst)
