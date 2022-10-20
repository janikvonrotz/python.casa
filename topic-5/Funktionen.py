lst = list(range(10, 101, 10))
lst.extend([110]) # Fügt eins oder mehre Elemente hinzu
lst.pop(2) # Entfernt element an der zweiten Position
lst.remove(80) # Entfern einen bestimmten Eintrag
print(lst)

def double(x):
    return x*2

print(list(map(double,lst)))

from functools import reduce
def sum(x,y):
    return x+y

print(reduce(sum,lst))

def IstGrösserAls(x,y=100):
    return (x > y)

print(list(filter(IstGrösserAls, lst)))

lst = list('Hello, World!')
lst.sort()
print(lst) # [' ', '!', ',', 'H', 'W', 'd', 'e', 'l', 'l', 'l', 'o', 'o', 'r']