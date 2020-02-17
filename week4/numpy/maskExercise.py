
# Class exercise: masking
# ) For the dataset: data = np.arange(1,101).reshape(10,10)
# 1. apply a mask that will return only the even numbers
# 2. using np.where() return only numbers that ends with 6
# 3. using the operators: % and | mask to only get numbers that are divisible by 3 and numbers begining with 8

import numpy as np

data = np.arange(1, 101).reshape(10, 10)

# 1. Return only even numbers, using mask.
mask = (data % 2 == 0)
even = data[mask]
print(even)

# 2. Use np.where() to return numbers that end with 6
mask = (data % 10 == 6)
ends = np.where(mask, data, None)
print(ends)

# 3 numbers divisible by 3 and end in 8
mask = ((data % 3 == 0) & (data % 10 == 8))
divisible = data[mask]
print(divisible)
