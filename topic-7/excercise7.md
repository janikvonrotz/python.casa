# Übungen Thema 7

## Aufgaben

Aufgaben zum Thema.

### Aufgabe 7.1: Klasse Tier entwerfen

Führen Sie diese Anweisungen aus:
* Erstellen Sie eine Klasse mit den Namen `Tier`
* Fügen Sie einen Konstuktor mit diesen Variablen hinzu:
	* Den Namen als `name`
	* Die Hautfarbe als `_farbe`
	* Den Laut des Tieres als `laut`
* Schreiben Sie eine Methode `ausgabe` und geben Sie diesen Satz aus: `"Das {_farbe}e Tier namens {name} macht: {laut}`

⭐ [Klasse Tier entwerfen](https://github.com/janikvonrotz/python.casa/blob/main/topic-7/Klasse%20Tier%20entwerfen.py)

### Aufgabe 7.2: Objekt Tier instanzieren

Rufen Sie ein Tier mit den folgenden Angaben ins Leben:

* Name: Pixel
* Farbe: grau
* Laut: Joink!

Führen Sie die Objekt-Methode `ausgabe` aus.

⭐ [Objekt Tier instanzieren](https://github.com/janikvonrotz/python.casa/blob/main/topic-7/Objekt%20Tier%20instanzieren.py)

### Aufgabe 7.3: Getter und Setter hinzufügen

Erstellen Sie eine Getter- und Setter-Methode für die Eigenschaft `_farbe`. 
Passen Sie die Farbe des Tieres aus der vorhergehenden Aufgabe an und führen Sie erneut die Methode `ausgabe` aus.

⭐ [Getter und Setter hinzufügen](https://github.com/janikvonrotz/python.casa/blob/main/topic-7/Getter%20und%20Setter%20hinzuf%C3%BCgen.py)

### Aufgabe 7.4: Klasse Tier vererben

Vereben Sie Klasse `Tier` zu einer neuen Klasse `Hund`. Die neue Klasse nimmt als zusätzlichen Parameter die Variable `alter` entgegen. Erstellen Sie ein neues Objekt aus der Klasse Hund mit diesen Angaben:

* Name: Dogster
* Farbe: blau
* Laut: Yikes!
* Alter: 37

Führen Sie die Objekt-Methode `ausgabe` aus.

⭐ [Klasse Tier vererben](https://github.com/janikvonrotz/python.casa/blob/main/topic-7/Klasse%20Tier%20verben.py)

### Aufgabe 7.5: Klasse Getränkeautomat entwerfen

Sie wurden beauftragt eine Software zur Steuerung eines Getränkeautomats zu schreiben. Sie haben sich für die Programmiersprache Python und den objektorientierten Ansatz entschieden. Sie möchten den Getränkeautomat als Klasse abbilden und haben sich folgende Notizen gemacht:

Der Getränkeautomat hat diese Instanzvariablen:

Ein Dictionary mit den verfügbaren Produkten:

```python
produkte = { 1: "Apfelsaft", 2: "Wasser", 1: "Redbull"}
```

Ein Dictionary mit dem Bestand:  

```python
bestand = { "Apfelsaft": 3, "Wasser": "4", "Redbull": 0}
```

Ein String mit dem Automatennamen:

```
name = "Gratis"
```

Im Weiteren hat der Automat diese Methoden:

Die Methode `Auflisten` listet die Produkte auf

```python
for key,value in self.produkte.items():
	print(f"Auswal {key}: {value}")
```

Die Methode `Ausgeben` erwartet eine Nummer, prüft den Bestand und simuliert eine Ausgabe des Produkts

```python
bestand = self.bestand[nummer]
if(bestand > 0):
	print(f"Das Produkt {self.produkte[nummer]} wurde ausgeben.")
	self.bestand[nummer] = (bestand - 1)
	print(f"Es sind noch {self.bestand[nummer]} Stk. verfügbar.")
else:
	print("Das gewählte Produkt ist nicht verfügbar.")
```

Fügen Sie die Eigenschaften und Methoden zu einer fertigen Python-Klasse zusammen.

```python
class Getränkeautomat:
    def __init__(self, produkte, ...):
		self.produkte = produkte
        ...
        
    def Auflisten(self):
		...

	...
```

⭐ [Klasse Getränkeautomat entwerfen](https://github.com/janikvonrotz/python.casa/blob/main/topic-7/Klasse%20Getr%C3%A4nkeautomat%20entwerfen.py)

### Aufgabe 7.6: Getränkeautomat ausführen

Sie haben die Python-Klasse für den Getränkeautomat entworfen und können nun die Software ausführen. Instanzieren Sie die Getränkeautomat-Klasse mit den benötigen Parameter. Rufen Sie die beiden Methoden auf und testen Sie den Automaten.

Dazu folgende Inputs:

```python
produkte = { 1: "Apfelsaft", 2: "Wasser", 3: "Redbull"}
bestand = { 1: 3, 2: 4, 3: 0}

automat = Getränkeautomat(produkte, bestand, "Gratis")

automat.Auflisten()
automat.Ausgeben(2)
automat.Ausgeben(3)
```

⭐ [Getränkeautomat ausführen](https://github.com/janikvonrotz/python.casa/blob/main/topic-7/Getr%C3%A4nkeautomat%20ausf%C3%BChren.py)

### Aufgabe 7.7: Klasse Getränkeautomat erweitern

Wir möchten den Namen des Getränkeautomats auch nach der Instanzierung ändern können. Erstellen Sie eine Getter- und Setter-Methode für die Instanzvariable `name`.

```python
@property
def name(self):
	return self._name
```

```python
@name.setter
def name(self, name):
	self._name = name
```

Bennen Sie die Instanzvariable von `name` zu `_name`.

⭐ [Klasse Getränkeautomat erweitern](https://github.com/janikvonrotz/python.casa/blob/main/topic-7/Klasse%20Getr%C3%A4nkeautomat%20erweitern.py)

### Aufgabe 7.8: Getränkeautomat prüfen

Erweitern Sie die Ausgabe der Methode `Auflisten` mit folgendem Code:

```python
print(f"Der Geränkeautomat {self._name} hat dieses Angebot:")
```

Instanzieren Sie die Klasse und rufen Sie die neue Setter-Methode auf.

```python
produkte = { 1: "Redbull", 2: "Redbull", 3: "Redbull"}
bestand = { 1: 3, 2: 4, 3: 0}

automat = Getränkeautomat(produkte, bestand, "Gratis")

automat.Auflisten()
automat.name = "Redbull-o-mat"
automat.Auflisten()
```

Als zusätzliche Aufgaben können Sie Getter- und Setter-Methoden für die Instanzvariablen `produkte` und `bestand` hinzufügen.

⭐ [Getränkeautomat prüfen](https://github.com/janikvonrotz/python.casa/blob/main/topic-7/Getr%C3%A4nkeautomat%20pr%C3%BCfen.py)


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

```python
class MyClass():
def __init__(self, a, b):
    self.a = a
    self.b = b
```

Welche Ausgaben liefern die beiden folgenden print-Funktionen?

```python
obj = MyClass(3, 4)
print(MyClass.a)
print(obj.a)
```

Ist der folgende Code zulässig?

```python
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

```python
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