def f(a,*b):
    print(a,b,type(b))
    
l = range(0,6)
f(1,l) # Ausgabe 1 (range(0, 6),) <class 'tuple'>
f(*l) # Ausgabe 0 (1, 2, 3, 4, 5) <class 'tuple'>