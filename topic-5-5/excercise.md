# Übungen Thema 5.5

## Aufgaben

Aufgaben zum Thema.

### Aufgabe 5.5.1: Klasse Getränkeautomat entwerfen

Sie wurden beauftragt eine Software zur Steuerung eines Getränkeautomats zu schreiben. Sie haben sich für die Programmiersprache Python und den objektorientierten Ansatz entschieden. Sie möchten den Getränkeautomat als Klasse abbilden und haben sich folgende Notizen gemacht:

Der Getränkeautomat hat diese Instanzvariablen:

Ein Dictionary mit den verfügbaren Produkten:

```py
produkte = { 1: "Apfelsaft", 2: "Wasser", 1: "Redbull"}
```

Ein Dictionary mit dem Bestand:  

```py
bestand = { "Apfelsaft": 3, "Wasser": "4", "Redbull": 0}
```

Ein String mit dem Automatennamen:

```
name = "Gratis"
```

Im Weiteren hat der Automat diese Methoden:

Die Methode `Auflisten` listet die Produkte auf

```py
for key,value in self.produkte.items():
	print(f"Auswal {key}: {value}")
```

Die Methode `Ausgeben` erwartet eine Nummer, prüft den Bestand und simuliert eine Ausgabe des Produkts

```py
bestand = self.bestand[nummer]
if(bestand > 0):
	print(f"Das Produkt {self.produkte[nummer]} wurde ausgeben.")
	self.bestand[nummer] = (bestand - 1)
	print(f"Es sind noch {self.bestand[nummer]} Stk. verfügbar.")
else:
	print("Das gewählte Produkt ist nicht verfügbar.")
```

Fügen sie die Eigenschaften und Methoden zu einer fertigen Python-Klasse zusammen.

```py
class Getränkeautomat:
    def __init__(self, produkte, ...):
		self.produkte = produkte
        ...
        
    def Auflisten(self):
		...

	...
```

### Aufgabe 5.5.2: Getränkeautomat ausführen

Sie haben die Python-Klasse für den Getränkeautomat entworf und können nun die Software ausführen. Instanzieren sie die Getränkeautomat-Klasse mit den benötigen Parameter. Rufen sie die beiden Methoden auf und testen sie den Automaten.

Dazu folgende Inputs:

```py
produkte = { 1: "Apfelsaft", 2: "Wasser", 3: "Redbull"}
bestand = { 1: 3, 2: 4, 3: 0}

automat = Getränkeautomat(produkte, bestand, "Gratis")

automat.Auflisten()
automat.Ausgabe(2)
automat.Ausgabe(3)
```

### Aufgabe 5.5.3: Klasse Getränkeautomat erweitern

Wir möchten den Namen des Getränkeautomats auch nach der Instanzierung ändern können. Erstellen sie eine Getter- und Setter-Methode für die Instanzvariable `name`.

```py
@property
def name(self):
	return self._name
```

```py
@name.setter
def name(self, name):
	self._name = name
```

### Aufgabe 5.5.4: Getränkeautomat ausführen

Erweitern sie die Ausgabe der Methode `Auflisten` mit folgendem Code:

```py
print(f"Der Geränkeautomat {self._name} hat dieses Angebot:")
```

Instanzieren sie die Klasse und rufen sie die neue Setter-Methode auf.

```py
produkte = { 1: "Redbull", 2: "Redbull", 3: "Redbull"}
bestand = { 1: 3, 2: 4, 3: 0}

automat = Getränkeautomat(produkte, bestand, "Gratis")

automat.Auflisten()
automat.name = "Redbull-o-mat"
automat.Auflisten()
```

Als zusätzliche Aufgaben können sie Getter- und Setter-Methoden für die Instanzvariablen `produkte` und `bestand` hinzufügen.

## Wiederholungsfragen

**W1**: W1: Erklären Sie den Unterschied zwischen Klasse und Objekt.

<details>
Grundsätzlich gibt der Code einer Klasse vor, welche Funktionen die Klasse erfüllt, das heißt, welche Variablen und Methoden es gibt. Wenn Sie so wollen, ist die Klasse ein Bauplan.

