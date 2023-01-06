# Slides Thema 7
## Objektorientierte Programmierung

[◀️ Thema 7](README.md)

⚡[Anwesenheit bestätigen](https://moodle.medizintechnik-hf.ch/mod/attendance/manage.php?id=8024)

📖 Kapitel 11 Objektorientierte Programmierung

---

### Lernziele

Ich kann ...
* das Idee der objektorientieren Programmierung eklären.
* kann ein Klasse entwickeln.
* kann ein Objekt anhand einer Klasse instanzieren.
* Getter- und Setter-Methoden anwenden.
* die Idee der Klassen-Verberung erläutern.

---

### Code Aufbau

Abhängig von der Projektgrösse muss der Code (Ordner und Dateien) organisiert werden.

Programmierung-Projekte werden mit numehnder Grösse komplexer.

---

### Funktionale Programmierung

Bis jetzt haben wir funktional programmiert.

Unser Code ist Funktionen organisiert.

---

### Objektorientierte Programmierung

Die objektorientierte Programmierung ist weiteres Programmierparadigma.

> Die Grundidee besteht darin, die Architektur einer Software an den Grundstrukturen desjenigen Bereichs der Wirklichkeit auszurichten, der die gegebene Anwendung betrifft.

Python unterstützt auch die objektorientierte Programmierung (OOP).

---

### Daten und Code

Mit OOP bündeln wir Daten (Variablen) und Code (Methoden) in einem Objekt:

![](../oop-class.png)

---

### Objekte und Klassen

Es gibt neue Begriffe.

* **Klasse**: Bauplan oder wie das Objekt aussehen soll
* **Objekt**: Alles ist ein Objekt, beispielsweise Personen, Autos, Bäume, Häuser, Länder, Werkzeuge und Schuhe

---

### Bauplan Auto

Eine Klasse dient als Bauplan für verschiedene Objekte.

![](../car-example.png)

---

### Kaffeemaschine

Im Folgenden wollen wir die Funktionsweise einer Kaffeemaschine mit Code ausdrücken.

---

### Klasse erstellen

Alles beginnt mit `class name:`.

🎬 Erstellen Sie die Datei `Kaffeemaschine.py` mit diesem Inhalt:

```python
class Kaffeemaschine:
```

### Konstruktur hinzufúgen

Jede Python-Klasse braucht einen Konstruktor `def __init__(self, var1, var2, ...):`.

🎬 Fügen Sie den Konstruktor hinzu:

```python
class Kaffeemaschine:
    def __init__(self, marke, anzahl):
        self.marke = marke
        self.anzahl = anzahl
```

ℹ️  Was es mit `self` auf sich hat, kommt weiter unten.

### Methode Zustand hinzufügen

Die Kaffeemaschine zeigt den Bestand an.

🎬 Fügen Sie die Methode `Zustand` hinzu:

```python
class Kaffeemaschine:
    def __init__(self, marke, anzahl):
        self.marke = marke
        self.anzahl = anzahl
    
    def Zustand(self):
        print(f"Ich bin eine {self.marke} Maschine")
        print(f"Es sind noch {self.anzahl} Kaffee(s) verfügbar")
```

### Methode Zustand hinzufügen

Die Kaffeemaschine nimmt Bestellungen entgegen.

🎬 Fügen Sie die Methode `Bestellen` hinzu:

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
```

ℹ️ Wir haben hier den Bauplan für eine Kaffeemaschine. Nun können wir beliebig viele Kaffeemaschinen erstellen.

---

### Objekt instanzieren

Wir rufen anhand des Bauplans eine Kaffeemaschine ins "Leben".

🎬 Fügen Sie diesen Code an:

```python
# Instanzieren
kaffeemaschine = Kaffeemaschine('Nespresso', 3)

# Methoden aufrufen
kaffeemaschine.Bestellen(2)
kaffeemaschine.Zustand()
```

---

### Lebenszyklus eines Objekts

1. Objekt instanzieren
	1. Konstruktor `__init__` aufrufen
2. Objektmethoden aufrufen
3. Objekt löschen (Progamm Ende)

---

### Initialisierung / Konstruktor

Die Initialisierung übernimmt der Konstruktor. Der Konstruktor ist eine Funktion mit dem Namen `__init__`.

```python
def __init__(self, marke, anzahl):
```

---

### Selbstbezug / Instanzvariablen

`self` bezieht sich auf das Objekt (die Instanz) selbst. Die self-Variablen nennt man Instanzvariablen.

```python
self.marke = marke
self.anzahl = anzahl
```

---

### Interaktion / Methoden

Über Methoden interagieren Sie mit dem Objekt.

```python
def Zustand(self):
	print(f"Ich bin eine {self.marke} Maschine")
	print(f"Es sind noch {self.anzahl} Kaffee(s) verfügbar")

def Bestellen(self, anzahl):
	self.anzahl -= anzahl
```

---

### Aufgaben 1

Lösen Sie die [Aufgaben](excercise7.md#aufgaben) 7.1 und 7.2.

⚡Aufteilung in Gruppen/Breakout-Rooms ⏱️ 10 Minuten

---

### Bestehende Python-Klassen

Sie haben bereits bestehende Python-Klassen verwendet. Beispielsweise die Klasse `date`.

```python
from datetime import date
today = date.today()  
```

Dazu der [Klassen-Code in der Python-Bibliothek](https://github.com/python/cpython/blob/86d18019e96167c5ab6f5157fa90598202849904/Lib/datetime.py#L762).

---

### Klassen- und Instanzvariablen

Man unterscheidet zwischen Klassen- und Instanvariablen.

**Instanzvariablen**:  Alle Variablen, denen `self` vorangestellt wird, sind Instanzvariablen.

**Klassenvariablen**: Variablen, die auf Klassenebene definiert werden, gehören zur Klasse, nicht zu einzelnen Objekten

---

### Beispiel Klassen- und Instanzvariablen

```python
class MyClass():  
    magicNumber = 42 # Klassenvariable
    def __init__(self, somedata, otherdata):
        somevar = 123 # lokale Variable
        self.data = somedata # Instanzvariablen
        self.other = otherdata
```

ℹ️ Attribute ist ein Sammelbegriff für Variablen und Methoden von Klassen bzw. Objekten.

---

### Dekoratoren

Dekoratoren werden mit `@` eingeleitet und dienen als Zusatzattribute für Funktionen, Methoden oder Klassen. Sie können die Intention von Code verdeutlichen und Informationen an den Python-Interpreter bzw. -Compiler weitergeben.

```python
@hello
def name():                                                                                                 
    print("Alice")  
```

---

### Beispiel Dekoraten

🎬  Erstellen Sie eine Datei `Dekoraten.py`, fügen Sie den Code von unten ein.

```python
# Dekoraten-Funktion
def hello(func):                                                                                            
    def inner():                                                                                            
        print("Hello ")                                                                                     
        func()                                                                                              
    return inner                                                                                 

# Funktion wird mit Dekorator erweitert
@hello
def name():                                                                                                 
    print("Alice")                                                                                          

name()
```

ℹ️ Durch das "dekorieren" einer Methode ändert man die "Wirkung".

---

### Getter- und Setter-Methoden

Der Konstruktor wird nur einmal ausgeführt. Bestimmte Variabeln kann man nicht mehr ändern. Mit Getter- und Setter-Methoden ermöglicht man den Zugriff auf diese Variablen.

```python
class Kaffeemaschine:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
```

ℹ️ Offensichtlich kommen hier Dekoratoren zum Einsatz.

---

### Beispiel Getter und Setter

🎬  Erstellen Sie eine Datei `Getter-Setter.py` und instanzieren Sie die Klasse von vorhin wie folgt:

```python
maschine = Kaffeemaschine("Jura")
print(maschine.name)
maschine.name = "Gaccia"
print(maschine.name)
```

---

### Vererbung

Dieses Thema werden wir nur anschneiden.

Klassen können vererbt werden. Das heisst Sie erhalten einen neuen Namen und zusätzliche Attribute.

![](../vererbung-tier.png)

---

### Beispiel Vererbung

In der Definition der Klasse kann die darüberliegende Superklasse angegeben werden. Bei der Initialisierung ruft man den Konstruktor der Superklasse auf.

```python
class Tier():
    def __init__(self, name, farbe, alter):
        self.rufname = name
        self.farbe   = farbe
        self.alter   = alter

class Katze(Tier): # Katze ist ein Tier
    def __init__(self, rufname, farbe, alter):
        super().__init__(rufname, farbe, alter) # Aufruf Konstruktor von Tier

katze = Katze("Sammy", "orange", 3)
print(katze.farbe)
```

---

### super() Funktion

Mit `super()` greift man auf die Instanz der Superklasse zu.

Beim Instanzieren der Klasse Katze wird damit der Konstruktur der Klasse Tief aufgerufen.

---

### Hierarchie

Beim Vererben der Klassen entsteht eine Hierarchie.

![](../hierarchie.png)

---

### Aufgaben 2

Lösen Sie die [Aufgaben](excercise7.md#aufgaben) 7.3 und 7.4.

⚡Aufteilung in Gruppen/Breakout-Rooms ⏱️ 10 Minuten

---

### Review

🎯 Wurden die [Lernziele](#lernziele) erreicht?

⚡ Feedback zu den Zielen einholen.
