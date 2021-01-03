#!/usr/bin/env python3
from random import randint

# Liste mit 50 Zufallszahlen initialisieren
lst = []
for _ in range(50):
  lst.append(randint(0, 10))
print(lst)

# alternative Lösung zur Initialisierung
lst = [ randint(0, 10) for _ in list(range(50)) ] 
print(lst)

# Summe ausrechnen
sum = 0
for itm in lst:
    sum += itm
print('Summe:', sum)

# Nullen zählen
cnt = 0
for itm in lst:
    if itm==0:
        cnt+=1
print(cnt, 'Nullen gefunden')
# Kontrolle
print(lst.count(0))

# Position der ersten Null
if cnt:
    for i in range(len(lst)):
        if lst[i]==0:
            # in Python-Zählweise, 0 entspricht erstem Element
            print('Postion der ersten Null:', i)
            break
else:
    print('Die Liste enthält keine Null.')
# Kontrolle
print(lst.index(0))
