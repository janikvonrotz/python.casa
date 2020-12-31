#!/usr/bin/env python3

import inspect

class A():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def m1(self):
        return self.x + self.y
        
    def m2(self):
        return self.x * self.y
        
class B(A):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def m2(self):
        return super().m2() * self.z
      
    def m3(self):
        return self.x + self.y * self.z
      
a = A(1, 2)
print(a.x, a.y)       # Ausgabe 1 2
print(a.m1(), a.m2()) # Ausgabe 3 2

b = B(1, 2, 3)
print(b.x, b.y, b.z)  # Ausgabe 1 2 3
print(b.m1(), b.m2(), b.m3())  # Ausgabe 6 6 7

print('isinstance-Funktion')
print(isinstance(a, A))      
print(isinstance(a, B))      
print(isinstance(b, A))      
print(isinstance(b, B))     
print(inspect.getmro(B)) 
