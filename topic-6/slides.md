## Ein- und Ausgabe

[Thema 6](readme.md)

⚡[Anwesenheit bestätigen](https://moodle.medizintechnik-hf.ch/mod/attendance/manage.php?id=4479) und Webcam einschalten.

📖 Kapitel 14 Dateien lesen und schreiben  
📖 Kapitel 15 Netzwerkfunktionen

---
### Rückblick

Besprechung der Wiederholungsfragen.  
Fragen zum Leistungsnachweis?

---

### Ausblick

Die ersten drei Lektionen:
* Verschiedene Dateiformate lesen und schreiben
* Objekt und Klassen
* Netzerkfunktionen
* Grafische Benutzeroberflächen

In der letzten Lektion bleibt Zeit für den Leistungsnachweis

---
### Warnung

Es werden einige neue Themen angeschnitten.\
Unbedingt melden, bevor es eine Crash gibt!

<iframe src="https://giphy.com/embed/5xrkJe3IJKSze" width="280" height="280" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

---
### Thonny Vorbereiten

🎬 Führen sie diese Aktionen aus:
* Neuer Ordner `Thema6` erstellen
* Neue Datei `Verzeichnisse.py` in Ordner erstellen

---
### Aktuelles Verzeichnis ausgeben

🎬 Diesen Code einfügen uns ausgeben.

```py
from pathlib import Path
current = str(Path.cwd().absolute())    
print('Aktuelles Verzeichnis:', current)
```

ℹ️ Der Rückgabewert von `Path.cwd().absolute()` ist ein Objekt.

---
### Objekte und Klassen

Das Objektorientierte Programmieren ist eine eigene Disziplin.

Ganz kurz:
* Klasse: Bauplan oder wie soll das Objekt aussehen
* Objekt: Alles ist ein Objekt,  beispielsweise Personen, Autos, Bäume, Häuser, Länder, Werkzeuge und Schuhe.

---
### Eine Klasse definieren

🎬 Erstellen sie die Datei `Objekt.py` mit diesem Inhalt:

```py
class Kaffeemaschine:
    def __init__(self, marke, anzahl):
        self.marke = marke
        self.anzahl = anzahl
    
    def Zustand(self):
        print(f"Ich bin eine {self.marke} Maschine")
        print(f"Es sind noch {self.anzahl} Kaffee(s) verfügbar")
    
    def Bestellen(self, anzahl):
        self.anzahl -= anzahl
```

---
### Objekt instanzieren

Nun erstellen wir anhand des Bauplans eine Kaffeemaschine.

🎬 Fügen sie diesen Code an:

```py
# Instanzieren
kaffeemaschine = Kaffeemaschine('Nespresso', 3)

# Methoden aufrufen
kaffeemaschine.Bestellen(2)
kaffeemaschine.Zustand()
```

---
### Textdatei schreiben

🎬 Erstellen sie die Datei `Schreiben.py` mit diesem Code:

```py
try:
    f = open('test.txt', 'wt')
    f.write('Lorem ipsum dolor sit amet, ...\n')
    f.write('Unicode äöüß\n')
    f.close()
  
except BaseException as err:
    print('Fehler:', err)
```

ℹ️ Wenn der Code `try`-Block nicht funktioniert, wird der `except`-Block aufgerufen.

---
### Textdatei lesen
🎬 Erstellen sie die Datei `Schreiben.py` mit diesem Code:

```py
try:
    f = open('test.txt', 'rt')
    for line in f:
        print(line, end='')
    f.close() 
  
except BaseException as err:
    print('Fehler:', err)
```

---
### JSON-Datenformat

---
### JSON-Beispieldatei

```json
[
    {
        "title": "Raspberry Pi",
        "isbn": "978-3836265195",
        "authors": [
            "Kofler",
            "Scherbeck",
            "Kühnast"
        ]
    },
    {
        "title": "Docker",
        "isbn": "978-3836261760",
        "authors": [
            "Öggl",
            "Kofler"
        ]
    }
]
```

---

### JSON-Dateien verarbeiten



---
### CSV-Dateien lesen und schreiben

---
### HTTP

--- 
### Download und Upload

---
### Qt

---
### Balkendiagram

---