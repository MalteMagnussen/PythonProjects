import numpy as np

a = np.arange(0, 100, 10)
b = a[:5]                       # when first index is 0 we can omit it.
c = a[a >= 50]                  # mask provided to filter all values below 50
d = a[(a % 20 == 0) & (a != 40)]  # more complex conditinal mask
# mask condition like ternary operator
e = np.where((a % 20 == 0) & (a != 40), a, None)
print('a:\n', a, '\nb:\n', b, '\n:c\n', c, '\nd:\n', d, '\ne:\n', e)
