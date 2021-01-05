## Slides - Einführung Programmiersprache

Thema 1

---
### Referenz

Buch: Kapitel 1 Hello, World!

---
### Python

<iframe src="https://giphy.com/embed/Wvfq2yFumK61W" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

* 1991 entwickelt
* Einfache Syntax und gute Lesbarkeit
* Universell anwendbar
* Beliebt in den Naturwissenschaften

---
### Installation Python

Installation Python via [Python Download](https://www.python.org/downloads).

Video: [Python3-Tutorial #1 - Installation unter Windows 10](https://www.youtube.com/watch?v=hr1P_F7Vp9Y)

*Aufteilung in Breakout-Rooms.*

Ziel: Jeder kann Python-Shell starten.

---
### Terminal

Wir machen unsere erste Schritte in der Python-Shell.

> Keine Angst vor dem Terminal

*Terminal starten*

---
### Hello World

Anweisung eingeben:

```py
print('Hello, World!')
```

---
### Weitere Shell-Befehle

```py
name='Michael'
'Hallo ' + name + '!'
```

---
### Skript erstellen

* Projektordner und Unterordner `Thema01` erstellen
* Datei [HelloWorld.py](https://raw.githubusercontent.com/janikvonrotz/python.casa/main/examples/kap01/HelloWorld.py) im Ordner speichern

---
### Skript ausführen

* Im Unterordner das Terminal starten
	* Ordner im Explorer öffnen
	* In Adressleiste `cmd.exe eingeben
* Skript in Terminal ausführen 

```bash
ptyhon ./HelloWorld.py`
```

Unter GNU/Linux muss das Programm mit `chmod +x ./HelloWorld.py` ausführbar gemacht werden.

---
### Shebang

Was hat es mit der ersten Zeile auf sich?

GNU/Linux und MacOS:

```py
#!/usr/bin/env python3
```

Windows:

`.py` -> `python.exe`

---
### Installation IDE

IDE=Integrierte Entwicklungsumgebung  
Wir arbeiten mit Python 3.6 und höher.  

IDE-Editor [VS Code](https://code.visualstudio.com/) installieren. 

Video: [Visual Studio Code für die Python-Programmierung einrichten](https://www.youtube.com/watch?v=og51Lo5uKBA)

*Aufteilung in Breakout-Rooms.*

Ziel: Jeder kann IDE starten.

---
### Skript öffnen

* Das Skript `HelloWorld.py` in der IDE öffnen
* Den Ausgabe-Text ändern und speichern
* Das Skript mit der IDE oder dem Terminal ausführen

---
### Was ist ein Skript?

* Quellcode wird direkt vom Interpreter (Python) ausgeführt
* Programmcode wird kompiliert

---
### Was passiert beim kompilieren?
![](../python-datei-kompilieren.png)

---
### Anweisungen

Ist normalerweise Einzeilig.

```py
print('abc',
      'efg')
```

Mehre Anweisungen auf einer Zeile:

```py
a=1; b=2; c=3
```

---
### Blockelemente

Sprachelemente über mehrere Zeilen.

```py
if xxx:
    anweisung1a
    anweisung1b
else:
    anweisung2a
```

Anweisungen müssen eingeruckt sein.

---
### Input

Eingabe des Benutzers empfangen.

```py
name = input('Geben Sie Ihren Namen an:')
print('Ihr Name lautet:', name)
```

---
### Kommentare

Kommentieren direkt im Code.

```py
# ein Kommentar
print('abc')  # noch ein Kommentar
```

---
### Aufgaben

Lösen die Aufgaben und besprechen sie die Wiederholungsfragen.

*Aufteilung in Breakout-Rooms.*

---
### Review

Ziele erreicht?
* Python ist installiert und interaktiv verfügbar
* Erstellen und Ausführen von Skripten funktioniert
* Vorgang Kompilierung verstanden

---
### Feedback

<iframe src="https://giphy.com/embed/UVZCz81UWkobY3oHbd" width="300" height="300" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

* Was lief gut?
* Was kann ich verbessern?