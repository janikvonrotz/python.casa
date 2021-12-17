def quersumme(zahl):
    summe = 0
    szahl = str(zahl)
    for s in szahl:
        summe += int(s)
    return summe

zahl = 177
print(f"Quersumme von {zahl} ist: {quersumme(zahl)}")

# Oder so

print(f"Quersumme von {zahl} ist: {sum([int(i) for i in [*str(zahl)]])}")
