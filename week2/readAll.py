# create a function that can read all files in folder
# and all subfolders and print a list of all png files
# including their full path name

import os

from pathlib import Path

# Getting the current work directory (cwd)
thisdir = os.getcwd()

# r=root, d=directories, f = files
for r, d, f in os.walk(thisdir):
    for file in f:
        if ".png" in file:
            print(os.path.join(r, file))
