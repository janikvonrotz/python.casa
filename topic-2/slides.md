## Variablen und Datentypen

[Thema 2](README.md)\
Umfang ⏱️: 2 Lektionen

⚡[Anwesenheit bestätigen](https://moodle.medizintechnik-hf.ch/mod/attendance/manage.php?id=6139)

📖 Kapitel 2 Variablen, 3 Operatoren und 4 Zahlen

---
### Besprechung Thema 1

* Ziele erreicht?
* Aufgaben und Wiederholungsfragen

---
### Variable

> Eine Variable ist ein Name für eine Leerstelle in einem logischen oder mathematischen Ausdruck.

---

### Variablen

Programm speichert vorübergehend Werte, Zeichenketten und andere Informationen.

Variable deklarieren:

```py
a = 1
b = 'abc'
```

---
### Datentyp

> Der Datentyp gibt an, von welcher Art die Daten sind, die mit ihm beschrieben werden (Datenvereinbarung), und welche Operationen auf diesen ausgeführt werden können.

---
### Datentypen

Es gibt verschiedene Typen zum Speichern von Daten.

![](../datentypen.png)

---
### Lebensdauer

Variablen leben bis zum Programmende.

Beim Start eines Programms wird es in den Arbeitsspeicher (Memory) geladen

![](../microprocessor.png)

---
### Der Heap

Im sogenannten Heap speichert Python die Werte der Variablen

![](../python-vm.png)

---
### Fensterdarstellung wechseln 1

Für den weiteren Verlauf des Unterrichts arbeiten wir mit Thonny und der Website gleichzeitig. Dazu wechseln wir die Fensterdarstellung.

---
### Fensterdarstellung wechseln 2

🎬 Folgende Aktion ausführen:
* Thonny öffnen und das Fenster auf die linke Seite schieben
	* Windows: <kbd>windows</kbd> + <kbd>←</kbd> drücken
* [ptyhon.casa - Thema 2 Slides](https://python.casa/topic-2/slides.html#fensterdarstellung-wechseln-1) öffnen und auf die rechte Seite schieben
	* Windows: <kbd>windows</kbd> + <kbd>→</kbd> drücken

---
### Heap anzeigen

Mit Thonny können wir sehen wie Python die Variablen und deren Werte verwaltet.

🎬 In Tonny Menu *Ansicht* anwählen und die Optionen *Heap* und *Variablen* aktivieren.

---
### Variablen anzeigen

> Variablen sind lediglich Referenzen

🎬 Folgende Aktionen in Thonny ausführen:
* Neues leeres Skript erstellen
* Datei speichern im neuen Ordner `Thema2` als `Heap.py`
* Anweisung `x=1` eingeben und ausführen

---
### Ergebnis Heap

Eine Variable ist eine Referenz zu einem Eintrag im Heap.

![](../thonny-variables-and-heap.png)

---
### Datentyp anzeigen

Variablen haben keinen Typ, aber deren Wert.

🎬 Im Programm `Heap.py` diesen Code anfügen und ausführen.

```py
print(type(x)) # Ausgabe: <class 'int'>
```

---
### Typumwandlung automatisch

Bei Berechnungen wandelt Python automatisch den Typ um.

🎬 Datei `Umwandlung.py` erstellen, Code eingeben und ausführen.

```py
a = 2 # int
b = 2.4 # float
c = a*b # auch float
print(c) # 4.8
```

---
### Typumwandlung manuell

Im Normalfall müssen Typumwandlungen explizit festgelegt werden.

🎬 Datei `Umwandlung.py` mit Code erweitern und ausführen.

```py
s = 'abc' # str
x = 3 # int
s = s + str(x)
print(s) # Ergebnis 'abc3'
```

---
### Gültigkeitsbereich

Ist eine Variable einmal definiert, kann sie weiterverwendet werden.

```py
if 1: # das ist immer erfüllt
    x=1 # daher wird diese Zuweisung ausgeführt
print(x) # ok, Ausgabe 1
```

```py
if 0: # das ist nie erfüllt
    x = 1 # daher wird diese Zuweisung nicht ausgeführt
print(x) # Fehler: name 'x' is not defined
```

---
### Zahlen

Python ...
* hat einen nahezu unendlich grossen Zahlenraum
* unterstützt komplexe Zahlen
*  kann Zufallszahlen generieren

---
### Operatoren

![](../operatoren.png)

---
### Gleicheit

Mit dem `=` macht man eine Zuweisung. Zur Prüfung der Gleicheit braucht es `==`.

```py
print(1 == 1) # Ausgabe: True
```

---
### Restwert

Der `%`-Operator macht eine Division und gibt es Restwert zurück.

```py
7 % 3 # Ausgabe: 1
```

ℹ️  Der Modulo-Operator ist in jeder Programmiersprache verfügbar.

---
### Zuweisung mit Operation

Bestimmte Operatoren kann man zusammennehmen.

```py
a = 1
a = a + 1
```

```py
a = 1
a =+ 1
```

---
### Division

Gewöhnliche Division liefert immer Fliesskommazahlen.

```py
print(2/3, 6/3) # Ausgabe: 0.6666666666666666 2.0
```

Für ganzzahlige Division `//` verwenden.

```py
print(2//3, 6//3) # Ausgabe: 0 2
```

🎬  Führen sie die Divisionen aus.

---
### Runden

🎬  Zum Runden die Funktion `round` verwenden.

```py
print(round(1.5)) # Ausgabe: 2
print(round(1.4)) # Ausgabe: 1
```

ℹ️ Mit `help(round)` erfahren sie mehr zur Funktion.

---
### Zufallszahl generieren

> Die Vertrauenswürdigkeit jeder Verschlüsselung basiert auf der Korrektheit von Zufallszahlen.

Zusätzliche Funktionen können mit `import` importiert werden.

```py
from random import randint
print(randint(0, 7))
```

🎬  Generieren sie eine Zufallszahl von 1 bis 10.

---
### Boolsche Werte

Boolsche Werte kennen zwei Zustände.

🎬  Führt das folgende Skript aus:

```py
a = True
b = 7==8
c = not 0
d = int(False)
print(a,b,c,d)
```

---
### Aufgaben

Lösen sie die [Aufgaben](excercise.md#aufgaben) und besprechen sie die [Wiederholungsfragen](excercise.md#wiederholungsfragen).

⚡Aufteilung in Gruppen/Breakout-Rooms ⏱️ 10 Minuten

Ziel: Alle Aufgaben gelöst.

---
### Review

🎯 Ziele erreicht?
* Variablen deklarieren und verwenden
* Datentypen verstanden
* Einfache Berechnungen ausführen

<!-- ---
---
### Abschluss

📝 Ich bitte euch die restlichen Aufgaben und Wiederholungsfragen im Selbststudium durchzugehen.

👋 Bis zum nächsten Mal.
-->