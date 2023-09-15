# Wissensprüfung 2

Ziel: Die Stundierenden verstehen Datenstrukturen zur Aufzählung, die Definition und Aufbau von Funktionen und Code in der Objekt-orientierten Darstellung .

Format: Schriftlich\
Dauer: 45 Minuten\
Anteil Gesamtnote: 35%

## Abgrenzung

Die Prüfung baut auf Anforderungen von [Prüfung 1](exam1.md) auf. Dazu kommen Folien, Aufgaben und Wiederholungsfragen von [T5](topic-5/README.md), [T6](topic-6/README.md) ,  [T7](topic-7/README.md) und [T8](topic-8/README.md).

Mögliche Fragetypen der Prüfung sind:

* Ja/Nein bzw. Wahr/Falsch
* Mehrere Antworten
* Zuordnung
* Code-Zeile ergänzen
* Bild markieren und kommentieren
* Code mit Elementen visualisieren
* Mehrere Code-Zeilen schreiben
* Analyse von komplexen Programmen

## Durchführung

Vor der Lektion 9 absolvieren die Studierenden eine Papier-Prüfung unter Aufsicht des Dozierenden.

## Beispielfragen

1\. Wir haben eine Liste und möchten das dritte Element ausgeben. Was geben Sie für `X` ein?

```python
liste = ['Bern', 'Luzern', 'Zürich', 'Genf']
print(list[X])
```

2\. Ordnen Sie Syntax den Aufzählungstypen zu:

1\. `[]` 2. `()` 3. `{}` 4. `{key: vlaue}`

Tupel: \_\_\
Set:  \_\_\
Dictionary:  \_\_\
Liste:  \_\_

3\. Was ist der Unterschied zwischen Python Klassen und Objekten? Erläutern Sie in eigenen Worten.

4\. Sie erhalten einen Klassen-Code. Wie instanzieren Sie das Objekt dazu? Schreiben ihre Ergänzung unten hin.

```python
class Kaffeemaschine:
	def __init__(self, typ, marke, farbe, tassen=2):
		self.typ = typ
		self.marke = marke
		self.farbe = farbe
		self.tassen = tassen
kaffeemaschine = ____________________________________________________
```

5\. Schreiben Sie ein Programm mit einer `while` Schleife, das von 100 bis 0 zählt. Schreiben sie das Programm unten hin.