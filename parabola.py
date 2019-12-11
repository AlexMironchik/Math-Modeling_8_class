import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
fig= plt.figure()
def circle_f(x_centre,y_centre, R, N):
    x=np.zeros(N)
    y=np.zeros(N)
    for i in range(N):
        alpha=np.linspace(0,2*np.pi,100)
        x[i]=x_centre+R*np.cos(alpha[i])
        y[i]=y_centre+R*np.sin(alpha[i])
    return x,y
x_centre_move = np.linspace(0, 10, 100)
a = 1
b = 1
c = 1
y_centre_move = a*x**2 + b*x + c
anim_list = []
N = 100
for i in range(0, N, 1):
    x,y = circle_f(x_centre_move[i], y_centre_move[i], R = 5, N = N)
    circle, = plt.plot(x,y, 'o-', lw = 2)
    anim_list.append([circle])
ani = ArtistAnimation(fig, anim_list, interval = 50)
plt.axis('equal')
ani.save('ani.gif')