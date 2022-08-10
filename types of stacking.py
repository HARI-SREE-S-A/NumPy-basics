# stacking
import numpy as np
x = np.arange(9).reshape(3,3)
y = np.arange(9,18).reshape(3,3)

z = np.hstack((x,y))
k = np.vstack((x,y))
l = np.dstack((x,y))

print(k)
print(z)
print(l)