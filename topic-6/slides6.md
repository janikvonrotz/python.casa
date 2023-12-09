# Slides Thema 6
## Funktionen und Flowchart

[◀️ Thema 6](README.md)

⚡Anwesenheit bestätigen

📖 Kapitel 9 Funktionen

---

### Lernziele

Ich kann ...
* neue Python-Funktionen schreiben und wiederverwenden.
* Parameter für Funktionen gemäss Anforderungen definieren.
* Den unterschied von lokalen und globalen Variablen erklären.
* Code mit einem Flowchart visualisieren.
* anhand eines Flowchart Code ableiten.

---

### Was sind Funktionen?

> Eine Funktion ist ein erstellter Programmcode, der aus dem „von-oben-nach-unten“-Ablauf des Programmes genommen wird und gezielt aufgerufen werden muss.

Wir haben bereits einige Funktionen verwendet, beispielsweise `len`. 

Funktionen helfen uns:

* Rendundanz zu vermeiden
* Code in Unterprogramme aufteilen
* Programm zu strukturieren

---

### Aufbau einer Funktion

Eine Funktion hat einen Input (Parameter) einen Output (Ergebnis).

![](len-function-input-output.png)

---

### Syntax einer Funktion

Die Syntax einer Funktion sieht wie folgt aus:

```
def funktionsname(para1, para2, para3):
    code
    mehr code
    noch mehr code
```

---

### Achtung bei Funktionen!

Bei der Anwendung von Funktionen gelten einige Regeln:
* Zuerst definieren dann verwenden
* Funktionen ohne Parameter sind erlaubt
* Alle Datentypen sind als Rückgabewerte erlaubt
* Funktionen können verschachtelt werden
* Mehrere Funktionen dürfen nicht den gleichen Namen haben

----

### IDE starten und einrichten

🎬 Führen Sie diese Aktionen aus:
* Neuer Ordner `Thema6` erstellen
* Neue Datei in Ordner `Funktion.py` erstellen

---
### Funktion mit Ergebnis

Wir starten mit einer einfachen Funktion Summe.

🎬 Diesen Code anfügen:

```python
def summe(x, y):
  return x+y

print(summe(4,5))
print(summe(7,5))
print(summe(11,9))
```

---
### Funktion ohne Ergebnis

Die Rückgabe eines Ergebnis ist nicht zwingend.

🎬 Diesen Code eingeben:

```python
def print_summe(x, y):
    print(x+y)

print_summe(4,5)
print_summe(7,5)
print_summe(11,9)
```

---

### Egebnis zur Weiterverarbeitung

Das Ergebnis einer Funktion kann weiter verarbeitet werden.

🎬 Diesen Code anfügen:

```python
n = summe(4, 5)
print(summe)
```

---

### Gültigkeitsbereiche

![](./python-scope.png)

---

### Lokale und globale Variablen

Variablen haben unterschiediche Gültigkeitsbereiche: Lokal und Global.

Variablen können innerhalb und ausserhalb einer Funktion deklariert werden.

---
### Variable Ausserhalb

🎬 Datei `Ausserhalb.py` erstellen und ausführen:

```python
def f1():
    print(x)

x=3
f1() # Ausgabe 3
```

---
### Lokale Variablen

🎬 Datei `Lokal.py` erstellen und ausführen:

```python
def f1():
    z=5
    print(z)

z=3
f1() # Ausgabe 5
print(z) # Ausgabe 3
```

---

### Globale Variable

Variablen mit der Kennzeichung `global` sind ausserhalb der Funktion verfügbar.

```python
def f1():
    global z
    z=z+3
    print(z) # Ausgabe 6

z=3
f1()
print(z) # Ausgabe 6
```

ℹ️ Das ist nice-to-know. In der Praxis gilt es globale Variablen zu vermeiden

---

### Parameter und Argumente

![](./parameters-and-arguments.png)

---

### Parameter

* Mit Prameter können Daten an eine Funktion übergeben werden
* Bei der Parameterdefinition besteht viel Gestaltungsraum

---

### Funktion mit Parameter

🎬 Datei `Parameter.py` erstellen und ausführen:

```python
def f1(x):
    print(x)

f1([1, 2]) # Ausgabe [1, 2]
```

---

### Aufruf ohne Parameter

Ein Aufruf ohne Parameter ist nicht möglich.

```python
def f1(x):
    print(x)

f1()
```

---

### Standardwert Parameter

Mit `para=default` definieren Sie für einen Parameter einen Standardwert. Dieser ist damit gleichzeitig optional.

