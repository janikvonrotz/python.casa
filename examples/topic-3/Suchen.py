s="abcdefghijklmnopqrstuvwxyz"
print(s.find("hij")) # Ergebnis: 7
print(s.find("hij",8)) # -1 also nicht gefunden
print(s.rfind("hij")) # Suche von Rechts nach Links

print(s.replace('e', 'X'))