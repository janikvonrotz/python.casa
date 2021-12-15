# Übungen Thema 4

## Aufgaben

Aufgaben zum Thema.

### Aufgabe 4.1: Listenkonfusion

Lies das folgende Programm und versuche zu erraten, was die Ausgabe ist. Probiere es anschliessend aus und suche nach einer Erklärung des Verhaltens.

```py
liste_a = ['Hallo', 'schönes', 'Wetter']
liste_b = liste_a

liste_b[1] = 'schlechtes'

print(liste_a[0], liste_a[1], liste_a[2])  
```

Das Verhalten dieses Programms ist der Grund, warum wir uns in Python Variablen nicht als Speicherplätze sondern als Namensschilder für Objekte vorstellen. Kannst du dies erklären?

### Aufgabe 4.2: Listen verstehen

Speichere die Elemente `'Schwalbe'`, `'Kokosnuss'`, `13`, `'Spam'` und `3.14` in einer Liste mit dem Namen `liste` ab und versuche zu verstehen was die folgenden Methoden machen.

```py
liste[2] = 666
len(liste)
liste.append('Ni')
liste.extend([4, 5, 3.14])
liste.insert(2, 'Taube')
liste.count(3.14)
liste.index(3.14)
liste.remove(3.14)
liste.pop()
liste.reverse()
sum([1,3,5])
```

### Aufgabe 4.3: Minimum und Maximum

Schreibe ein Programm, welches vom Benutzer 10 Zahlen einliest und diese in einer Liste speichert. Anschliessend soll das Minimum und das Maximum der Zahlen aus der liste bestimmt und ausgegeben werden.

::: tip
Die folgenden Elemente sollten weiterhelfen:

```py
# Eine leere Listeerstellen
liste = []
```

```py
# Zahl eingeben
zahl = input("Eingabe: ")
```

```py
# Schleife von 1 bis 4
for i in range(1,5):
    print(i)
```

```py
# Kleinste Zahl aus Liste ausgeben
min([1,3,2])
```
:::

### Aufgabe 4.4: Zoo

Gegeben ist der folgende Anfang eines Programms:

```py
animals = ["tiger", "mouse", "bird", "python", "elephant", "monkey"]
```

Ergänze das Programm so, dass für jedes Tier aus der Liste animals der Satz "… ist ein Tier" in der Konsole ausgegeben wird. Benutze dafür die print() Funktion.

### Aufgabe 4.5: Ohne for-Schleife

Schreibe ein Programm, welches alle Zahlen von 1 bis 100 auf den Bildschirm schreibt, ohne dafür eine for-Schleife zu verwenden.

### Aufgabe 4.6: Euklid

Schreibe ein Programm, welches mit `input()` zwei Zahlen vom Benutzer einliest und den grössten gemeinsamen Teiler der beiden Zahlen mit`print()` ausgibt.
    
Dazu kannst du den Euklidischen Algorithmus benutzen. Mehr dazu findest du hier: <https://de.wikipedia.org/wiki/Euklidischer_Algorithmus>.

## Wiederholungsfragen

* **W1**: Versuchen Sie, drei unterschiedliche Wege zu finden, eine Liste mit den Vielfachen von 7 zu bilden, die kleiner als 100 sind (also [7, 14, ..., 98]).

<details>
</details>

* **W2**: Extrahieren Sie aus der Zeichenkette Hello, World! alle Vokale und verbinden Sie diese zu einer neuen Zeichenkette.

<details>
</details>

* **W3**: Welchen Datentyp verwenden Sie, um Lottozahlen zu speichern?

<details>
</details>

* **W4**: Entfernen Sie die Doppelgänger aus einer Liste von Zahlen, z. B. aus [1, 2, 3, 2, 7, 3, 9]. Die Ergebnisliste soll aufsteigend sortiert sein.

<details>
</details>

* **W5**: Erstellen Sie ein kleines Deutsch-Englisch-Wörterbuch für Zahlen. Beispielsweise soll woerter['eins'] die englische Bezeichnung 'one' liefern.

<details>
</details>

* **W6**: Ermitteln Sie die maximale Wortlänge in der folgenden Zeichenkette (siehe http://www.loremipsum.de):

```
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, ...
```

<details>
</details>

* **W7**: Berechnen Sie die Fakultät der Zahlen von 1 bis 20. (Die Fakultät ist als das Produkt aller Zahlen bis n definiert. Die Fakultät von 6 ist also 1×2×3×4×5×6 = 720.)

<details>
</details>

* **W8**: Berechnen Sie die Summe der Funktion 1/x^2, wenn Sie für x alle Zahlen zwischen 2 und 30 einsetzen.

<details>
</details>

*   **W9**: Was wird bei der Ausführung des folgenden Codes ausgegeben?

```py
for i in range(1, 3):
    for j in range(i):
        print(i+j)
```

<details>
</details>

* **W10**: Schreiben Sie eine while-Schleife, die in 5er-Schritten von 100 bis 0 zählt.

<details>
</details>

* **W11**: Formulieren Sie eine Schleife, um den Wertebereich zwischen 125 und 160 in elf Schritten zu durchlaufen. Das Programm soll alle elf Zahlen ausgeben, beginnend mit 125,0 und endend mit 160,0.

<details>
</details>