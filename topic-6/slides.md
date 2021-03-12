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
* Objekte und Klassen
* Netzwerkfunktionen
* Grafische Benutzeroberflächen
* Erstellen HTML-Bericht

In der letzten Lektion bleibt Arbeitszeit für den Leistungsnachweis.

---
### Achtung

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
* Objekt: Alles ist ein Objekt,  beispielsweise Personen, Autos, Bäume, Häuser, Länder, Werkzeuge und Schuhe

---
### Beispiel Auto

Eine Veranschaulichung anhand des Objekts Auto.

![](../car-example.png)

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
*  Syntax nahezu Deckungsgleich mit Listen und Dictionaries

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
    file_writer = csv.writer(file, delimiter=',', quotechar='"')

    # Erste Zeile enthält die Tabellenüberschriften
    file_writer.writerow(['Name', 'Abteilung', 'Geboren im'])
    file_writer.writerow(['Peter Lustig', 'Buchhaltung', 'November'])
    file_writer.writerow(['Erika Meier', 'IT', 'März'])
```

ℹ️ Die erstellte Datei `Mitarbeiter.csv` kann mit einem Texteditor geöffnet werden.

---
### CSV-Datei lesen

🎬 Fügen sie diesen Code an:

```py
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
### Pause

⚡Wir machen eine Pause ⏱️ 20 Minuten

<iframe src="https://giphy.com/embed/iigcSmBaMUC5FoSUlu" width="280" height="280" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

---
### HTTP-Protokoll

* Hypertext Transfer Protocol (HTTP)
* Kommunikationsprotokol für das WWW
* Browser rufen Webseiten über HTTP auf

![](../http.png)

---
### HTTP-Request anzeigen

🎬 Zur Betrachtung eines HTTP-Requests führen sie folgende Aktionen aus:
* Browser und einen leeren Tab öffnen
* Mit `F12` die Entwicklerkonsole aufrufen
* In der Konsole die Ansicht *Netzwerk* öffnen
* In der Adressleiste `https://example.com` eingeben
* Den HTTP-Request mit Status `200` und Methode `GET` anklicken

---
### HTTP-Request Beispiel

Der HTML-Code der Webseite wird als HTTP-Response zurückgegeben.

![](../http-response.png)

---
### HTTP-Request mit Python

Dasselbe kann nun mit Python machen.

🎬 Erstellen sie die Datei `HTTP.py` und fügen sie diesen Code ein:

```py
import urllib.request
url = 'https://example.com'
response = urllib.request.urlopen(url)
binary = response.read() # Download durchführen
html = binary.decode('utf-8')

f = open('index.html', 'wt')
f.write(html)
f.close()
```

ℹ️ Öffnen sie die Datei `index.html` im Browser.

--- 
### Benutzeroberfläche

Bisher haben wir nur Programme im Terminalfenster ausgeführt.  
Mit Python können aber auch grafische Oberflächen entwickelt werden.  
Damit wir ein Graphical User Interface (GUI) entwickeln können, müssen Softwarepakete aus der Python-Bibliothek installiert werden.

---

### Qt-Paket installieren

🎬 Führen sie diese Anweisungen in Thonny aus:
* Navigation nach *Extras > Manage packages ...*
* `PyQt5` eingeben und auf *Paket von PyPI suchen* klicken
* Das Paket mit `installiere` installieren

ℹ️ Es kann sein, dass das Softwarepaket bereits vorinstalliert ist.

---
### Hello World mit Qt

🎬 Erstellen sie die Datei `GUI.py` mit diesem Code:

```py
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget             
from PyQt5.QtCore import QSize

class MeinFenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(QSize(300, 100)) # Fenstergröße und Titel einstellen
        self.setWindowTitle('Hello, Qt!') # Fenstertitel festlegen

        title = QLabel('Hello, Qt!', self) # Label definieren
        title.setAlignment(QtCore.Qt.AlignCenter) # Label mittig in Fenster anzeigen
        self.setCentralWidget(title)

App = QtWidgets.QApplication(sys.argv) 
Fenster = MeinFenster() 
Fenster.show() # Fenster anzeigen
sys.exit(App.exec_())
```

---
### GUIs sind komplex

GUIs entwickeln ist aufwändig!\
Wer sich weiter einarbeiten möchte kann diese Tutorial-Reihe schauen: [Python GUI Programmierung mit PyQT](https://www.youtube.com/watch?v=FiaPzdWKhJU&list=PLNmsVeXQZj7ruNQIfS8NRpjzZIRq0A8QP)

ℹ️ Mit dem [Qt-Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html) kann Oberflächen mit einem what-you-see-is-what-you-get (WYSIWYG) Editor erstellen.

---
### HTML

* Hypertext Markup Language (HTML)
* Auszeichnungssprache für strukturierte Dokumente
* Wird von Browser visuell dargestellt
* Grundlage des WWW

---
### HTML-Paket installieren

Damit man mit Python ein HTML-Dokument erstellen kann, braucht es ein zusätzliches Python-Paket.

🎬  Öffnet den Thonny Paketmmanager und installiert das Paket `yattag`.

Mehr zu [Yattag](https://www.yattag.org/).

---
### HTML-Dokument erstellen

🎬 Erstellen sie die Datei `HTML.py` und fügen sie diesen Code ein:

```py
from yattag import Doc

doc, tag, text = Doc().tagtext() # HTML-Funktionen abrufen

with tag('html'): # HTML-Dokumente mit den Elementen zusammenstellen
    with tag('body'): # Mit with werden Funktionsaufrufe aneinander gereiht
        with tag('p', id = 'main'):
            text('Beispiel')
        with tag('a', href='https://example.com'):
            text('Linktext')

html = doc.getvalue() # HTML-Code generieren

with open('example.html', 'wt') as file:
    file.write(html)
```

---
### HTML-Dokument im Browser öffnen

🎬 Fügen sie diesen Code an um die Datei direkt im Browser zu öffnen:

```py
# Die HTML-Datei im Browser aufrufen
import webbrowser
from pathlib import Path
webbrowser.open('file://' + str(Path('example.html').absolute()))
```

---
### Entscheidung

Die restliche Zeit steht für diese Optionen zur Verfügung:

* Frage und Antwort
* Aufgabe 6.1 erledigen
* Arbeit an Leistungsnachweis
* Repetition von vergangenen Themen

---
### Review

🎯 Ziele erreicht?
* Dateien schreiben, lesen und verarbeiten
* HTTP-Request ausführen
* Benutzeroberfläche erstellen

---
### Feedback

Habt ihr Feedbacks zum Kurs?\
Was hat euch gefallen und was nicht?\
Wurden die Erwartungen erfüllt?

---
### Abschluss

Ich wünsche gutes gelingen bei den Projekten ☘️.

Bei Fragen oder Problemen dürft ihr euch jederzeit melden!

---
