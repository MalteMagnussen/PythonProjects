a = np.arange(0, 27).reshape((3, 3, 3))  # = (z, y, x)
#print('whole cube: \n',a, '\n---------------')

print('1st row (x-values): \n', a[0, 0, :], '\n---------')
print('1st collumn (y-values, where x==0): \n', a[0, :, 0], '\n---------')
print('1st depth (z-values, where y==0 and x==0): \n',
      a[:, 0, 0], '\n---------')
print('value of first side, second slice, third piece:\n',
      a[0, 1, 2], '\n-------------')  # equal to a[0][1][2] = 5
# equivivalent to a[:,2,:] all z, y=2, all x.
print('values of all x*z where y=2\n', a[:, 2], '\n----------')
print('all z and y values where x = 2: \n', a[:, :, 2], '\n--------')  #
# all z (skip each second) and all y (skip each second) etc.
print('skip each second z,y,x: \n', a[::2, ::2, ::2])
