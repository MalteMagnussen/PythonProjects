# use one np array as indices for another
a = np.arange(0, 100, 10)
indices = np.array([1, 5, -1])
print(indices)
print(a)
print(a[indices])
