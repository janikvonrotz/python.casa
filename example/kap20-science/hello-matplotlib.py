#!/usr/bin/env python3
import math
import numpy as np
import tkinter  # (nur unter Linux erforderlich)
import matplotlib.pyplot as plt
x  = np.linspace(0, 2 * np.pi, 1000)
y1 = np.sin(x)
plt.plot(x, y1)
plt.savefig('sinus.png')
plt.savefig('sinus-highres.png', dpi=200)
plt.savefig('sinus.eps')
plt.savefig('sinus.jpg')

y2 = np.cos(x)
plt.plot(x, y2)
plt.savefig('sinus-cosinus-1.png', dpi=200)

# neues Diagram, Sinus als durchgezogene Linie,
# Cosinus strichliert
plt.figure()
plt.plot(x, y1, '-', x, y2, '--')
plt.savefig('sinus-cosinus-2.png', dpi=200)

# eigene Funktion zeichnen
plt.figure()
f  = lambda x: math.sin(x) * math.exp(-0.1 * x)
vf = np.vectorize(f)
x  = np.linspace(0, 25, 1000)
y  = vf(x)
plt.plot(x, y)
plt.savefig('sinus-exp.png', dpi=200)

# Diagramm beschriften (nochmals die Funktion von oben)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set(xlabel='x', ylabel='f(x)', title='Gedämpfte Schwingung')
ax.grid()
fig.savefig('sinus-exp-grid.png', dpi=200)


# zweiteiliges Diagramm
x = np.linspace(0, 2 * np.pi, 1000)
y1 = np.sin(x)
y2 = np.cos(x)
plt.figure()          # neues Diagramm starten
plt.subplot(2, 1, 1)  # 2 Zeilen, 1 Spalte, Position 1
plt.plot(x, y1)       # erster Plot an dieser Position
plt.subplot(2, 1, 2)  # wie bisher, Position 2
plt.plot(x, y2)       # zweiter Plot an dieser Position
plt.savefig('plot-in-array.png', dpi=200)