Objekte werden von der Klasse abgeleitet. Wenn Sie also eine Auto-Klasse programmiert haben, können Sie im laufenden Programm daraus unzählige Auto-Objekte erzeugen. Anstelle von Objekten sind auch die Begriffe Instanz oder Exemplar üblich.

Python ist insofern ein Sonderfall, als auch die Klasse an sich als Objekt gilt.
</details>

**W2**: Wozu dient der Konstruktor? Wie lautet sein interner Name, wie wird er aufgerufen?

<details>
Die Aufgabe des Konstruktors besteht darin, die Daten (Instanzvariablen) eines neuen Objekts zu initialisieren. Oft werden im Konstruktor auch die übergebenen Parameter daraufhin überprüft, ob es sich um sinnvolle Daten handelt. Ist das nicht der Fall, kann ein Fehler ausgelöst werden.

Innerhalb der Klasse wird der Konstruktor als spezielle Methode mit dem Namen __init__ implementiert. Der erste Parameter lautet immer self und gibt Zugriff auf die neue Objektinstanz.

Zum Aufruf des Konstruktors kommt es, wenn Sie ein Objekt erzeugen, also var = MyClass(parameter) aufrufen.
</details>

**W3**: Die folgende Klasse sei gegeben:

```py
class MyClass():
def __init__(self, a, b):
    self.a = a
    self.b = b
```

Welche Ausgaben liefern die beiden folgenden print-Funktionen?

```py
obj = MyClass(3, 4)
print(MyClass.a)
print(obj.a)
```

Ist der folgende Code zulässig?

```py
obj.c = 7
print(obj.c)
```

<details>
MyClass.a ist nicht zulässig. a ist eine Instanzvariable, der Zugriff kann nur über ein Objekt erfolgen.
<pre>
# Beispieldatei instancevar.py
obj = MyClass(3, 4)
print(MyClass.a)  # Fehler, MyClass hat kein Attribut 'a'
print(obj.a)      # Ausgabe 3
</pre>
Im Gegensatz zu den meisten anderen Programmiersprachen sind Objekte zur Laufzeit um zusätzliche Attribute (also Variablen und Methoden) erweiterbar. Daher funktioniert dieser Code ohne Probleme:
<pre>
obj.c = 7
print(obj.c)       # Ausgabe 7
</pre>
</details>

**W4**: Entwerfen Sie den Code für eine Bankkontoklasse, die sich wie folgt nutzen lässt:

```py
k1 = Konto('Michael', 200, 0)
k2 = Konto('Maria')
k3 = Konto('Peter', 1000, 500)
k1.einzahlen(100)
if k2.abheben(100):
	print('Geld von Konto 2 abgehoben')
if k3.abheben(1200):
	print('Geld von Konto 3 abgehoben')
for k in [k1, k2, k3]: 
	print(k)
```

<details>
Die Klasse für ein Bankkonto kann z. B. so aussehen:
<pre>
# Beispieldatei konto.py
class Konto():  
    # Konstruktor
    def __init__(self, name, startguthaben=0, rahmen=0):
        # private Instanzvariablen
        self.__name = name
        self.__guthaben = startguthaben
        self.__rahmen = rahmen

    # Instanzmethoden
    def einzahlen(self, betrag):
        if betrag<=0:
            raise ValueError('Ungültige Parameter!')
        self.__guthaben += betrag    

    def abheben(self, betrag):
        if betrag<=0:
            raise ValueError('Ungültige Parameter!')
        if betrag > self.__guthaben + self.__rahmen:
            print('Zu wenig Geld auf dem Konto.')  
            return False
        else:
            self.__guthaben -= betrag   
            return True

    # Objekt ausgeben
    def __str__(self):
        s = 'Konto von %s:\n  Guthaben: %d\n' + \
            '  Überziehungsrahmen: %d\n'
        return s % (self.__name, self.__guthaben, 
                    self.__rahmen)   
</pre>
</details>