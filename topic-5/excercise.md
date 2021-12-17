# Übungen Thema 5

## Aufgaben

Aufgaben zum Thema.

### Aufgabe 5.1: Vereinfachen mit Funktion

Für die Ansage von Zugabfahren wurde ein Programm erstellt.

```py
print("Der nächste Zug fährt nach Bern.")
print("Der nächste Zug fährt nach Luzern.")
print("Der nächste Zug fährt nach Zürch.")
print("Der nächste Zug fährt nach Genf.")
print("Der nächste Zug fährt nach Chur.")
```

Es wird immer der gleiche Satz verwendet, nur der Name des Zuges ändert. Versuchen sie dieses Programm mit einer Funktion zu vereinfachen.

::: tip
Erstelle sie eine Funktion `ansage`, die als Parameter den Ort erhält und rufen sie die Funktion wie folgt auf:

```py
print(ansage("Bern"))
print(ansage("Luzern"))
print(ansage("Zürich"))
print(ansage("Genf"))
print(ansage("Chur"))
```
:::

### Aufgabe 5.2: Vereinfachen mit Schleife

Unser Programm kann noch verbessert werden. Erstellen sie eine Liste der Orte und übergeben sie diese Parameter an die Ansage-Funktion.

### Aufgabe 5.3: Parameter validieren

Wir möchten sicherstellen, dass die Ansage-Funktion nur Variablen vom Typ `str` verarbeitet. Erstellen sie eine entsprechende Prüfung vor der Ausgabe.

### Aufgabe 5.4: Quersumme berechhen

Schreibe eine Funktion `quersumme(zahl)`, welche die Quersumme von `zahl` berechnet und zurückgibt.

::: tip
Wenn man die Zahl in einen String umwandelt kann man sie in einer Schleife verarbeiten.
:::

### Aufgabe 5.5: Rekursion auf der Festplatte

Schreiben sie eine rekursive Funktion, die als Parameter einen Ordnerpfad erwartet und alle Unterordner ausgibt.

::: tip
Dazu eine Hilfestellung. Das folgende Programm gibt alle Dateien und Ordner unterhalb eines bestimmten Ordnerpfads aus:

```py
import os

basepath = '/pfad/to/my/directory'

for entry in os.listdir(basepath):

	fullpath = os.path.join(path, entry)

    if os.path.isfile(fullpath):
        print("Datei: ", entry)
		
    if os.path.isdir(fullpath):
        print("Ordner:", entry)
```
:::

### Aufgabe 5.6: Filtern mit Lambda

Kopieren sie die Datenstruktur von <https://jsonplaceholder.typicode.com/users> nach Python.

![kopieren-daten-jsonplaceholder](../kopieren-daten-jsonplaceholder.gif)

Filter sind alle Benutzer aus der Liste, die eine Telefonnumer haben, die mit einer `1` beginnt. Verwenden sie dazu eine Lambda-Funktion.

::: tip
Verwenden sie die folgende Bausteine:

```py
print(user.get('email'))
```

```py
for user in users:
```

```py
filter(lambda user: user["name"] == "Leanne Graham", data)
```

```py
users = list(filter)
```
:::

### Aufgabe 5.7: Chart to Code

Schreiben sie diese Flowchart als Code:

![diagram](../diagram.svg)

### Aufgabe 5.8: Code to Chart

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

### Aufgabe 5.9: Hangman

Entwickeln sie das Spiel *Hangman*. Implementierung sie dazu folgende Punkte:
* Zu Finden des Worts hat man 5 Versuche
* Das zu suchende Wort wird in Grossbuchstaben umgewandelt
* Der eingegebene Buchstabe wird in Grossbuchstaben umgewandelt
* Das zu suchende Wort wird als Liste gespeichert

::: tip

Als Anschub haben wir die folgenden Bausteine:

```py
wort = list("python".upper())
laenge = len(wort)
zensiert = list(laenge * '_')
versuche = 5
gefunden = []
gewonnen = False
```

```py
if eingabe in wort:
        gefunden.extend([eingabe])
```

```py
while versuche > 0  and not gewonnen:
    eingabe = input("Geben sie einen Buchstaben ein: ").upper()
```

```py
for i in range(0, laenge):
	if wort[i] in gefunden:
		zensiert[i] = wort[i]
```

```py
if '_' not in zensiert:
	gewonnen = True
	print("Du hast gewonnen!")
```

```py
if not gewonnen:
    print("Du hast verloren!")
```
:::

## Wiederholungsfragen

* **W1**: Die in Python vordefinierten Funktionen min und max ermitteln das kleinste bzw. größte Element einer Liste. Programmieren Sie die Funktion minmax, die die beiden entsprechenden Elemente als Tupel zurückgibt – natürlich, ohne auf min und max zurückzugreifen.

<details>
Die triviale Lösung zur Aufgabenstellung greift auf die vorgegebenen min- und max-Funktionen zurück und gibt die beiden Ergebnisse als Tupel zurück:
<pre>
def minmax(lst):   
    return min(lst), max(lst)
