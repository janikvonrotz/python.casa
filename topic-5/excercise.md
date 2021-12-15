# Übungen Thema 5

## Aufgaben

Aufgaben zum Thema.

### Aufgabe 5.1: Quersumme

Schreibe eine Funktion `quersumme(zahl)`, welche die Quersumme von `zahl` berechnet und zurückgibt.

::: tip
Wenn man die Zahl in einen String umwandelt kann man sie in einer Schleife verarbeiten.
:::

### Aufgabe 5.2: Rekursion auf der Festplatte

Schreiben sie eine rekursive Funktion, die als Parameter einen Ordnerpfad erwartet und alle Unterordner ausgibt.

Dazu eine Hilfestellung:

```py
import os
# List all files in a directory using os.listdir
basepath = 'my_directory/'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)
```

### Aufgabe 5.3: Chart to Code

Schreiben sie diese Flowchart als Code:

![diagram](../diagram.svg)

### Aufgabe 5.4: Code to Chart

Erstellen sie einen Flowchart mit [draw.io](https://draw.io) anhand dieses Codes:

```py
spicyfood = input("Do you like spicy food? True or False?")
if spicyfood == "True":
    level = input("How spicy do you like it? hot, very hot, super hot ?")
    if level == "super hot":
        print(f"The user likes {level} spicy food!")
    else:
        print("The user likes spicy food!")
if spicyfood == "False":
    print("The user hates spicy food!")
```

## Wiederholungsfragen

* **W1**: Die in Python vordefinierten Funktionen min und max ermitteln das kleinste bzw. größte Element einer Liste. Programmieren Sie die Funktion minmax, die die beiden entsprechenden Elemente als Tupel zurückgibt – natürlich, ohne auf min und max zurückzugreifen.

<details>
</details>

* **W2**: Ein Palindrom ist ein Text, der von vorn und hinten gelesen den gleichen Inhalt hat – z. B. "Lagerregal" oder "Trug Tim eine so helle Hose nie mit Gurt?"". Leer- und Satzzeichen werden dabei ignoriert. Weitere Beispiele finden Sie hier: <https://de.wikipedia.org/wiki/Palindrom>. Schreiben Sie eine Funktion, die testet, ob eine Zeichenkette ein Palindrom ist. Tipp: Verwenden Sie die Funktion str.isalpha, um zu testen, ob ein Zeichen ein Buchstabe ist.

<details>
</details>

* **W3**: Die Python-Funktion sum(a, b, c) berechnet die Summe aller übergebenen Parameter. Schreiben Sie eine äquivalente Funktion prod, die alle Parameter multipliziert.

<details>
</details>

* **W4**: Schreiben Sie eine Funktion, die eine Zeichenkette nach allen Vorkommen einer anderen Zeichenkette durchsucht und die Startpositionen als Liste zurückgibt. Beispiel:

```py
print(findAll('abcefgabcxyzabcd', 'abc'))
# Ausgabe: [0, 6, 12]
```

<details>
</details>