"""import matplotlib.pyplot as plt;
from random import randint;

x = [];
y = [];
for _ in range(1, 30000):
    y += [randint(0, 100)];
    x += [randint(0, 100)];

plt.plot(x,y, 'ro');
plt.show();"""

import itertools


modes = ['metro', 'train', 'bus']
n = len(modes)

for model in ['time_expanded', 'condensed', 'alpha_beta']:
    for i in range(n + 1):
        parts = list(itertools.combinations(modes, i))
        for p in parts:
            string = '-'.join(p)
            print("'" + model + ('-' if string != '' else '') + string + ".txt',")
               
            