import numpy as np

"""
This script is a test.
"""

def corrcheck(a,b):
    lower = (max(a+b-1,0)-a*b)/np.sqrt(a*b*(1-a)*(1-b))
    upper = (min(a,b)-a*b)/np.sqrt(a*b*(1-a)*(1-b))
    return lower, upper

def funct(x,y,p):
    lower, upper = corrcheck(x,y)
    if p <= lower:
        return max(x+y-1,0)
    if p >= upper:
        return min(x,y)
    else:
        return x*y+p*np.sqrt(x*y*(1-x)*(1-y))

values = []

X = np.linspace(0.1,0.99,100)
Y = np.linspace(0.1,0.99,100)

for i in range(len(X)):
    for k in range(len(Y)):
        values.append(funct(X[i],Y[k],-0.31))

values = np.array(values)
print(values)
print(len(values))

values = values.reshape((len(X), len(Y)))
print(np.shape(values))
print(values)

print(funct(0.1,0.99,-0.31))
print(corrcheck(0.1,0.99))
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig, ax = plt.subplots()
CS = ax.contour(X, Y, values)
ax.clabel(CS)
plt.show()
