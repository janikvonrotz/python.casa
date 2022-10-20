a = 27
b = 12

if a == 0:
    ergebnis = b
else:
    while(b != 0):
        if a > b:
            a = a - b
        else:
            b = b - a
    ergebnis = a

print (ergebnis)