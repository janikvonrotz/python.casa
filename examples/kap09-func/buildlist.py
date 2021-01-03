#!/usr/bin/env python3
import math

def buildlist(n, start, end, fn):
    if n<=1:
      return []  # leeres Ergebnis
    delta = (end - start) / (n-1)
    return [ fn(start + i*delta) for i in range(n)]
  
# Anwendung
lst1 = buildlist(5, 0.0, 4.0, math.sqrt)
print(lst1)

lst2 = buildlist(11, 0.0, 2.0, lambda x: x)
print(lst2)