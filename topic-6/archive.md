## Archiv

---
### Variable Parameteranzahl

Es können mehrere Parameter mit Standardwerten definiert werden.

🎬 Diesen Code in der Datei `Parameter.py` anfügen:

```python
def f(a,b,c=-1,d=0):
    print(a,b,c,d)

f(6,7,8,9) # Ausgabe 6 7 8 9
f(6,7,8) # Ausgabe 6 7 8 0
f() # Fehler a und b werden vermisst
```

---

### Parameter mit mehreren Werten

Wenn man einen Parameter mit `*para` oder `**para` definiert, kann man beliebig viele Werte übertragen.

* `*para` ist ein Tupel
* `**para` ist ein Dictionary

Das funktioniert auch beim Funktionsaufruf.

---

### Beispiel mit Liste

```python
liste = ['a','b','c']

print(liste) # Ausgabe ['a', 'b', 'c']
print(*liste) # a b c
```

ℹ️ Der `*` nimmt die Struktur einer oder mehreren Variablen auseinander oder vereinigt diesen.

---

### Beispiel mehrere Werte

🎬 Datei `Mehrere.py` mit diesem Code erstellen:

```python
def f(a, *b):
    print(a, b, type(b))
    
l = range(0,6)
f(1, l) # Ausgabe 1 (range(0, 6),) <class 'tuple'>
```

ℹ️ Keep it simple! Verwenden Sie einfache Parameter.