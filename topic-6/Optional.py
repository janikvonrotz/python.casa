def f(a,b,c=-1,d=0):
    print(a,b,c,d)

f(6,7,8,9) # Ausgabe 6 7 8 9
f(6,7,8) # Ausgabe 6 7 8 0
f() # Fehler a und b werden vermisst