```python
def f1(x=1):
    print(x)

f1()
```

Zur Definition der Parameter gibt noch [weitere Aspekte](archive.md).

---

### Aufgaben 1

Lösen Sie die [Aufgaben](excercise6.md#aufgaben) 6.1 bis 6.4.

⚡Aufteilung in Gruppen/Breakout-Rooms ⏱️ 20 Minuten

---

### Parameter überprüfen

> Im Vergleich zu anderen Programmiersprachen kann bei Python der Typ einer Variable nicht explizit festgelegt werden.

---

### Parameter in der Funktion prüfen

🎬 Datei `Ungültig.py` mit diesem Code erstellen:

```python
def f(n):
    if isinstance(n, int):
        return 2*n
    else:
        print('Ungültig')

print(f(1))
```

---

### Rekursive Funktionen

Funktionen können sich selber aufrufen.

🎬 Datei `Rekursion.py` mit diesem Code erstellen:

```python
def f(n):
    if n < 20:
        print(n)
        n += 1
        f(n)

f(0)
```

---

### Lambda-Funktionen

Lambda-Funktionen sind ganz spezielle Funktionen:
* Sie haben keinen Funktionsnamen.
* Parameter und Ausdruck müssen auf einer Zeile Platz haben.

Dazu die Syntax:

```
lambda var1, var2, var3, ...: ausdruck
```

---

### Deklaration Lambda-Funktion

Eine Kurzschreibweise für Funktionen.

🎬 Datei `Lambda.py` mit diesem Code erstellen:

```python
x = lambda a : a + 10 # Lambda Funktion wird einer Variable zugewiesen
y = x(5) # Lambda Funktion wird aufgerufen
print(y) # Ausgabe: 15
```

ℹ️ Die Lambda-Funktion macht das gleiche wie:

```python
def x(a):
	return a + 10
y = x(5)
print(y)
```

---

### Filter mit Lambda

Lambda Funktionen sind ausgezeichnet um Daten zu filtern.

Wir erinnern uns an die filter-Funktion `filter(function,list)`?

🎬 Datei `Lambda.py` mit diesem Code erweitern:

```python
data = [1, 2, 3, 9, 345, 36, 33]

filtered = list(filter(lambda x: x > 9, data))
print(filtered) # Ausgabe [345, 36, 33]
```

---

### Aufgaben 2

Lösen Sie die [Aufgaben](excercise6.md#aufgaben) 6.5 und 6.6.

⚡Aufteilung in Gruppen/Breakout-Rooms ⏱️ 10 Minuten

---

### Flowcharts

Mit Flowcharts kann man einen Vorgang oder Prozess visualisieren.

![](./flowchart.png)

Zur Darstellung gibt es verschiedene Symbole. Hier die wichtigsten:

---
### diagrams.net

🎬 Öffnen Sie die Website <https://app.diagrams.net> und erstellen Sie ein ein Diagramm mit den Element aus dem Bereich *General*.

![](./diagrams-general.png)

---

### Symbol Pfeil

Zeigt den logischen Fluss mit der Verbindung der Symbole.

![symbol-pfeil](./symbol-pfeil.svg)

---

### Symbol Start/Stop

Start und Ende des Prozesses.

![symbol-start](./symbol-start.svg)

---

### Symbol Eingabe/Ausgabe

Ein- und Ausgabe von Daten.

![symbol-eingabe](./symbol-eingabe.svg)

---

### Symbol Prozess

Arithmetische Operationen und Datenverarbeitung.

![symbol-prozess](./symbol-prozess.svg)

---

### Symbol Enscheidung

Enscheidungsfindung für ein oder mehrere Alternativen.

![symbol-entscheidung](./symbol-entscheidung.svg)

---

### Symbol Vorddefinierte Funktion/Prozess

Repräsentiert eine andere Funktion/Prozess.

![symbol-vordefiniert](./symbol-vordefiniert.svg)

---

### Flowchart Anwendung

* Mit Flowcharts kann man einen Algorithmus dokumentieren
* Mit Flowcharts kann man Pseudo-Code visualisieren

ℹ️ Pseudocode ist schriftliche Beschreibung eines Algorithmus

---

### Aufgaben 4

Lösen Sie die [Aufgaben](excercise6.md#aufgaben) 6.10 und 6.11.

⚡Aufteilung in Gruppen/Breakout-Rooms ⏱️ 10 Minuten

---
### Review

🎯 Wurden die [Lernziele](#lernziele) erreicht?

⚡ Feedback zu den Zielen einholen.
