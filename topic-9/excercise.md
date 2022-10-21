# Übungen Thema 7

## Aufgaben

Aufgaben zum Thema.

### Aufgabe 7.1: Programm aufteilen

Wir erinnern uns an das Kaffeemaschinen-Programm bzw. deren Klasse?

```python
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

Zerlegen Sie das Programm in  ein `Kaffeemaschine.py` und ein `main.py`. Erstere soll den Klassen-Code enthalten und die zweite Datei importiert den Klassen-Code und instanziert das Objekt.

Führen Sie das Programm `main.py` ohne Fehler aus.

## Aufgabe 7.2: Python-Paket verwenden

Sie haben ein Programm `camel.py` und eine `requirements.txt` Datei erhalten.

**requirements.txt**

```
camelcase
```

**camel.py**

```python
import camelcase  
  
c = camelcase.CamelCase()  
txt = "hello world"  
print(c.hump(txt))
```

Die *requirements* Datei enhählt eine Liste der pip-Pakete, die Sie zusätzlich installieren müssen.

Erstellen Sie einen Ordner mit den Dateien und führen Sie auf dem VSCode-Terminal den Befehl `pip install -r requirements.txt` aus. Anschliessend führen Sie das Programm aus.

Was macht die Methode `hump` mit dem Text-Parameter?