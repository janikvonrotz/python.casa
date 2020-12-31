#!/usr/bin/env python3
class Rectangle():
    # Konstruktor, initialisiert x und y mit Startposition
    def __init__(self, width, height):
        self.w = width
        self.h = height
    
    # Instanzmethoden
    def area(self):
        return self.w * self.h
        
    def perimeter(self):
        return 2 * (self.w + self.h)
    
# Anwendung
r1 = Rectangle(12, 7.4)
r2 = Rectangle(8, 5)
for r in [r1, r2]:
    print('Breite: ', r.w)
    print('Höhe:   ', r.h)	
    print('Fläche: ', r.area())
    print('Umfang: ', r.perimeter())
    print()
    
# andere Schreibweise zum Aufruf von Instanzmethoden, unüblich
print(Rectangle.area(r1))

