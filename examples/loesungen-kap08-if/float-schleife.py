#!/usr/bin/env python3
nmax = 11
min = 125.0
max = 160.0
delta = (max - min) / (nmax - 1)

for i in range(0, nmax):
  x = min + delta * i
  print(x)
