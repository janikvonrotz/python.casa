#!/usr/bin/env python3
import sys
import threading

threading.stack_size(64 * 1024 * 1024) # 64 MiB
sys.setrecursionlimit(10000)

def f(n):
    return 1 + f(n)
    
f(2)  # RecursionError: maximum recursion depth exceeded
    