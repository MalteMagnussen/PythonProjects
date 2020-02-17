import numpy as np

a = np.array([[10, 11, 12, 13, 14],
              [15, 16, 17, 18, 19],
              [20, 21, 22, 23, 24],
              [25, 26, 27, 28, 29]])

yellow = a[0, 0]

print(yellow)

red = a[0, 1:4]

print(red)

purple = a[::2, 4]

print(purple)

green = a[0:3, 2]

print(green)

lightblue = a[0:4, 1::2]

print(lightblue)

blue = a[::2, 4]

print(blue)
