#!/usr/bin/env python3
import numpy as np

# 3x3 Matrix mit lauter Nullen
a = np.zeros([3, 3])
print(a)
print(a.shape, a.dtype)

# 2x2 Matrix aus Liste erzeugen
lst = [[0.1, 0.2], [-0.3, 0.4]]
b = np.asarray(lst)
print(b)
print(b.shape, b.dtype)
print(b[0, 1])  # Ausgabe 0.2
print(b[1, 1])  # Ausgabe 0.4

# Matrix kopieren
c = b.copy()
c[1, 1] = 0.5
print(b)
print(c)

# 3x3 Matrix mit Zufallszahlen zwischen 0 und 1
print('-- Zufallszahlen --')
d = np.random.rand(3, 3)
print(d)
print(d.shape, d.dtype)

# Slicing
print('-- Slicing-Syntax --')
m = np.reshape(range(16), (4, 4))
print(m)
print(m[2, :])
print(m[: ,2])
print(m[1:3, 2:4])

# alle Elemente der 2. und 3. Zeile ändern
m[1:3, :] = 0
print(m)

# mit Matrizen rechnen
print('-- rechnen --')
m1 = np.asarray([[1.0, 2.0], [3.0, 2.5]])
m2 = np.asarray([[2.0, 0], [2.2, 4.0]])
print('Multiplikation / Addition mit Skalar')
print(m1 * 2)
print(m1 + 3)

print('Addition zweier Matrizen')
print(m1 + m2)

print('Elementweise Multiplikation zweier Matrizen')
print(m1 * m2)

print('Richtige Multplikation zweier Matrizen')
print(m1 @ m2)
print(np.dot(m1, m2))

print('Quadratwurzel')
print(np.sqrt(m1))

print('Maximum')
print(np.maximum(m1, m2))

print('Summe')
print(m1.sum())

print('Transponierte Matrix')
print(m1.T)

