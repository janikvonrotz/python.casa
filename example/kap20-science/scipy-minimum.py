#!/usr/bin/env python3
from scipy import optimize
import numpy as np
import tkinter
import matplotlib.pyplot as plt
f = lambda x: x/8 + 2/x
result = optimize.minimize(f, 1.0)
x = np.linspace(0.2, 10, 1000)
plt.plot(x, f(x), '-', result.x, result.fun, 'o')
plt.savefig('minimum.png', dpi=200)
