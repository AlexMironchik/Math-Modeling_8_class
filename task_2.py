from Constant import g
from Constant import M
from Constant import R
from math import pi,sqrt
h = 100
v = sqrt((g*h*pi)/(2*M*R))
print (v)
T = 200
epsilon = 300
k = 1.38*10**(-23)
from math import e
h = 6.63*10**(-34)
N = (2/(sqrt(pi))*(h/((k*T)**(3/2)))*((e)**((-e)/(k*T)))*(epsilon)**(T/2))
print (N)