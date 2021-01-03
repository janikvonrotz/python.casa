#!/usr/bin/env python3
def shrink(s, n):
    if not isinstance(s, str):
        raise TypeError('s muss eine Zeichenkette sein.')
    if not isinstance(n, int):
        raise TypeError('n muss eine ganze Zahl sein.')
    if n < 0:
        raise ValueError('n muss größer 0 sein.')
        
    if n >= len(s):  
        return s
    elif n < 15:
        return s[:n]
    else:        
      return s[:n-10] + ' ... ' + s[-5:]
  
print(shrink('abcdefghijklmnopqrstuvwxyz', 8))
print(shrink('abcdefghijklmnopqrstuvwxyz', 17))
print(shrink('abcdefghijklmnopqrstuvwxyz', 22))
