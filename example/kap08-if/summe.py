#!/usr/bin/env python3
from functools import reduce
sum = 0
for i in range(1, 1001):
  sum += i
print('Summe der Zahlen von 1 bis 1000:', sum)

sum = 0
i = 1
while i<=1000:
  sum += i
  i += 1
print('Das gleiche Ergebnis, diesmal in einer while-Schleife errechnet:', sum)  


sum = reduce(lambda x, y: x + y, list(range(1, 1001)))
print(sum)
