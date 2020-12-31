#!/usr/bin/env python3
import math

def verschachteln(f, g, x):
    return f(g(x))
  
# Anwendung
verschachteln(print, math.sin, 0.2) # 0.19866933079506122
print(math.sin(0.2))                # 0.19866933079506122
  
ergebnis = verschachteln(math.sin, math.sqrt, 0.5)
print(ergebnis == math.sin(math.sqrt(0.5)))  # True
  