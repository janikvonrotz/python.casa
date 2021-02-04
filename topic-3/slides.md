## Boolsche Algebra  und Zeichenketten

[Thema 3](readme.md)

⚡[Anwesenheit bestätigen](https://moodle.medizintechnik-hf.ch/mod/attendance/manage.php?id=4479) und Webcam einschalten.

📖 Kapitel 3 Operatoren und 5 Zeichenketten

---
### Herkunft Boolean

* Boolean sind benannt nach Georg Boole (1815)
* Er gründete die moderne mathematische Logik

> Seinen Arbeiten verdanken wir den Computer

---
### Boolsche Algebra

Im Programmieren sind wir immer mit logischen Problemstellungen konfrontiert.

Boolsche Algebra hilft uns diese Probleme zu lösen.

---
### Binäre und logische Operatoren

![](../binary-operators.png)

---
### Gesetze

In den nächsten Slides schauen wir uns die Gesetze[^1] der boolschen Algebra an.

🎬 Deklariert diese Variablen in der Python-Shell:

```py
a = True
b = False
```

---
### Konjunktion

🎬 In der Python-Shell ausführen:

```py
a and b
```

---
### Disjunktion

🎬 In der Python-Shell ausführen:

```py
a or b
```

---
### Negation

🎬 In der Python-Shell ausführen:

```py
not a
not b
```

---
### Kommutativ

🎬 In der Python-Shell ausführen:

```py
(a and b) == (b and a)
(a or b) == (b or a)
```

---
### Assoziativ

🎬 In der Python-Shell ausführen:

```py
c = True
((a and b) and c) == (a and (b and c))
((a or b) or c) == (a or (b or c))
```

---
### Absorption

🎬 In der Python-Shell ausführen:

```py
(a or (a and b)) == a
(a and (a or b)) == a
```

---
### Distributiv

🎬 In der Python-Shell ausführen:

```py
a or (b and c) == (a or b) and (a or c)
a and (b or c) == (a and b) or (a and c)
```

---
### Komplentär / Idempotenz

🎬 In der Python-Shell ausführen:

```py
(a or not a) == 1
(a and not a) == 0
```

---
### de Morgan

🎬 In der Python-Shell ausführen:

```py
not (a or b) == (not a and not b)
not (a and b) == (not a or not b)
```

---
### Neutralität / Extremal

🎬 In der Python-Shell ausführen:

```py
(a or 0) == a
(a and 1) == a
```

---
### Doppelte Negation

🎬 In der Python-Shell ausführen:

```py
(not not a) == a
```

---
### Short-Circuit-Evaluation

Evaluation wird abgebrochen sobald Ergebnis feststeht.

```py
x = True
y = False
y and (x and y) or (y and x) # Evaluation wird nach y abgebrochen
y and (x and y) or (y and x) # Evaluation vollständig geprüft
```

---
### Aufgaben 1

Lösen sie die ersten zwei Aufgaben.

⚡Aufteilung in Breakout-Rooms ⏱️ 10 Minuten

Ziel: Aufgabe 3.1 und 3.2 gelöst.

---
### Pause

⚡Wir machen eine Pause ⏱️ 10 Minuten

<iframe src="https://giphy.com/embed/pp6pC4XgyDOiQ" width="280" height="280" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

---
### Grundregeln Zeichenketten

* Wichtigkeit: Zeichenketten > Zahlen
* In Python macht den Umgang mit Zeichenketten relativ leicht

```py
s='abc'
print(type(s)) # <class 'str'>
```

---
### Apostrophe

Einfache oder doppelte Apostrophe sind gleichwertig.

```py
'abc' == "abc"
```

---
### Mehrzeilige Zeichenketten

🎬 Erstellen sie eine mehrzeilige Zeichenkette:

```py
s = """Das ist
       eine lange
    Zeichenkette."""
print(s)
```

ℹ️ Zeilenumbrüche werden mit der Escape-Sequen `\n` gespeichert.

---
### Zeichenketten kombinieren

```py

```

---
### Zeichenketten vervielfältigen

---
### Sonderzeichen

---
### Teilzeichenketten

---
### Schrittweite

---
### Zeichenkettenfunktionen

---
### Suchen und ersetzen

---
### Formatierung mit %-Operator

---
### Format-Kurzschreibweise

---
###  Aufgaben 2

Breakout Session 2

---
### Abschluss

---
### Referenzen

[^1]: [Wikipedia - Boolesche Algebra](https://de.wikipedia.org/wiki/Boolesche_Algebra#Definition)