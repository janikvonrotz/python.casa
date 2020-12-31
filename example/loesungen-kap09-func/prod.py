#!/usr/bin/env python3
from functools import reduce
import operator

def prod(*f):
    result = f[0]
    for factor in f[1:]:
      result = result * factor
    return result


# Variante mit reduce und Lambda
def prod1(*f):
    if len(f)<2:
        return f[0]
    else:
        return reduce(lambda x, y: x*y, f)

# Variante mit reduce und operator.mul
def prod2(*f):
    if len(f)<2:
        return f[0]
    else:
        return reduce(operator.mul, f)
    
# Test
print(prod(1), prod1(1), prod2(1))
print(prod(1, 2, 3), prod1(1, 2, 3), prod2(1, 2, 3))
print(prod(7, 10, 2, 5), prod1(7, 10, 2, 5), prod2(7, 10, 2, 5))
