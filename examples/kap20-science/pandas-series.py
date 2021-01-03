#!/usr/bin/env python3
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

s = Series( [7, 12, 13, 9, np.nan, 20] )
print(s)
print(s[2:4])

# eigener Index
s.index = ['a', 'b', 'c', 'd', 'e', 'f']
print(s['c'], s[2])

# Auswahl von Elementen
print(s[s>10])

# Berechnungen
print(s.sum())
print(s.mean())