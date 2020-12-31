#!/usr/bin/env python3
import math

def funcbuilder(f, n):
  def newfunc(x): 
      return f(n*x)  # Ergebnis von newfunc
  return newfunc     # Ergebnis von funcbuilder

# bildet die Funktion sin(2*x)
f1 = funcbuilder(math.sin, 2)
print(f1(0.4), math.sin(0.4*2))
# Ausgabe 0.7173560908995228 0.7173560908995228

# bildet die Funktion cos(4*x)
f2 = funcbuilder(math.cos, 4)
print(f2(0.07), math.cos(0.07*4))
# Ausgabe 0.9610554383107709 0.9610554383107709
