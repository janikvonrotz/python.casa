# Fragen und Antworten

Hier werden Fragen und Antworten zum Kurs publiziert.

### Ein Programm mehrmals ausführen

Frage: Wie kann ich ein Programm mehrmals ausführen?

Antwort:

```python
# Programm mehrmals auführen

ausführen = 'Ja'

while(ausführen == 'Ja'):
    print("Programmcode ...")
    
    ausführen = input("Soll das Programm erneut ausgeführt werden? Ja, Nein: ")
```

### Vorlage Dokumetation mit Obsidian

Frage: Wie kann ich eine Dokumentation mit Obsidian erstellen?

Antwort:

```md
# Dokumentation

## Problemstellung

Beschreibung des Problems.

## Vorgehen

Vorgehen um das Problem zu lösen. Visualisierung mittels Flowchart.

![[Flowchart.png]]

## Umsetzung

Wie wurde die Lösung effektiv implementiert? Beschreibung der wichtigsten Programm-Teile.

## Rückblick

Gab es Problem bei der Umsetzung? Was lief gut und was nicht?

## Technische Anleitung

Wie kann man das Program ausführen? Welche Vorbereitungen müssen getroffen werden?
```

### HTML-Dokument erweitern

Frage: Wie kann ich das HTML-Dokument erweitern?

Antwort:

```python
from yattag import Doc

doc, tag, text = Doc().tagtext() # HTML-Funktionen abrufen

liste = ['Banane', 'Apfel', 'Orange']

with tag('html'): # HTML-Dokumente mit den Elementen zusammenstellen
    with tag('body'): # Mit with werden Funktionsaufrufe aneinander gereiht
        with tag('p', id = 'main'):
            text('Beispiel')
        with tag('a', href='https://example.com'):
            text('Linktext')
        with tag('ul'):
            for fruit in liste:
                with tag('li'):
                        text(fruit)
        doc.stag('img', src='https://raw.githubusercontent.com/janikvonrotz/python.casa/main/buch.png')

html = doc.getvalue() # HTML-Code generieren

with open('example.html', 'wt') as file:
    file.write(html)
```

### JSON-HTTP-Response verarbeiten

Frage: Wie kann eine HTTP-Response mit JSON-Inhalt verarbeiten?

Antwort:

```python
url = 'https://raw.githubusercontent.com/janikvonrotz/python.casa/main/topic-6/B%C3%BCcher.json'

import json
import urllib.request

response = urllib.request.urlopen(url)
data = json.loads(response.read().decode('utf-8'))

for book in data:
    print("Title: ", book['title'])
```

### PyQt5 mit Visual Studio Code

Frage: Wie kann `PyQt5` für Visual Studio Code installiert werden?

Antwort:

![Animation Installation PyQt5 auf Visual Studio Code](./install-pyqt5-vscode.gif)

### CSV nach SQLite importieren

Frage: Ich konnte für mein Projekt "Ersatzteilverwaltung" eine Datenbank erstellen (wie im Unterricht) und über die Webapplikation mit Python Flask (wie im Unterricht) aufrufen. Jetzt möchte ich noch unsere bestehende Ersatzteilliste in diese Datenbank importieren, damit nicht alle Positionen (ca. 1800) von Hand eingetragen werden müssen. Nach einigen Stunden suchen und ausprobieren (SQL, CSV, ..., habe ich das Gefühl nicht wirklich zum Ziel zu gelangen. Wie würdest du so etwas lösen?

Antwort: Ich nehme an, dass die Spalten im CSV und im der SQLite Tabelle die gleichen Namen haben. Der einfachste Weg um das CSV zu importieren ist wohl mit dem SQLiteStudio [https://sqlitestudio.pl/](https://sqlitestudio.pl/). Dazu ein Link mit einem Beispiel (weiter unten): [https://www.sqlitetutorial.net/sqlite-import-csv/](https://www.sqlitetutorial.net/sqlite-import-csv/). Mit dem SQLiteStudio kannst du die Datenbankdatei direkt bearbeiten. Natürlich geht das auch über die Kommandozeile, dazu musst du die SQLite Tools installieren: [https://www.sqlite.org/index.html](https://www.sqlite.org/index.html). Dieser Vorgang ist aber etwas schwieriger und ist ebenfall in meinem Beispiel-Link vorhanden.

### Spielfeld auf Kommandozeile

Frage: Wie kann ich ein Spielfeld, beispielsweise für Tic Tac Toe auf der Kommandozeile ausgeben?

Antwort: Dazu braucht es die folgenden Elemente: eine Schleife, eine Ausgabe einer Spielfeldzeile und eine Aktion die den Bildschirm zurücksetzt. Den Vorgang nennt man "Rendern".

```python
import os

# 3x3 Matrix erstellen
matrix = [[' ' for i in range(0,3)] for i in range(0, 3)]

# Matrix-Feld anpassen
matrix[1][1] = 'x'

# Funktion zur Ausgabe der Matrix
def ausgabe():
    for row in matrix:
        print('|{0}|{1}|{2}|'.format(row[0], row[1], row[2]))

# Bildschirm löschen und Matrix ausgeben
os.system('clear')
ausgabe()
```