#!/usr/bin/env python3

# Read-only-Rectangle

class Rectangle():
    # Konstruktor, initialisiert x und y mit Startposition
    def __init__(self, width, height):
        self.__w = width
        self.__h = height

    @property
    def w(self):
        return self.__w
    @property
    def h(self):
        return self.__h
    
    # Instanzmethoden
    def area(self):
        return self.__w * self.__h
        
    def perimeter(self):
        return 2 * (self.__w + self.__h)
        
    # Gleichheit
    def __eq__(self, other):
        return (self.__w, self.__h) == (other.__w, other.__h)
    
    # Hash-Funktion
    def __hash__(self):
        return hash((self.__w, self.__h))
        
r1 = Rectangle(1, 2)
r2 = Rectangle(1, 2)
print(r1 == r2) # True        


