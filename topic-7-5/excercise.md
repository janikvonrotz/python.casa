# Übungen Thema 7.5

## Aufgaben

Aufgaben zum Thema.

### Aufgabe 7.5.1: Datenbank auslesen und sortieren

Wir erinnern uns an das Kaffeemaschinen-Programm bzw. deren Klasse?

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

# Instanzieren
kaffeemaschine = Kaffeemaschine('Nespresso', 3)

# Methoden aufrufen
kaffeemaschine.Bestellen(2)
kaffeemaschine.Zustand()
```

Zerlegen sie das Programm in  ein `Kaffeemaschine.py` und ein `main.py`. Erstere soll den Klassen-Code enthalten und die zweite Datei importiert den Klassen-Code und instanziert das Objekt.

Führen sie das Programm `main.py` ohne Fehler aus.

## Aufgabe 7.5.2: Abfrage mit Input

```python
# Eingabe Teil des Namens
eingabe = input("Bitte den gesuchten Namensteil eingeben: ")
sql = "SELECT * FROM personen WHERE name LIKE ?"
eingabe = '%' + eingabe + '%'
```





```python
sql = "SELECT * FROM personen ORDER BY name, vorname"
```