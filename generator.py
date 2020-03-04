import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

def generator(r,N,v):
    for i in range(0,N,1):
        alpha = 2*np.pi/N
        x = np.sin(alpha*i)*r
        y = np.cos(alpha*i)*r
        if x<0 and y<0:
            vx = v*np.sin(0.5*np.pi-alpha*i)
            vy = -v*np.cos(0.5*np.pi-alpha*i)
        elif x<0 and y>0:
            vx = v*np.cos(alpha*i)
            vy = -v*np.sin(alpha*i)
        else:
            vx = 0
            vy = 0
        plt.arrow(x,y,vx,vy)
        plt.scatter(x,y)
        plt.plot(x,y,marker='o')
    plt.axis('equal')
    plt.show()

generator(10,100,10)