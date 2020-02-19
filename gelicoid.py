import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = p3.Axes3D(fig)

fa = np.linspace(-2*np.pi, 2*np.pi, 100)
O = np.linspace(-2*np.pi, 2*np.pi, 100)
h = 1

x = np.outer(fa, np.cos(O))
y = np.outer(fa, np.sin(O))
z = np.outer(h, O)

ax.plot_surface(x,y,z,color = 'b')
plt.show()