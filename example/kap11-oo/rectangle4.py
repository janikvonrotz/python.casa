#!/usr/bin/env python3
class Rectangle():
    # Konstruktor, initialisiert x und y mit Startposition
    def __init__(self, width, height):
        if width<=0 or height<=0:
            raise ValueError('Ungültige Parameter!')
        self.__w = width
        self.__h = height
    
    # Getter und Setter für Länge
    @property
    def w(self):
        return self.__w

    @w.setter
    def w(self, width):
        if width>0:
            self.__w = width
        else:
            raise ValueError('Die Länge muss >0 sein.')

    # Getter und Setter für Höhe
    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, height):
        if height>0:
            self.__h = height
        else:
            raise ValueError('Die Höhe muss >0 sein.')

    # Instanzmethoden
    def area(self):
        return self.__w * self.__h
        
    def perimeter(self):
        return 2 * (self.__w + self.__h)


    
# Anwendung
r = Rectangle(12, 7.4)
print(r.w)  # 12, führt @property w() aus
r.w = 25    # führt @w.setter w() aus

# r2 = Rectangle(-7, 5)  # löst einen Fehler aus
# r.w = -11              # löst ebenfalls einen Fehler aus
    

