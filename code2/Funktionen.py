liste = ['a','b','c']
index = 1
print(liste[index])

def f(a, b):
    return a, a+b
print(f(3, 5))

data = [17, 44, 3, 9, 75, 26, 33]
filtered = list(filter(lambda x: x < 30, data))
print(filtered)


def quersumme(zahl):
    summe = 0
    szahl = str(zahl)
    for s in szahl:
        summe += int(s) 
    return summe
print(quersumme(17))