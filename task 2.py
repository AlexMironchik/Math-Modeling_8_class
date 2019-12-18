import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0,10,0.1)
def money_f(n,t):
    dndt = n*-k*t
    return dndt
k = 0.08
m_0=10
solve = odeint(money_f,m_0,t)
plt.plot(t,solve[:,0])
plt.show()