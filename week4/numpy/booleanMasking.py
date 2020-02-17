import numpy as np
# X=Having 50 values between 0-2*pi, Y=sinus values to x
import matplotlib.pyplot as plt

xs = np.linspace(0, 2 * np.pi, 50)
ys = np.sin(xs)
#print(xs,'\n',ys, '\n',len(ys))
plt.plot(xs, ys)
plt.show()

mask = ys >= 0                        # condition for the blue crosses
# rendering the blue plots only with filtered values
plt.plot(xs[mask], ys[mask], 'bx')
mask = (ys < 0)                       # condition for the green dots
# condition applied to xs and ys data sets
plt.plot(xs[mask], ys[mask], 'go')
plt.show()
