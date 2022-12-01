# Slides Thema 6
## Funktionen und Flowchart

[◀️ Thema 6](README.md)

⚡[Anwesenheit bestätigen](https://moodle.medizintechnik-hf.ch/mod/attendance/manage.php?id=8024)

📖 Kapitel 9 Funktionen

---
### Lernziele

Ich kann ...
* neue Python-Funktionen schreiben und wiederverwenden.
* Paramter für Funktionen gemäss Anforderungen definieren.
* Den unterschied von lokalen und globalen Variablen erklären.
* Code mit einem Flowchart visualisieren.
* anhand eines Flowchart Code ableiten.

---

### Code gestalten

Mit `if` kann man nur bestimmte Teile im Code ausführen.

Mit `while` und `for` können wir Anweisungen im Code wiederholen.

Wie können wir Code-Teile wiederverenden?

---

### Funktionen

Wir haben Funktionen bereits kennengelernt, beispielsweise `len`. 

Funktionen helfen uns:

* Rendundanz zu vermeiden
* Code übersichtlicher zu gestalten

---

### Aufbau einer Funktion

![](../python-function-definition.png)

---

### Achtung bei Funktionen!

Bei der Anwendung von Funktionen gelten einige Regeln:
* Zuerst definieren dann verwenden
* Funktionen ohne Parameter sind erlaubt
* Alle Datentypen sind als Rückgabewerte erlaubt
* Funktionen können verschachtelt werden
* Mehrere Funktionen dürfen nicht den gleichen Namen haben

---

### Syntax einer Funktion

Die Syntax einer Funktion sieht wie folgt aus:

```
def funktionsname(para1, para2, para3):
    code
    mehr code
    noch mehr code
```

----

### IDE starten und einrichten

🎬 Führen Sie diese Aktionen aus:
* Neuer Ordner `Thema5` erstellen
* Neue Datei in Ordner `Funktion.py` erstellen

---
### Funktion ohne Ergebnis

Wir erstellen eine Funktion.

🎬 Diesen Code eingeben:

```python
# Funktion ohne Ergebnis
def f1(x, y):
    print('Parameter 1:', x)
    print('Parameter 2:', y)
```

---
### Funktion mit Ergebnis

Und fügen eine zweite Funktion hinzu

🎬 Diesen Code anfügen:

```python
# Funktion mit Ergebnis
def f2(x, y):
  return x+y
```

---
### Funktion ausführen

Diese Funktionen führen wir nun aus.

🎬 Diesen Code anfügen:

```python
# Hier beginnt die Programmausführung
f1(2, 3)
# Ausgabe: Parameter 1: 2
#          Parameter 2: 3

n = f2(4, 5)
print(n) # Ausgabe: 9
```

---

### Gültigkeitsbereiche

![](../python-scope.png)

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

![](../parameters-and-arguments.png)

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

### Aufgaben 1

Lösen Sie die [Aufgaben](excercise6.md#aufgaben) 6.1 und 6.2.

⚡Aufteilung in Breakout-Rooms ⏱️ 10 Minuten

---

### Optionale Parameter

Mit `para=default` definieren Sie für einen Parameter einen Standardwert. Dieser ist damit gleichzeitig optional.

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

---

### Aufgaben 2

Lösen Sie die [Aufgaben](excercise6.md#aufgaben) 6.3 und 6.4.

⚡Aufteilung in Breakout-Rooms ⏱️ 10 Minuten

---

### Parameter überprüfen

> Im Vergleich zu anderen Programmiersprachen kann bei Python der Typ einer Variable nicht explizit festgelegt werden.

---

### Parameter dennoch überprüfen

🎬 Datei `Ungültig.py` mit diesem Code erstellen:

```python
def f(n):
    if isinstance(n,int):
        return 2*n
    else:
        print('Ungültig')

print(f(1))
```

---

### Rekursion

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

### Aufgaben 3

Lösen Sie die [Aufgaben](excercise6.md#aufgaben) 6.5 und 6.6.

⚡Aufteilung in Breakout-Rooms ⏱️ 10 Minuten

---

### Pause

⚡Wir machen eine Pause ⏱️ 10 Minuten

<iframe src="https://giphy.com/embed/3o7aCVTfelG4XSbv3y" width="280" height="280" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

---

### Flowcharts

Mit Flowcharts kann man einen Vorgang oder Prozess visualisieren.

![](../flowchart.png)

Zur Darstellung gibt es verschiedene Symbole. Hier die wichtigsten:

---

### Symbol Pfeil

Zeigt den logischen Fluss mit der Verbindung der Symbole.

![symbol-pfeil](../symbol-pfeil.svg)

---

### Symbol Start/Stop

Start und Ende des Prozesses.

![symbol-start](../symbol-start.svg)

---

### Symbol Eingabe/Ausgabe

Ein- und Ausgabe von Daten.

![symbol-eingabe](../symbol-eingabe.svg)

---

### Symbol Prozess

Arithmetische Operationen und Datenverarbeitung.

![symbol-prozess](../symbol-prozess.svg)

---

### Symbol Enscheidung

Enscheidungsfindung für ein oder mehrere Alternativen.

![symbol-entscheidung](../symbol-entscheidung.svg)

---

### Symbol Vorddefinierte Funktion/Prozess

Repräsentiert eine andere Funktion/Prozess.

![symbol-vordefiniert](../symbol-vordefiniert.svg)

---

### Flowchart Anwendung

* Mit Flowcharts kann man einen Algorithmus dokumentieren
* Mit Flowcharts kann man Pseudo-Code visualisieren

ℹ️ Pseudocode ist schriftliche Beschreibung eines Algorithmus

---

### Aufgaben 3

Lösen Sie die ersten zwei Aufgaben.

⚡Aufteilung in Breakout-Rooms ⏱️ 10 Minuten

Ziel: Aufgaben 5.7 und 5.8 sind gelöst.

---
### Review

🎯 Wurden die [Lernziele](#lernziele) erreicht?

⚡ Feedback zu den Zielen einholen.
