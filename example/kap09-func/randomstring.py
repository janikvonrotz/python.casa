#!/usr/bin/env python3
from random import randint

def randomstr(n):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    max = len(letters)
    lst = [letters[randint(0, max-1)] for _ in range(n)]
    return ''.join(lst)
    
print(randomstr(4))
print(randomstr(8))
print(randomstr(100))


    
# Alternative
from string import ascii_lowercase
from random import choices

def randomstr2(n):
    return ''.join(choices(ascii_lowercase, k=n))
    
    
print(randomstr2(4))
print(randomstr2(8))
print(randomstr2(100))
