import numpy as np

a = np.arange(0, 27).reshape((3, 3, 3))  # = (z, y, x)
#print('whole cube: \n',a, '\n---------------')


# Class exercise: cube
# 1. Slice out [12 13 14] from the above cube using only one slice. e.g: a[:,:,:]
# 2. Slice out [3 12 21].
# 3. Slice out all y-values where x is 2 and z is 0.

one = a[1, 1, 0:3]
print(one)

two = a[0:3, 1, 0]
print(two)

three = a[0, :, 2]
print(three)
