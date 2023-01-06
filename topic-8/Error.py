# ergebnis = 1/0
# print(ergebnis)

try:
    ergebnis = 1/0
    print(ergebnis)
except ZeroDivisionError:
    print("Durch Null teilen ist nicht möglich.")