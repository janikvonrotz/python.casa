#!/usr/bin/env python3
# herkömmliche Funktion, liefert die ersten n
# Fibonacci-Zahlen
def fiblst(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result += [a]
        a, b = b, a+b
    return result

print(fiblst(10))     
# Ausgabe [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Generator-Funktion
def fibgen(n):
    cnt = 0
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b
        cnt += 1
        if cnt > n:
            return

print(fibgen(10))
# Ausgabe <generator object fibgen at 0x109569af0>

print(list(fibgen(10)))
# Ausgabe [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Fibonacci-Zahlen < 1000 ausgeben
gen = fibgen(100)
fib = next(gen)
while fib<1000:
    print(fib)
    fib = next(gen)

# nochmals, aber Generator zu klein
gen = fibgen(10)
fib = next(gen)
while fib<1000:
    print(fib)
    fib = next(gen, None)
    if fib == None: 
        print('Generator erschöpft')
        break


