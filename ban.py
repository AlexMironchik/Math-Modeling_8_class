import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
t = np.arange(0,18,0.05)
def mayatnik(z,t):
    s,v = z
    ds_dt = v
    dv_dt = -9.8*np.sin(s/l)-k/m*v
    return ds_dt,dv_dt
l = 6
m = 8
k = 3
s0 = 3
v0 = 1
z0 = s0,v0
sol = odeint(mayatnik,z0,t)
plt.plot(sol[:,1],sol[:,0])
plt.show()