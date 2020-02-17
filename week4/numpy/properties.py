import numpy as np

a = np.arange(10, 70, dtype=np.int8).reshape((4, 3, 5))

print('type: ', type(a))
print('dtype', a.dtype)
print('size', a.size)
print('shape', a.shape)
print('itemsize: ', a.itemsize)
print('ndim: ', a.ndim)
print('nbytes: ', a.nbytes)
