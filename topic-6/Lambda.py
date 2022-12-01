x = lambda a : a + 10 # Lambda Funktion wird einer Variable zugewiesen
y = x(5) # Lambda Funktion wird aufgerufen
print(y) # Ausgabe: 15

def x(a):
	return a + 10
y = x(5)
print(y)

data = [1, 2, 3, 9, 345, 36, 33]

filtered = list(filter(lambda x: x > 9, data))
print(filtered) # Ausgabe [345, 36, 33]
