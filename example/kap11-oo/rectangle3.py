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

    # interner Methoden-Aufruf
    def ap(self):
        return { 'area': self.area(), 
                 'perimeter': self.perimeter() }
    
    # statische Methoden
    @staticmethod
    def sarea(width, height):
        return width * height

    @staticmethod
    def sperimeter(width, height):
        return 2 * (width + height)
        
    @staticmethod
    def createquad(length):
        return Rectangle(length, length)
        
    @staticmethod
    def sap(width, height):
        return { 'area': Rectangle.sarea(width, height), 
                 'perimeter': Rectangle.sperimeter(width, height) }
    

# statische Methoden anwenden
print('Fläche: ', Rectangle.sarea(10, 5))
print('Umfang: ', Rectangle.sperimeter(10, 5))
print('Beides auf einmal: ', Rectangle.sap(10, 5))
r3 = Rectangle.createquad(7)
print(r3.area()) # 49

# Instanzmethoden
r = Rectangle(12, 9)
print(r.ap())
