# Übungen Thema 4

## Aufgaben

Aufgaben zum Thema.

### Aufgabe 4.1

### Aufgabe 4.2

### Aufgabe 4.3

Das folgende Programm benutzt zwei geschachtelte if Verzweigungen. Schreibe das Programm um, so dass es mit einer einzelnen Verzweigung auskommt:

```py
zahl = int(input("Gib eine Zahl ein: "))
   
if zahl % 2 == 0:
    if zahl % 3 == 0:
        print("Die eingegebene Zahl ist durch drei und zwei teilbar.")
    else:
        print("Die eingegebene Zahl ist nicht durch drei und zwei teilbar.")
else:
    print("Die eingegebene Zahl ist nicht durch drei und zwei teilbar.")
```

### Aufgabe Password-Check

Sicheres Password prüfen.

## Wiederholungsfragen

* W1: Versuchen Sie, drei unterschiedliche Wege zu finden, eine Liste mit den Vielfachen von 7 zu bilden, die kleiner als 100 sind (also [7, 14, ..., 98]).
* W2: Extrahieren Sie aus der Zeichenkette Hello, World! alle Vokale und verbinden Sie diese zu einer neuen Zeichenkette.
* W3: Welchen Datentyp verwenden Sie, um Lottozahlen zu speichern?
* W4: Entfernen Sie die Doppelgänger aus einer Liste von Zahlen, z. B. aus [1, 2, 3, 2, 7, 3, 9]. Die Ergebnisliste soll aufsteigend sortiert sein.
* W5: Erstellen Sie ein kleines Deutsch-Englisch-Wörterbuch für Zahlen. Beispielsweise soll woerter['eins'] die englische Bezeichnung 'one' liefern.
* W6: Ermitteln Sie die maximale Wortlänge in der folgenden Zeichenkette (siehe http://www.loremipsum.de):

```
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, ...
```