#!/usr/bin/env python3
from scipy.interpolate import interp1d
import numpy as np
import tkinter
import matplotlib.pyplot as plt
x = np.linspace(1.0, 10.0, 10)
y = np.random.rand(10) * 5
f = interp1d(x, y, kind='cubic')
xvalues = np.linspace(1.0, 10.0, 1000)
plt.plot(x, y, 'o', xvalues, f(xvalues), '-')
plt.savefig('interpolate.png', dpi=200)
