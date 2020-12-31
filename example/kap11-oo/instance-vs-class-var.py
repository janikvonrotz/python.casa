#!/usr/bin/env python3
class MyClass():
    magicNumber = 42   # Klassenvariable
    # Konstruktor, initialisiert x und y mit Startposition
    def __init__(self, somedata, otherdata):
        self.data = somedata    # Instanzvariablen
        self.other = otherdata

obj1 = MyClass(3, 4)
print('Instanzvariablen von Objekt 1:', obj1.data, obj1.other)

obj2 = MyClass(7, 8)
print('Instanzvariablen von Objekt 2:', obj2.data, obj2.other)

print('Klassenvariable der Klasse "MyClass":', MyClass.magicNumber)
    
# Ausgabe
# Instanzvariablen von Objekt 1: 3 4
# Instanzvariablen von Objekt 2: 7 8
# Klassenvariable der Klasse 'MyClass': 42

print(vars(obj1))
print(vars(obj2))
print(vars(MyClass))
# Ausgabe
# {'data': 3, 'other': 4}
# {'data': 7, 'other': 8}
# {'__module__': '__main__', 'magicNumber': 42, 
#  '__init__': <function MyClass.__init__ at 0x10437a0d0>, 
#  '__dict__': <attribute '__dict__' of 'MyClass' objects>, ...}

obj2.magicNumber = 43      # erzeugt neue Instanzvariable
print(obj2.magicNumber)    # Instanzvariable: 43
print(MyClass.magicNumber) # Klassenvariable: weiterhin 42

