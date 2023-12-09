# Slides Thema 5

## Kontrollstrukturen und Listen

[◀️ Thema 5](README.md)

⚡Anwesenheit bestätigen

📖 Kapitel 7 Listen, Tupel, Sets und Dictionairies  
📖 Kapitel 8 Verzweigungen und Schleifen

---
### Lernziele

Ich kann ...
* die verschiedene Aufzählungstypen erkennen und benennen.
* den richtigen Aufzählungstyp gemäss Anforderung verwenden.
* Verzweigungen und Schleifen anwenden.
* Listen und Schleifen kombinieren.

---
### Ausblick

Thema 5:
* Listen, Tupel, Sets und Dictionaries
* Verzweigungen und Schleifen

Thema 6:
* Funktionen
* Flowcharts

ℹ️ In diesem Thema werden bereits erste Funktionen gezeigt.

---
### Listen, Tupel, Sets und Dictionaries

* Mehrere Variablen als Daten speichern
* Aufzählungen verarbeiten

| 0          | 1           | 2        | 3         | 4       | 5        | 6        | 7           | ... |
| ---------- | ----------- | -------- | --------- | ------- | -------- | -------- | ----------- | --- |
| `'Januar'` | `'Februar'` | `'März'` | `'April'` | `'Mai'` | `'Juni'` | `'Juli'` | `'August'` | ... |

---
### Übersicht Aufzählungstypen

Aufzählungen werden eingeklammert: `[]`, `()`, `{}` und `{key: value}`.

* **Listen**: Wichtigster und flexibelster Datentyp
* **Tupel**: Verwendung für zusammengehörende Daten
* **Sets**: Ungeordnete Menge ohne Doppelgänger
* **Dictionaries**: Kombination aus Schlüssel und Wert
* **Arrays**: Spielt eine untergeordnete Rolle

---
### Listen

* Kann einen bliebigen Datentyp aufnehmen
* Formulierung mit `[]`-Klammern

---
### IDE vorbereiten

🎬 Führen Sie diese Aktionen aus:
* Neuer Ordner `Thema5` erstellen
* Neue Datei in Ordner `Listen.py` erstellen

---
### Liste deklarieren

Wir erstellen eine einfache Liste und geben das dritte Element aus.

🎬 In der IDE ausführen:

```python
lst = [1, 2.3, 'abc', 'efg', 12]
print(lst[2]) # Ausgabe: abc
```

---
### range-Funktion

Mit der Range-Syntax Reihenfolgen definieren.

🎬 In der IDE ausführen:

```python
lst = list(range(10, 101, 10))
print(lst) # Ausgabe: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```

---
### Umwandlung Zeichenkette

🎬 Zeichenketten können einfach in Listen umgewandelt werden.

```python
lst = list('Hello, World!')
print(lst) # ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!'
```

---
### Funktionen zur Verarbeitung

Die wichtigsten Funktionen und Methoden zur Bearbeitung von Liste:

![](./list-functions-and-methods.png)

---
### Listenelemente hinzufügen

🎬 Führen Sie diese Aktionen aus:
* Erstellen Sie die Datei `Funktionen.py`
* Schreiben Sie diesen Code:

```python
lst = list(range(10, 101, 10))
lst.extend([110]) # Fügt eins oder mehre Elemente hinzu
lst.pop(2) # Entfernt element an der zweiten Position
lst.remove(80) # Entfern einen bestimmten Eintrag
print(lst)
```

---
### Aufgaben 1

