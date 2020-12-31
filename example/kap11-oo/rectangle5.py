#!/usr/bin/env python3

# Operator Overloading

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
        
    # Operator Overloading
    
    # Gleichheit
    def __eq__(self, other):
        return (self.w, self.h) == (other.w, other.h)
    
    # Vergleiche (< und <=)
    def __lt__(self, other):
        return self.area() < other.area()
    def __le__(self, other):
        return self.area() <= other.area()
    
    # Hash-Funktion
    def __hash__(self):
        return hash((self.w, self.h))

    # str (Ausgabe durch print/format)
    def __str__(self):
        return 'Rechteck(%.2f, %.2f)' % (self.w, self.h)

    # repr ('offizielle' String-Darstellung des Objekts)
    def __repr__(self):
        return 'Rectangle: w=%f, h=%f' % (self.w, self.h)
    
# Anwendung
r1 = Rectangle(12, 8)
r2 = r1
r3 = Rectangle(12, 8)

# Vergleiche von Objekten
if r1 is r2:
  print('r1 und r2 zeigen auf das gleiche Rechteck-Objekt')
  
if r1 == r3:  # erfordert __eq__
  print('r1 und r3 sind gleich groß')

# erfordert __str__
print(r1)            # Ausgabe Rechteck 12.00 mal 8.00

# erfordert __repr__
print(r1.__repr__()) # Rectangle: w=12, h=8.000000class Rectangle():


# Rechtecke vergleichen (erfordert __lt__ und __le__)
print( Rectangle(4, 3) > Rectangle(5, 2) )  # True

# Rechtecke sortieren (erfordert __lt__ und __le__)
lst = [Rectangle(3, 1), Rectangle(1, 2), Rectangle(2, 2)]
print(sorted(lst))

print(sorted(lst, key=lambda r: r.w))

# erfordert __hash__
set = {r1, r2, r3}
print(set)

# Set mit Doppelgänger
r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
set = {r1, r2}
print(len(set))
r2.w = 1
r2.h = 2
print(r1 == r2)
print(len(set))
print(set)
