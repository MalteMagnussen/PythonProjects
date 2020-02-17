import numpy as np

a = np.arange(11, 36).reshape(5, 5)
# explanation: comma separates the arrays and colon does the positional selection
# 2dArray[rows, columns]
# double colon: get every n^th value e.g. ::2 menas print every second value and 2::3 means get every third value starting from third pos.
# get one-dim. subarray of row 0, start:1 (pos=2) end:4 (not included, pos=4)
red = a[0, 1:4]
blue = a[1:4, 0]  # get one-dim. subarrays (index 1,2,3) of column 0
# get a two-dim. subarray of every second element by row and column
green = a[::2, ::2]
purple = a[:, 1]    # get the second column

print('red:', red, '\nblue:', blue, '\ngreen:\n', green, '\npurple:', purple)
