import os

# 3x3 Matrix erstellen
matrix = [[' ' for i in range(0,3)] for i in range(0, 3)]

# Matrix-Feld anpassen
matrix[1][1] = 'x'

# Funktion zur Ausgabe der Matrix
def ausgabe():
    for row in matrix:
        print('|{0}|{1}|{2}|'.format(row[0], row[1], row[2]))

# Bildschirm löschen und Matrix ausgeben
os.system('clear')
ausgabe()

