import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0, 100, 1)
def diff_func(v, t):
    dvdt = (F - y*v**2) / m
    return dvdt
v_0 = 0
y = 0.01
m = 1
F = 0.1
solve = odeint(diff_func, v_0, t)
plt.plot(t, solve[:, 0])
plt.show()