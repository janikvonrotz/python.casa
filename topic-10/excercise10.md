# Übungen Thema 10

## Aufgaben

Aufgaben zum Thema.

Danke an Hari Thavachchelvam für die Idee zur Aufgabenstellung. 

### Aufgabe 10.1: Datenbank auslesen und sortieren

Laden Sie als erstes die Datei [`quiz.db`](https://raw.githubusercontent.com/janikvonrotz/python.casa/main/topic-10/quiz.db) herunter und speichern Sie es in einem Ordner. Erstellen Sie die Datei `quiz.py` im selben Ordner.

Schauen Sie sich die Datenbank mit VSCode an und beantworten Sie diese Fragen:
* Wieviele Datensätze gibt es?
* Welche Spalte identifiziert die Datensätze eindeutig und wie heisst diese?
* Welcher Datentyp hat diese Spalte?

Erstellen Sie nun ein Progamm um einen bestimmten Datensatz auszulesen. Ergänzen Sie dazu die Markierungen `?????` im folgenden Code:

```python
import sqlite3

# Verbindung, Cursor
connection = sqlite3.connect("?????.db")
cursor = connection.cursor()

# SQL-Abfrage
sql = "SELECT * FROM questions WHERE ????? = 403"

# Absenden der SQL-Abfrage und Empfang des Ergebnis
cursor.execute(sql)

# Ausgabe des Ergebnis
for datensatz in cursor:
    print("Frage: ", datensatz[1])
    print("Antworten: ", ', '.join(datensatz[2:6]))

# Verbindung beenden
connection.close()
```

⭐ [Datenbank auslesen und sortieren](https://github.com/janikvonrotz/python.casa/blob/main/topic-10/Datenbank%20auslesen%20und%20sortieren.py)

### Aufgabe 10.2: Abfrage mit Input

Mit dem `input` Befehl können wir nach einer bestimmten Frage-ID und Antwort-Nummer fragen. Erweitern Sie das Skript aus der vorhergehenden Aufgabe mit dem Befehl.

Dazu diese Inputs:

```python
# SQL-Abfrage mit Eingabe
frage = input("Bitte geben Sie eine Frage-ID ein: ")
sql = "SELECT * FROM questions WHERE questionID = " + frage
```

```python
	# Eingabe Antwort
    antwort = input("Ihre Antwort 1-4: ")
```

```python
    # Ausgabe korrekt/falsch
    korrekt = str(datensatz[6])
    if korrekt == antwort:
        print("\nDie Antwort ist korrekt!\n")
    else:
        print("\nDie Antwort ist falsch!\n")
```

⭐ [Abfrage mit Input](https://github.com/janikvonrotz/python.casa/blob/main/topic-10/Abfrage%20mit%20Input.py)

**Zusatzaufgabe**

Können Sie das Programm in einer Schleife schalten, bis man die richtige Antwort gefunden hat?

Erstellen Sie eine eine Frage-ID nach Zufall und filtern Sie verfügbaren Fragen anhand des Schwierigkeits-Grades.
