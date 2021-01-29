import numpy as np

"""
This script evaluates the different parametric t-norms at the
point (1/2,1/2), as suggested by Detyniecki, Yager, and Bouchon-Meunier.

Yager, R.R., Detyniecki, M. and Bouchon-Meunier, B., 2000. Specifying t-norms based on the value of T (1/2, 1/2). Mathware & soft computing. 2000 Vol. 7 Núm. 1.

"""

sample = np.linspace(0,50,5000)
x = 1/2
y = 1/2

value = []

from parametric.tnorms import hamacher
for i in range(len(sample)):
    value.append(hamacher(x,y,sample[i]))

import matplotlib.pyplot as plt

plt.plot(sample, value, label='Hamacher')

value = []

from parametric.tnorms import frank
for i in range(len(sample)):
    value.append(frank(x,y,sample[i]))

plt.plot(sample, value, label='Frank')

value = []

from parametric.tnorms import yager
for i in range(len(sample)):
    value.append(yager(x,y,sample[i]))

plt.plot(sample, value, label='Yager')

value = []

from parametric.tnorms import aczel_alsina
for i in range(len(sample)):
    value.append(aczel_alsina(x,y,sample[i]))

plt.plot(sample, value, label='Aczel')

value = []

from parametric.tnorms import dombi
for i in range(len(sample)):
    value.append(dombi(x,y,sample[i]))

plt.plot(sample, value, label='Dombi')

value = []

from parametric.tnorms import sugeno_weber
for i in range(len(sample)):
    value.append(sugeno_weber(x,y,sample[i]))

plt.plot(sample, value, label='Sugeno')
plt.xlabel('p')
plt.ylabel('T(1/2,1/2)')
plt.legend(loc='best')
plt.show()
