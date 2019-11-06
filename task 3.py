from constant_module import g
def energy(m, v, h):
    E = (m*v**2)+(m*g*h)
    print(E)
energy(10, 5, 200)