# Übungen Thema 5.5

## Aufgaben

Aufgaben zum Thema.

### Aufgabe 5.5.1: Klasse Getränkeautomat entwerfen

Sie wurden beauftragt eine Software zur Steuerung eines Getränkeautomats zu schreiben. Sie haben sich für die Programmiersprache Python und den objektorientierten Ansatz entschieden. Sie möchten den Getränkeautomat als Klasse abbilden und haben sich folgende Notizen gemacht:

Der Getränkeautomat hat diese Instanzvariablen:

* Ein Dictionary mit den verfügbaren Produkten:

```py
produkte = { 1: "Apfelsaft", 2: "Wasser", 1: "Redbull"}
```

* Ein Dictionary mit dem Bestand:

```py
bestand = { "Apfelsaft": 3, "Wasser": "4", "Redbull": 0}
```

* Ein String mit dem Automatennamen:

```
name = "Gratis"
```

Im Weiteren hat der Automat diese Methoden:

* Die Methode `Auflisten` listet die Produkte auf

```py
for key,value in self.produkte.items():
	print(f"Auswal {key}: {value}")
```

* Die Methode `Ausgeben` erwartet eine Nummer, prüft den Bestand und simuliert eine Ausgabe des Produkts

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
        
    def Afulisten(self):
		...

	...
```

## Aufgabe 5.5.2: Getränkeautomat ausführen

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

## Aufgabe 5.5.3: Klasse Getränkeautomat erweitern

Wir möchten den Namen des Getränkeautomats auch nach der Instanzierung ändern können. Erstellen sie eine Getter- und Setter-Methode für die Instanzvariable `name`.

## Aufgabe 5.5.4: Getränkeautomat ausführen




## Wiederholungsfragen

* **W1**: W1: Erklären Sie den Unterschied zwischen Klasse und Objekt.

<details>
</details>