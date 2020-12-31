#!/usr/bin/env python3
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Daten einlesen
data = pd.read_csv('bundeslaender.txt', 
                   sep='\t', 
                   decimal=',', 
                   header=None)

print(data)
print()

# Spalten und Zeilen beschriften, nur die ersten 5 Zeilen ausgeben
data.columns = ['Bundesland', 'Fläche', 'Einwohner', 'Hauptstadt']
data = data.set_index('Bundesland')
print(data.head())
print()

# Zugriff auf eine Spalte
print('Nur die Einwohner-Spalte (Serie)')
print(data['Einwohner'])
print()

# Berechnungen
print('Summe der Einwohner:  ', data['Einwohner'].sum())
print('Mittelwert der Fläche:', data['Fläche'].sum(), 'km2')
print()

# Selektion
big = data.loc[data['Einwohner'] > 2000000]
cnt = big.shape[0]
print(cnt, 'Bundesländer mit mehr als 2 Mil. Einwohner')
print(big)
print()

# Sortieren
print('Bundesländer mit mehr als 2 Mil. Einwohner sortiert nach Fläche')
sorted = big.sort_values(by=['Fläche'], ascending=False)
print(sorted.head())
