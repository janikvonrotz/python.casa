#!/usr/bin/env python3
class MyClass():
    def __init__(self, a, b):
        self.a = a
        self.b = b

obj = MyClass(3, 4)
# print(MyClass.a) # Fehler, MyClass hat kein Attribut 'a'
print(obj.a)       # Ausgabe 3

obj.c = 7
print(obj.c)       # Ausgabe 7

