x0 = 1
y0 = 2
v0x = 3
v0y = 4
from Constant import g
import numpy as np
t = np.arange(0, 5, 0.01)
A = np.ndarray(shape =(500, 3))
for i in range(0, 500, 1):
    x = x0+v0x*t[i]
    y= y0+v0y*t[i]-g*t[i]**2/2
    A[i,0] = t[i]
    A[i,1] = x
    A[i,2] = y
print (A)