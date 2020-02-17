import numpy as np


# # np.ones()
# a = np.ones((3, 3))
# print(a, '\n-------------')
# a[1] = 2  # asign value to multiple cells
# a[2] = 3
# b = np.arange(9).reshape(3, 3)

# print(a)
# print(b)


a = np.ones((3, 3), dtype=int)
a[1] = 2
a[2] = 3
b = np.arange(9).reshape(3, 3)

print('a: \n', a)
print('b: \n', b)

print('a+b: \n', a + b)  # sum values on each index
print('a - b', a - b)
print('a * b', a*b)
print('b / a', b/a)
print('a ** 2', a**2)
print('a < b', a < b)
print('a > b', a > b)

array_a = np.array([1, 2, 3])
array_b = np.array([1, 2, 3])

print(
    'adding all the products a[0,0]*b[0,0]+a[1,0]*b[1,0]...\n', np.dot(array_a, array_b))

print(
    'adding all the products a[0,0]*b[0,0]+a[1,0]*b[1,0]...\n', array_a.dot(array_b))

print(a)

print(a[1:4, :] == a[1:4])
print(a[1:4].sum())
print(a.cumsum())  # cumulated sum
print(a.min())
print(a.max())
