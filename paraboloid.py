import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = p3.Axes3D(fig)

fa = np.arange(0.01, 4*np.pi, 0.01)
O = np.arange(0, 2*np.pi, 0.01)

x = np.outer(fa, np.cos(O))
y = np.outer(fa, np.sin(O))
z = np.outer(fa**2, np.ones(np.size(O)))

ax.plot_surface(x,y,z,color = 'b')
plt.show()