</pre>
Wenn Sie die Funktion selbst implementieren, müssen Sie in einer Schleife alle Elemente der Liste durchlaufen – das ist Ihnen vermutlich klar. Schwierig ist es, Startwerte für die beiden Ergebnisvariablen min und max zu wählen. Sie könnten für min eine sehr große und für max eine sehr kleine Zahl nehmen (min=100000 und max=-100000). Wenn die Liste dann allerdings noch kleinere oder noch größere Werte enthält, erhalten Sie ein falsches Ergebnis.
Auf der sicheren Seite sind Sie, wenn Sie als Startwerte einfach das jeweils erste Element der Liste verwenden. Wenn Sie Glück haben, ist das schon das Endergebnis. Wenn nicht, werden min bzw. max in der for-Schleife immer wieder korrigiert, bis die beiden Variablen schließlich den kleinsten bzw. größten Wert enthalten.
<pre>
# Beispieldatei minmax.py  
def minmax(lst):   
    min = lst[0]   
    max = lst[0]      
    for itm in lst:   
        if itm < min:   
            min = itm   
        if itm > max:   
            max = itm   
    return (min, max)  # Tupel zurückgeben
</pre>
</details>

* **W2**: Ein Palindrom ist ein Text, der von vorn und hinten gelesen den gleichen Inhalt hat – z. B. "Lagerregal" oder "Trug Tim eine so helle Hose nie mit Gurt?"". Leer- und Satzzeichen werden dabei ignoriert. Weitere Beispiele finden Sie hier: <https://de.wikipedia.org/wiki/Palindrom>. Schreiben Sie eine Funktion, die testet, ob eine Zeichenkette ein Palindrom ist. Tipp: Verwenden Sie die Funktion str.isalpha, um zu testen, ob ein Zeichen ein Buchstabe ist.

<details>
Die Lösungsfunktion wandelt die übergebene Zeichenkette zuerst in Kleinbuchstaben um und bildet daraus eine Liste. Aus dieser Liste filtert sie nun mit isalpha alle Buchstaben heraus und eliminiert so Leer- und Satzzeichen. join bildet aus den verbliebenen Listenelementen wieder eine Zeichenkette. Als Rückgabeergebnis gilt der Test, ob diese Zeichenkette identisch ist mit einer Zeichenkette in umgekehrter Reihenfolge (Slicing-Notation [::-1]).
<pre>
# Beispieldatei palindrom.py  
def palindrom(s):          
    lst = list(s.lower())  
    plainlst = filter(str.isalpha, lst)        
    plain = ''.join(plainlst)     
    return plain == plain[::-1]
</pre>
</details>

* **W3**: Die Python-Funktion sum(a, b, c) berechnet die Summe aller übergebenen Parameter. Schreiben Sie eine äquivalente Funktion prod, die alle Parameter multipliziert.

<details>
Der entscheidende Punkt bei dieser Aufgabe ist die variable Parameteranzahl, die Sie in der Schreibweise *para realisieren. Innerhalb der Funktion können Sie auf die übergebenen Elemente in Form einer Liste zugreifen. Davon ausgehend gibt es mehrere Lösungsvarianten. Am naheliegendsten ist die Programmierung einer Schleife. Dabei wird der erste Parameter in der lokalen Variablen result gespeichert und in der Folge mit allen weiteren Parametern (Slicing-Notation [:1]) multipliziert.
<pre>
# Beispieldatei prod.py  
def prod(*f):  
    result = f[0]  
    for factor in f[1:]:  
        result = result * factor  
    return result
</pre>
»Schöner« wird der Code (zumindest in Python-Denkweise), wenn Sie die reduce-Funktion anwenden. An reduce müssen Sie eine Lambda-Funktion übergeben, die die Multiplikation durchführt:
<pre>
from functools import reduce  
def prod(*f):  
    if len(f)<2:  
        return f[0]  
    else:  
        return reduce(lambda x, y: x*y, f)
Auf die Lambda-Funktion können Sie verzichten, wenn Sie wissen, dass sie alle Python-Operatoren im operator-Modul auch als Funktionen zur Verfügung stehen:
import operator  
def prod(*f):  
    if len(f)<2:  
        return f[0]  
    else:  
        return reduce(operator.mul, f)
</pre>
</details>

* **W4**: Schreiben Sie eine Funktion, die eine Zeichenkette nach allen Vorkommen einer anderen Zeichenkette durchsucht und die Startpositionen als Liste zurückgibt. Beispiel:

```py
print(findAll('abcefgabcxyzabcd', 'abc'))
# Ausgabe: [0, 6, 12]
```

<details>
findAll sucht zuerst nach dem ersten Vorkommen von pattern in s. Wenn es eines gibt, also pos einen Wert ungleich –1 enthält, wird dieser Wert in der while-Schleife dem Ergebnis hinzugefügt. Danach wird die Suche an der Stelle pos+1 fortgesetzt.
<pre>
# Beispieldatei findall.py  
def findAll(s, pattern):  
    matches = []  
    pos = s.find(pattern)  
    while pos != -1:  
        matches += [pos]  
        pos = s.find(pattern, pos+1)  
    return matches
	</pre>
</details>