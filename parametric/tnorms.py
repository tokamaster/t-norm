import math
import numpy as np

def frank(x,y,p):
    if p == 0:
        return min(x,y)
    if p == 1:
        return x*y
    if p == math.inf:
        return max(0,x+y-1)
    else:
        a = 1 + ((p**x-1)*(p**y-1)/(p-1))
        return math.log(a,p)

def hamacher(x,y,p):
    if x == 0 and y == 0 and p == 0:
        return 0
    if p == math.inf:
        if x == 1 and y == 1:
            return x
        if x == 1 and y != 1:
            return y
        if x != 1 and y == 1:
            return x
        if x != 1 and y !=1:
            return 0
    else:
        return (x*y)/(p+(1-p)*(x+y-x*y))

def schweizer_sklar(x,y,p):
    if p == -math.inf:
        return min(x,y)
    if p > -math.inf and p < 0:
        return (x**p+y**p-1)**(1/p)
    if p == 0:
        return x*y
    if p > 0 and p < math.inf:
        return (max(0,x**p+y**p-1))**(1/p)
    if p == math.inf:
        if x == 1 and y != 1:
            return y
        if x != 1 and y == 1:
            return x
        if x != 1 and y !=1:
            return 0

def yager(x,y,p):
    if p == 0:
        if x == 1 and y == 1:
            return x
        if x == 1 and y != 1:
            return y
        if x != 1 and y == 1:
            return x
        if x != 1 and y !=1:
            return 0
    if p > 0 and p < math.inf:
        return max(0,1-((1-x)**p+(1-y)**p)**(1/p))
    if p == math.inf:
        return min(x,y)

def aczel_alsina(x,y,p):
    if p == 0:
        if x == 1 and y == 1:
            return x
        if x == 1 and y != 1:
            return y
        if x != 1 and y == 1:
            return x
        if x != 1 and y !=1:
            return 0
    if p > 0 and p < math.inf:
        return np.exp(-(np.abs(np.log(x))**p+np.abs(np.log(y))**p)**(1/p))
    if p == math.inf:
        return min(x,y)

def dombi(x,y,p):
    #issues for x,y=0.25, p=646
    if x == 0 or y == 0:
        return 0
    if p == 0:
        if x == 1 and y == 1:
            return x
        if x == 1 and y != 1:
            return y
        if x != 1 and y == 1:
            return x
        if x != 1 and y !=1:
            return 0
    if p == math.inf:
        return min(x,y)
    else:
        A = np.power(1/x-1, p, dtype=np.longdouble)
        B = np.power(1/y-1, p, dtype=np.longdouble)
        denom = (1+(A+B)**(1/p))
        return 1/denom

def sugeno_weber(x,y,p):
    if p == -1:
        if x == 1 and y == 1:
            return x
        if x == 1 and y != 1:
            return y
        if x != 1 and y == 1:
            return x
        if x != 1 and y !=1:
            return 0
    if p > -1 and p < math.inf:
        return max(0,(x+y-1+p*x*y)/(1+p))
    if p == math.inf:
        return x*y
