#!/usr/bin/env python3

# Datenklasse (data classes), erfordert Python 3.7
from dataclasses import dataclass

@dataclass()
class Rectangle():
    w: float  # Type Annotation ist für @dataclass()
    h: float  # erforderlich,

    # Instanzmethoden
    def area(self):
        return self.w * self.h
        
    def perimeter(self):
        return 2 * (self.w + self.h)
    
# Anwendung
r1 = Rectangle(12, 7.4)
r2 = Rectangle(8, 5)
print(r1 == r2)               # False
print(r2 == Rectangle(8, 5))  # True
print(r1)                     # Ausgabe Rectangle(w=12, h=7.4)
r1.w = 13                     # erlaubt