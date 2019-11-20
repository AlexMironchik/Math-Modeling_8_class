import numpy as np
import matplotlib.pyplot as plt
t=np.arange(1,14,0.1)
R=15
x=R*(t-np.sin(t))
y=R*(1-np.cos(t))
plt.plot(x,y,label='Ditch')
plt.axis('equal')
plt.show()
