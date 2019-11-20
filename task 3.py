import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
fig, ax=plt.subplots()
anim_object, = plt.plot([],[], 'o')
xdata,ydata = [], []
ax.set_xlim(-5, 15)
ax.set_ylim(-5, 5)
R=1
def update(t):
    xdata.append(R * (t - np.sin(t)))
    ydata.append(R * (1 - np.cos(t)))
    anim_object.set_data(xdata, ydata)

ani = FuncAnimation(fig, 
                    update,
                    frames=np.arange(0,4*np.pi,0.1),
                    interval=10)

ani.save('anfvi.gif')