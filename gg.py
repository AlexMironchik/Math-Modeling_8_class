import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
t = np.arange(0,18,0.05)
def difurka(z,t):
    y,K = z
    dy_dt = K
    dK = -np.sin(y)*K-3*y*t-5
    return dy_dt,dK
y0 = 0.01
K0 = 0.05
x0 = y0,K0
sol = odeint(difurka,x0,t)
plt.plot(sol[:,1],sol[:,0])
plt.show()
    