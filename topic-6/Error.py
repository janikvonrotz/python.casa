try:
    ergebnis = 1/0
    print(ergebnis)
except ZeroDivisionError:
    print("Man kann nicht durch Null teilen.")