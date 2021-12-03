liste = []

for i in range(1,11):
    eingabe = int(input('Geben sie eine Zahl ein: '))
    liste.extend([eingabe])

print(min(liste), max(liste))

