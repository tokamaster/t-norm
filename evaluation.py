"""
This script evaluates the different parametric t-norms at the
point (1/2,1/2), as suggested by Detyniecki, Yager, and Bouchon-Meunier.

Yager, R.R., Detyniecki, M. and Bouchon-Meunier, B., 2000. Specifying t-norms based on the value of T (1/2, 1/2). Mathware & soft computing. 2000 Vol. 7 Núm. 1.

"""
import numpy as np
import matplotlib.pyplot as plt
from parametric.tnorms import *

def evaluate(x, y, samples, tnorm):
    value = []
    for sample in samples:
        value.append(tnorm(x, y, sample))
    plt.plot(samples, value, label=tnorm.__name__)

samples = np.linspace(0,50,5000)
x = 1/2
y = 1/2

evaluate(x, y, samples, hamacher)
evaluate(x, y, samples, frank)
evaluate(x, y, samples, yager)
evaluate(x, y, samples, aczel_alsina)
evaluate(x, y, samples, dombi)
evaluate(x, y, samples, sugeno_weber)

plt.xlabel('p')
plt.ylabel('T(1/2,1/2)')
plt.legend(loc='best')
plt.show()
