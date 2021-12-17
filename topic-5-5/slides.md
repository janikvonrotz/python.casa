

### Begriffe


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

### Abschluss

Ich hoffe das war nicht viel! Nun habt ihr die wichtigsten Element der Programmierung mit Python gelernt.

Jetzt heisst es anwenden!

---
