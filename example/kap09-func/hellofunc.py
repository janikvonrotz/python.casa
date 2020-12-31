#!/usr/bin/env python3
# Funktion ohne Ergebnis
def f1(x, y):
    print('Parameter 1:', x)
    print('Parameter 2:', y)
    
# Funktion mit Ergebnis
def f2(x, y):
    return x+y
    
# hier beginnt die Programmausführung
f1(2, 3)      # gibt die Parameter aus
# Ausgabe: Parameter 1: 2
#          Parameter 2: 3

n = f2(4, 5)
print(n)      
# Ausgabe: 9