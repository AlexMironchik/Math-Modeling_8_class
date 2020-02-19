import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = p3.Axes3D(fig)

fa = np.linspace(-2*np.pi, 2*np.pi, 100)
O = np.linspace(-2*np.pi, 2*np.pi, 100)
n = 1
l = 2
m = 3

x = fa*np.outer(np.cos(O), np.ones(np.size(O))) + l*np.outer(O, np.ones(np.size(O)))
y = fa*np.outer(np.sin(O), np.ones(np.size(O))) + m*np.outer(O, np.ones(np.size(O)))
z = n*np.outer(O, np.ones(np.size(O)))

ax.plot_surface(x,y,z,color = 'b')
plt.show()