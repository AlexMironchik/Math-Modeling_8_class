import numpy as np

def massiv(a):
    p = 1
    for i in range(0, len(a), 1):
        p = p*a[i]
    print(p)
        
a = np.arange(1, 5, 1)

massiv(a)