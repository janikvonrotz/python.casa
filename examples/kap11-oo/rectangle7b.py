#!/usr/bin/env python3

# Datenklasse (data classes), erfordert Python 3.7

from dataclasses import dataclass

@dataclass(frozen=True)
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
set = {r1, r2} # erlaubt, weil Hash-Funktion vorhanden ist
# r1.w = 13  # Fehler