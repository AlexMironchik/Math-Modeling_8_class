import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = p3.Axes3D(fig)

fa = np.linspace(-2*np.pi, 2*np.pi, 100)
O = np.linspace(-2*np.pi, 2*np.pi, 100)
a = 1
b =2
c = 3

x = a*np.outer(np.sinh(O), np.cos(fa))
y = b*np.outer(np.sinh(O), np.sin(fa))
z = c*np.outer(np.sinh(O), np.ones(np.size(fa)))

ax.plot_surface(x,y,z,color = 'b')
plt.show()