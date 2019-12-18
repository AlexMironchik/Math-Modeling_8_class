import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0, 5,0.1)
def bactery_f(n,t):
    dmdt = n*k
    return dmdt
k=0.5
m_0=10
solve = odeint(bactery_f, m_0,t)
plt.plot(t,solve[:,0])
plt.show