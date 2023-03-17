# Slides Thema 10
## Datenbanken

[◀️ Thema 10](README.md)

⚡[Anwesenheit bestätigen](https://moodle.medizintechnik-hf.ch/mod/attendance/manage.php?id=8024)

📖 Kapitel 20 Wissenschaftliche Anwendung

---

### Lernziele

Ich kann ...
* den Begriff Datenbank und relationales Datenbankmanagementsystem erklären.
* mit Python eine SQLite-Datenbankdatei erstellen.
* auf einer SQLite-Datenbank die CRUD-Operationen ausführen.

---

### Grosse Datenmengen

Wie man Text-Daten liest und speichert, wissen wir. Im Umgang mit grossen Datenmengen ergeben Sie neue Fragen:
* Wie speichert man grosse Datenmengen?
* Wie stellt man sicher, dass in den Daten keine Fehler sind?
* Wie ermöglicht man den Zugriff für mehrere Programme auf dieselben Daten?

---

### Daten zentral speichern

Daten in einer Datenbank an einem Ort speichern.

![](./data-central.png)

---

### Was ist eine Datenbank?

>  Eine Datenbank ist ein System zur **elektronischen Verwaltung von Daten**. Die Kernaufgabe von Datenbanken liegt in der effizienten, dauerhaften und fehlerfreien Speicherung großer Datenmengen sowie in der bedarfsgerechten Bereitstellung benötigter Informationen.

ℹ️ Das Gegenteil einer Datenbank ist Excel.

---

### Datenbanken bereitstellen

Auf einem Server installiert man ein Datenbankmanagementsystem.

![](./datenbanksystem.png)

Auf dem Desktop kann man direkt auf die Datenbank zugreifen.

---

### Welche Datenbanktypen gibt es?

Grundtypen:
* **Relational**: Definierte Tabellen und Spalten, Abfragen und Manipulation von Daten nur in diesem Raster möglich.
* **NoSQL/Non-Relational**: Schema ist freiher, dafür Datenkonsistenz nicht gegeben.

---

### Beispiel Relational/Non-Relational

![](./relational-non-relatonal.png)

---

### Relationales Datenbankmanagementsystem

Es gibt verschiedene RDBMS. Wir interessieren uns für *PostgreSQL* und *SQLite*.

* **PostgreSQL**: Komplexes Datenbanksystem, dass auf Server installiert wird.
* **SQLite**: Ist im wesentlichen eine Datenbankdatei, die überall installiert werden kann.

---

### SQLite

Ist die meist verbreitete Datenbank-Engine[^1]. Sie ist auf jedem Smartphone vorhanden.

![](./sqlite.png)

Wie viele andere Datenbanksysteme ist SQLite SQL-basiert. Bei SQL (Structured Query Language) handelt es sich um die am meisten verwendete Datenbanksprache.

---

### Python und SQLite

Mit Python können wir eine SQLite-Datenbank erstellen und bearbeiten. Wir wollen diese Lager-Tabelle erstellen:

| ID  | Name        | Referenz  | Barcode      | Lager | Preis |
| --- | ----------- | --------- | ------------ | ----- | ----- |
| 1   | Holztisch   | E-COM06   | 601647855633 | 3     | 147   |
| 2   | Bürostuhl   | FURN_7777 | 601647855634 | 1     | 70.50 |
| 3   | Abfalleimer | E-COM10   | 601647855649 | 5     | 43    |

---

### Vorgehen

Eine Datenbank wird in den folgenden Schritten erzeugt:
-   Anlegen der Datenbank
-   Anlegen von Datenbanktabellen durch Angabe der Struktur
-   Eingabe der Datensätze in die Datenbanktabellen

---

### Modul und Datentypen

SQLite wird über das Modul `sqlite3` direkt in Python eingebunden. Es bietet standardmäßig die folgenden Datentypen:

-   **TEXT**: Für Zeichenketten
-   **INTEGER**: Für ganze Zahlen
-   **REAL**: Für Zahlen mit Nachkommastellen
-   **BLOB**: Für _binary large objects_, also große binäre Datenmengen
-   **NULL**: Entspricht _None_ in Python

🤔  Wie ordnen Sie die Datentypen der Spalten der Lager-Tabelle zu?

---

### VSCode vorbereiten

🎬 Führen Sie diese Aktionen aus:
* Neuer Ordner `Thema10` erstellen
* Ordner mit VSCode öffnen
* Datei `lager.py` anlegen

---

### Datenbank-Datei erzeugen

Aktualisiert die Datei `lager.py` mit diesem Code:

```python
import os, sys, sqlite3

# Datei entfernen wenn existiert
if os.path.exists("lager.db"):
    os.remove("lager.db")

# Verbindung zur Datenbank erzeugen
connection = sqlite3.connect("lager.db")

# Datensatz-Cursor erzeugen
cursor = connection.cursor()
```

---

### Tabelle erstellen

🎬 Mit SQL erstellen wir nun eine Tabelle. Fügen Sie diesen Code hinzu:

```python
# Datenbanktabelle erzeugen
sql = """CREATE TABLE lager(
    id INTEGER PRIMARY KEY,
    name TEXT,
    referenz TEXT ,
    barcode TEXT,
    lager INTEGER,
    preis REAL)"""
cursor.execute(sql)
```

---

### Datensatz hinzufügen

🎬 Fügen Sie diesen Code an, um einen Datensatz zu erzeugen:

```python
# Datensatz erzeugen
sql = "INSERT INTO lager VALUES(1, 'Holztisch', 'E-COM06', '601647855633', 3, 147)"
cursor.execute(sql)
connection.commit()

# Verbindung beenden
connection.close()
```

🎬 Führen Sie das Programm `lager.py` aus. Es wird nun eine `lager.db` Datei erstellt.

---

### Datenbank anschauen

Mit dieser VSCode-Erweiterung können Sie die Datenbank-Datei anschauen:

![](./vscode-sqlite.png)

🎬 Installieren Sie diese Erweiterung.

---

### SQLite Datenbank anschauen

🎬 Zeigen Sie den Inhalt von `lager.db` wie folgt an:
* <kbd>ctrl</kbd> + <kbd>shift</kbd> gedrückt halten und zusätzlich <kbd>p</kbd> drücken
* Im Dialog `Open Database` eingeben und Befehl mit <kbd>Enter</kbd> bestätigen
* Die vorgeschlagene Datenbank auswählen und mit <kbd>Enter</kbd> bestätigen
* Unten links erscheint der `SQLite Explorer`, darauf klicken und die Datenbank anzeigen

![sqlite-browse](./sqlite-browse.gif)

---

### SQLlite Datenbank anschauen

🎬 Zeigen Sie den Inhalt von `lager.db` wie folgt an:
* Rechtsklick auf die Datebank-Datei machen
* Aktion *Opten Database* wählen.
* Unten links erscheint der `SQLite Explorer`, darauf klicken und die Datenbank anzeigen

![](./vscode-sqlite-open-database.png)

---

### Weitere Datensätze einfügen

🎬 Fügen wie weitere Datensätze hinzu, indem Sie den Code unten an der richtigen Stelle einfügen.

```python
# Datensatz erzeugen
sql = "INSERT INTO lager VALUES(1, 'Holztisch', 'E-COM06', '601647855633', 3, 147)"
cursor.execute(sql)
sql = "INSERT INTO lager VALUES(2, 'Bürostuhl', 'E-COM06', '601647855634', 1, 70.50)"
cursor.execute(sql)
sql = "INSERT INTO lager VALUES(3, 'Abfalleimer', 'E-COM06', '601647855649', 5, 43)"
cursor.execute(sql)
connection.commit()
```

⭐ [lager.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-10/lager.py)

---

### Daten abfragen

Wir möchten die Daten mit SQL/Python auslesen.

🎬 Erstellen Sie eine neue Datei `abfragen.py`.

---

### Alle Datensätze anzeigen

🎬 Ergänzen Sie `abfragen.py` und führen Sie den Code aus.

```python
import sqlite3

# Verbindung, Cursor
connection = sqlite3.connect("lager.db")
cursor = connection.cursor()

# SQL-Abfrage
sql = "SELECT * FROM lager"

# Absenden der SQL-Abfrage und Empfang des Ergebnis
cursor.execute(sql)

# Ausgabe des Ergebnis
for datensatz in cursor:
    print(datensatz[1])
    print(datensatz)

# Verbindung beenden
connection.close()
```

🤔 Wie kann man nur bestimmte Datensätze ausgeben?

---

### Daten filtern

Das Schlüsselwort heisst `WHERE`.

🎬 Ersetzen Sie die SQL-Abfrage mit:

```python
sql = "SELECT * FROM lager WHERE id = 1"
```

ℹ️ SQL hat eine andere Syntax als Python.

🤔 Wie kann man bestimmte Datensätze verändern?

---

### Datensatz verändern

Das Schlüsselwort heisst `UPDATE`.

🎬 Ersetzen Sie die SQL-Abfrage mit:

```python
# Datensatz aktualisieren
sql = "UPDATE lager SET preis = 71 WHERE id = 2"
cursor.execute(sql)
connection.commit()

# SQL-Abfrage
sql = "SELECT * FROM lager WHERE id = 2"
```


🤔 Wie kann man bestimmte Datensätze löschen?

---

### Datensatz löschen

Das Schlüsselwort heisst `DELETE`.

🎬 Ersetzen Sie die SQL-Abfrage mit:

```python
# Datensatz löschen
sql = "DELETE FROM lager WHERE id = 3"
cursor.execute(sql)
connection.commit()

# SQL-Abfrage
sql = "SELECT * FROM lager"
```

⭐ [abfrage.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-10/abfrage.py)

---

### CRUD

Wir haben gerade die CRUD-Operationen angewendet:

* **C**: Create
* **R**: Read
* **U**: Update
* **D**: Delete

---

### Mehr zu SQL

SQL wird von verschiedenen Datenbanksystemen unterstützt.

Wer mehr zu SQL wissen wollt, besucht das [SQL Tutorial](https://www.w3schools.com/sql/).

---

### Aufgaben 1

Lösen Sie die [Aufgaben](excercise10.md#aufgaben) 10.1 und 10.2.

⚡Aufteilung in Gruppen/Breakout-Rooms ⏱️ 10 Minuten

---

### Review

🎯 Wurden die [Lernziele](#lernziele) erreicht?

⚡ Feedback zu den Zielen einholen.

---

### Quellen

[^1]: https://www.sqlite.org/mostdeployed.html