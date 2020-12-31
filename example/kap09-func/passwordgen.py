#!/usr/bin/env python3
from random import randint
from random import shuffle
# Achtung: choices erfordert Python >= 3.6!
from random import choices

import string

def passwordgen(n):
    if n<8:
        n=8
    lower =  string.ascii_lowercase
    upper =  string.ascii_uppercase
    digits = string.digits
    other =  '.,;:-_!$%&()='
    pwlst = choices(lower, k=n-3)
    # für Python 3.5, wenn choices nicht zur Verfügung steht:
    # pwlst = \
    # [ lower[randint(0, len(lower)-1)] for _ in range(n-3) ]
    pwlst += [upper[randint(0, len(upper)-1)]]
    pwlst += [digits[randint(0, len(digits)-1)]]
    pwlst += [other[randint(0, len(other)-1)]] 
    shuffle(pwlst)
    return ''.join(pwlst)

for _ in range(3):    
    print(passwordgen(10))
