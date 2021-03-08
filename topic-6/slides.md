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

*  JavaScript Object Notation (JSON) 
*  Beliebtestes Format für hierarchische Datenstrukturen
*  Syntax Nahezug Deckungsgleich mit Listen und Dictionaries

---
### JSON-Beispieldatei

🎬 Erstellen sie die Datei `Bücher.json` mit diesem Inhalt:

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

🎬 Datei `JSON.py` mit diesem Code ausführen:

```py
import json
with open('Bücher.json', 'r') as f:
    data = json.load(f)
print(data)
```

ℹ️ Mit der Anweisung `with ausdruck1 as var1, ausdruck2 as var2, ...: Code`  werden Ressourcen automatisch geschlossen. 

---
### JSON verabeiten

Der JSON-Inhalt kann ganz einfach verarbeitet werden.

🎬 Fügen sie diesen Code an:

```py
for book in data:
    print(f"Titel: {book['title']}")
    for author in book['authors']:
        print(f"Author: {author}")
    print('')
```

---
### CSV-Dateiformat
* Comma-separated values (CSV)
* Textdatei zur Speicherung strukturierter Daten
* Kann mit jeder Tabellekalkulations-Software bearbeitet werden

---

### CSV-Datei schreiben
🎬 Erstellen sie die Datei `CSV.py` und fügen sie diesen Code ein:

```py
import csv

with open('Mitarbeiter.csv', mode='w') as file:
    file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Erste Zeile enthält die Tabellenüberschriften
    file_writer.writerow(['Name', 'Abteilung', 'Geboren im'])
    file_writer.writerow(['Peter Lustig', 'Buchhaltung', 'November'])
    file_writer.writerow(['Erika Meier', 'IT', 'März'])
```

ℹ️ Die erstellte Datei `Mitarbeiter.csv` kann mit einem Texteditor geöffnet werden.

---
### CSV-Datei lesen

🎬 Fügen sie diesen Code an:

```
with open('Mitarbeiter.csv', newline='') as file:
    file_reader = csv.reader(file, delimiter=',', quotechar='"')
    line_count = 0
    for row in file_reader:
        # Erste Zeile enthält Tabellenüberschriften
        if line_count == 0:
            print(f'Spaltennamen sind {", ".join(row)}')
            line_count += 1
        else:
            print(f'{row[0]} arbeitet in der Abteilung {row[1]} und ist geboren im {row[2]}.')
            line_count += 1
    print(f'{line_count} Zeilen wurden verarbeitet.')
```

---
### HTTP

http://example.com/

--- 
### Download und Upload

---
### Qt

---
### Balkendiagram

---
### Review



---
### Abschluss

