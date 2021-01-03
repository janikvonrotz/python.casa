#!/usr/bin/env python3
import traceback
def f2(x):
    return 2/(x-1)

def f1(x):
    ergebnis = f2(x) + 7
    return ergebnis
  
try:
    n=f1(1)
    print(n)
except ZeroDivisionError as e:
    print(traceback.print_exc())
