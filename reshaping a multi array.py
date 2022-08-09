import numpy as np

x = np.arange(18).reshape(3,2,3)
print(x)
y = x[2,0:2,1:3]
print(y)
