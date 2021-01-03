#!/usr/bin/env python3
def f(n):
    if n<=1:
        return 1
    else:
        return n * f(n-1)
        
result = f(5)
print(result)  # 120
