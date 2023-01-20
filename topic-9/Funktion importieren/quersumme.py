def quersumme(zahl):
    summe = 0
    szahl = str(zahl)
    for s in szahl:
        summe += int(s)
    return summe