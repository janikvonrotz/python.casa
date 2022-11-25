liste = []

for i in range(1,6):
    eingabe = int(input('Geben Sie eine Zahl ein: '))
    liste.extend([eingabe])

print(min(liste), max(liste))