Lösen Sie die [Aufgaben](excercise5.md#aufgaben) 5.1 und 5.2.

⚡Aufteilung in Gruppen/Breakout-Rooms ⏱️ 10 Minuten

---
### map-Funktion

Mit `map` kann eine Funktion auf jedes Listenelement angewendet werden.

```python
def double(x):
    return x*2

print(list(map(double,lst)))
```

ℹ️ Der Rückgabewert von `map` ist ein Iterator und muss zur Ausgabe in eine Liste umgewandelt werden.

---
### reduce-Funktion

Mit `reduce` wird eine Funktion auf jedes Listenelement (x) und auf das Resultat des Vorgänger (y) angewendet. 

```python
from functools import reduce
def sum(x,y):
    return x+y

print(reduce(sum,lst))
```

---
### filter-Funktion

Mit `filter` werden alle Listenelemente zurückgegeben, die eine Bedingung erfüllen. 

```python
def IstGrösserAls(x, y=100):
    return (x > y)

print(list(filter(IstGrösserAls, lst)))
```

---
### Listen sortieren

Elemente einer Liste werden nicht automatisch sortiert.

🎬 Führen Sie diesen Code aus:

```python
lst = list('Hello, World!')
lst.sort()
print(lst) # [' ', '!', ',', 'H', 'W', 'd', 'e', 'l', 'l', 'l', 'o', 'o', 'r']
```

---
### Tupel

*  Ist eine unveränderliche liste
*  Formulierung mit `()`-Klammern

---
### Tupel deklarieren

🎬 Führen Sie diese Aktionen aus:
* Erstellen Sie die Datei `Tupel.py`
* Schreiben Sie diesen Code:

**Tupel.py**

```python
t = (12, 73, 3)
print(t)
```

---
### Tupel Anwendungsfälle

Mit Tupel sind Zuweisungen und Vergleiche mit mehreren Variablen möglich.

🎬 Fügen Sie diesen Code an:

```python
(a, b, c) = (1, 2, 3)
if (a, b, c) == (1, 2, 3):
    print('Vollständige Übereinstimmung')
```

---
### Sets

*  Ungeordnete Liste ohne Doppelgänger
*  Formulierung mit `{}`-Klammern

---
### Sets deklarieren

🎬 Führen Sie diese Aktionen aus:
* Erstellen Sie die Datei `Sets.py`
* Schreiben Sie diesen Code:

**Sets.py**

```python
s = {1,2,3,3}
print(s)
```

---
### set-Methoden

Im Vergleich zu Listen gibt es weitere Methoden zur Bearbeitung eines Sets.

🎬 Fügen Sie diesen Code hinzu:

```python
s.add(4)
s.remove(2) # Entfernt Element
s.discard(2) # Gibt keinen Fehler aus, auch wenn Element bereits entfernt ist.
print(s)
```

---

### Dictionaries

* Elementaufzählungen mit einem Schlüssel zur Verwaltung
*  Formulierung mit `{key: value}`

---
### Dictionaries deklarieren

🎬 Führen Sie diese Aktionen aus:
* Erstellen Sie die Datei `Dict.py`
* Schreiben Sie diesen Code:

**Dict.py**

```python
key = "Blau"
value = '#FFFF00'
d = {'Rot': '#FF0000', key: '#0000FF', "Gelb": value}
print(d)
```

---
### keys und values Methoden

🎬 Fügen Sie diesen Code hinzu:

```python
print(d.get('Gelb')) # Ausgabe: #FFFF00
print(d.values()) # dict_values(['#FF0000', '#0000FF', '#FFFF00'])
print(d.keys()) # dict_keys(['Rot', 'Blau', 'Gelb'])
```

---
### Arrays

* Bei vielen Programmiersprachen haben Arrays eine zentrale Bedeutung
* Arrays sind nicht so flexibel wie Listen, Tupel, Sets und Dictionairies

---
### Aufgaben 2

Lösen Sie die [Aufgaben](excercise5.md#aufgaben) 5.3, 5.4 und 5.5.

⚡Aufteilung in Gruppen/Breakout-Rooms ⏱️ 15 Minuten

---
### Verzweigungen und Schleifen

* **Verzweigungen**: Abhängig von Bedingungen Codeteile ausführen
* **Schleifen**: Code mehrfach ausführen solange Bedingung erfüllt ist

![](./loop-with-condition.png)

---
### if-Verzweigung

Syntax sollte leicht verständlich sein:

```
if bedingung1:
    block1
elif bedingung2:
    block2
elif bedingung3:
    block3
else:
    block4
```

---
### if-Kurzschreibweise

Die if-Anweisung kann auf einer Zeile definiert werden.

```
x = wert1 if bedingung else wert2
```

ℹ️ In anderen Programmiersprachen gibt es dafür den [*Ternary Operator*](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)

---
### if-Beispiel

🎬 Erstellen und führen Sie die Datei `if.py` mit diesem Inhalt aus:

```python
antwort = input("Möchtest du Feierabend: ")

if antwort in ["Ja", "ja", "jep"]:
    print("Sehr gut!")
else:
    print("Ich glaube dir nicht!")
```

---
### Schleifen

Mit Schleifen können Sie Anweisungen wiederholen, ohne diese mehrfach zu schreiben.

---
### Mehrfache Anweisungen vereinfachen

Wie kann man das vereinfachen?

```python
print('a')
print('b')
print('c')
print('d')
print('e')
...
```

---
### for-Schleife

Die Syntax:

```
for var in elemente:
    anweisungen
```

---
### for mit Zeichenkette

🎬 Erstellen und führen Sie die Datei `for.py` mit diesem Inhalt aus:

```python
for element in 'abcde':
    print(element)
```

**Für** jedes Element **in** der List mach folgendes: Ausgabe Element.

---
### for mit Listen, Tupel und Sets

🎬 Fügen Sie diesen Code hinzu:

```python
for c in ['a', 'b', 'c']:
    print(c)
    
for i in (17, 87, 4): 
    print(i, end=' ') # end Paramter verhindert Zeilenumbruch
```
---
### for mit Dictionaries

Bei Schleifen mit Dictionaries enthält die Variable den Schlüssel.

🎬 Fügen Sie diesen Code hinzu:

```python
dict = {'a':12, 'c':78, 'b':3, 'd':43}

for k in dict:
    print(k, dict[k])

for k,v in dict.items():
    print(k, v)
```

---
### while-Schleife

Die Syntax:

```
while bedingung:
    anweisungen
```

---
### while-Beispiel

🎬 Erstellen und führen Sie die Datei `while.py` mit diesem Inhalt aus:

```python
i=1
while i<5:
    print(i)
    i+=1
# Ausgabe: 1 2 3 4
```

---
### List Comprehension

* Ein elegantes Konzpet zum verarbeiten von Listen.
* Form: `[ausdruck for x in liste]`

🎬 Fügen Sie diesen Code an:

```python
[print(s) for s in lst]
```

ℹ️ Schleifen sind Verarbeitungsmethoden für Listen.

---
### Aufgaben 3

Lösen Sie die [Aufgaben](excercise5.md#aufgaben) 5.6, 5.7 und 5.8.

⚡Aufteilung in Gruppen/Breakout-Rooms ⏱️ 15 Minuten

---
### Review

🎯 Wurden die [Lernziele](#lernziele) erreicht?

⚡ Feedback zu den Zielen einholen.
