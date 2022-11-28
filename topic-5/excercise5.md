# Übungen Thema 5

## Aufgaben

Aufgaben zum Thema.

### Aufgabe 5.1: Liste deklarieren

Erstellen Sie eine Liste mit allen 12 Monaten.

```python
monate = ['Januar', 'Feburar', ...]
```

Und geben Sie den den zehnten Monat aus. Was müssen Sie für `?` einsetzen?

```python
print(monate[?])
```

⭐ [Monate.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-5/Monate.py)

### Aufgabe 5.2: Listen kombinieren

Sie erhalten diese Liste:

```python
arbeitstage = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag']
```

Und diese Liste:

```python
wochenende = ['Samstag', 'Sonntag']
```

Kombinieren Sie die beiden Listen zu einer neuen Liste `woche` mithilfe der `extend`-Methode und geben Sie den Inhalt der Liste aus.

⭐ [ListeKombinieren.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-5/ListeKombinieren.py)

### Aufgabe 5.3: Listenkonfusion

Lies das folgende Programm und versuche zu erraten, was die Ausgabe ist. Probiere es anschliessend aus und suche nach einer Erklärung des Verhaltens.

```python
a = ['Hallo', 'schönes', 'Wetter']
b = a

b[1] = 'schlechtes'

print(a[0], a[1], a[2])  
```

Das Verhalten dieses Programms ist der Grund, warum wir uns in Python Variablen nicht als Speicherplätze sondern als Namensschilder für Objekte vorstellen. Kannst du dies erklären?

### Aufgabe 5.4: Listen verstehen

Speicheren Sie die Elemente `'Schwalbe'`, `'Kokosnuss'`, `13`, `'Spam'` und `3.14` in einer Liste mit dem Namen `liste` ab und versuchen zu verstehen was die folgenden Methoden machen. Verwenden Sie dazu den Python-Debugger.

```python
liste[2] = 666
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

⭐ [ListenMethoden.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-5/ListenMethoden.py)

### Aufgabe 5.5: Duplikate entfernen

Sie erhalten eine Liste von Programmiersprachen:

```python
lang = ['Java', 'Python', 'Java', 'C++', 'C', 'C#', 'JavaScript', 'Python', 'Go', 'Swift', 'Go', 'PHP', 'C']
```

Diese Liste enthält Duplikate und ist nicht sortiert. Um das zu verbesseren gehen Sie wie folgt vor:
* Wandeln Sie die Liste mit `set()` in Set um
* Wandel Sie das Set mit `list()` wieder in eine Liste um
* Sortieren Sie die Liste mihilfe dert `sort`-Methode
* Geben Sie den Inhalt der Liste aus

⭐ [DuplikateEntfernen.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-5/DuplikateEntfernen.py)

### Aufgabe 5.6: Zoo

Gegeben ist der folgende Anfang eines Programms:

```python
animals = ["tiger", "mouse", "bird", "python", "elephant", "monkey"]
```

Ergänze das Programm so, dass für jedes Tier aus der Liste animals der Satz `VARIABLE ist ein Tier.` in der Konsole ausgegeben wird. Benutze dafür wie immer `print()` Funktion.

⭐ [Zoo.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-5/Zoo.py)

### Aufgabe 5.7: Minimum und Maximum

Schreiben Sie ein Programm, welches vom Benutzer 5 Zahlen einliest und diese in einer Liste speichert. Anschliessend soll das Minimum und das Maximum der Zahlen aus der Liste bestimmt und ausgegeben werden.

::: tip
Die folgenden Elemente sollten weiterhelfen:

```python
# Eine leere Listeerstellen
liste = []
```

```python
# Zahl eingeben
zahl = input("Eingabe: ")
```

```python
# Schleife von 1 bis 5
for i in range(1,6):
    print(i)
```

```python
# Kleinste Zahl aus Liste ausgeben
min([1,3,2])
```
:::

⭐ [MinimumMaximum.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-5/MinimumMaximum.py)

### Aufgabe 5.8: Übersetzung

Sie erhalten dieses Dictionary:

```python
monate = {
    'january': 'Januar',
    'february': 'Feburar',
    'march': 'März',
    'april': 'April',
    'mai': 'Mai',
    'june': 'Juni',
    'july': 'Juli',
    'august': 'August',
    'september': 'September',
    'october': 'Oktober',
    'november': 'November',
    'december': 'Dezember'
}
```

Schreiben Sie ein Programm welches für jeden Monat in der Liste den folgenden Satz ausgibt: `The german translation for 'january' is 'Januar'`.

⭐ [Übersetzung.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-5/Übersetzung.py)

### Aufgabe 5.9: Euklid

Schreibe ein Programm, welches mit `input()` zwei Zahlen vom Benutzer einliest und den grössten gemeinsamen Teiler der beiden Zahlen mit`print()` ausgibt.
    
Dazu können Sie den Euklidischen Algorithmus implementieren. Mehr dazu finden Sie hier: <https://de.wikipedia.org/wiki/Euklidischer_Algorithmus>.

⭐ [Euklid.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-5/Euklid.py)

## Wiederholungsfragen

**W1**: Versuchen Sie, drei unterschiedliche Wege zu finden, eine Liste mit den Vielfachen von 7 zu bilden, die kleiner als 100 sind (also [7, 14, ..., 98]).

<details>
Der einfachste und effizienteste Weg, eine Liste mit Vielfachen von 7 kleiner 100 zu generieren, bietet die range-Funktion:
<pre>
lst = list(range(7,100,7))  
print(lst)  
  [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
</pre>
Deutlich umständlicher ist es, von einer Liste aller Zahlen zwischen 1 und 100 auszugehen und dann die herauszufiltern, die durch 7 teilbar sind:
<pre>
hundred = list(range(1,101))  # [1, 2, ..., 100]  
lst = list(filter(lambda x: x%7==0, hundred))
</pre>
Eine weitere Variante besteht darin, mit den Zahlen von 1 bis 14 zu beginnen und jedes Element mit 7 zu multiplizieren. Im folgenden Beispiel kommt dabei die List-Comprehension-Syntax zur Anwendung.
<pre>
fourteen = list(range(1,15))  # [1, 2, ..., 14]  
lst = [ x*7 for x in fourteen ]
</pre>
Zum gleichen Ergebnis kommt list(map(...)) mit der Funktion x*7:
<pre>
lst = list(map(lambda x: x*7, fourteen))
</pre>
</details>

**W2**: Extrahieren Sie aus der Zeichenkette Hello, World! alle Vokale und verbinden Sie diese zu einer neuen Zeichenkette.

<details>
Diese Übung ist schon etwas schwieriger! list bildet aus der Zeichenkette eine Liste. list(filter(...)) bildet daraus eine neue Liste, die nur Vokale enthält. Den dabei eingesetzten in-Operator haben Sie bereits im Kapitel 3, »Operatoren«, kennengelernt. join fügt diese Liste wieder zu einer Zeichenkette zusammen.
<pre>
lst = list('Hello, World!')
vocals = list(filter(
  lambda x: x in ('a', 'e', 'i', 'o', 'u'), lst))
print(vocals)
  ['e', 'o', 'o']
result = ''.join(vocals)
print(result)
  eoo
</pre>
Der obige Code hat den Nachteil, dass er nur für Kleinbuchstaben funktioniert. Dieser Mangel lässt sich beheben, indem Sie im Filterausdruck Großbuchstaben mit lower in Kleinbuchstaben umwandeln:
<pre>
vocals = list(filter(
  lambda x: x.lower() in ('a', 'e', 'i', 'o', 'u'), lst))
</pre>
</details>

**W3**: Welchen Datentyp verwenden Sie, um Lottozahlen zu speichern?

<details>
Hier gibt es keine eindeutige Antwort: Eine Grundregel bei Lottozahlen ist, dass Sie eindeutig sein müssen. Es darf also keine Zahl mehrfach vorkommen. Aus diesem Grund bieten sich Sets an.
Oft sollen Lottozahlen aber geordnet dargestellt werden – und das können nur Listen. Die folgenden Zeilen zeigen, wie Sie Lottozahlen zuerst als Set speichern und daraus bei Bedarf eine geordnete Liste machen.
<pre>
lotto = {34, 12, 25, 26, 3, 40}  
geordnet = sorted(lotto)  
print(geordnet)  
  [3, 12, 25, 26, 34, 40]
</pre>
</details>

**W4**: Entfernen Sie die Doppelgänger aus einer Liste von Zahlen, z. B. aus [1, 2, 3, 2, 7, 3, 9]. Die Ergebnisliste soll aufsteigend sortiert sein.

<details>
Durch die Umwandlung in ein set werden alle Doppelgänger eliminiert. sorted macht aus dem Set eine geordnete Liste.
<pre>
lst = [1, 2, 3, 2, 7, 3, 9]  
result = sorted(set(lst))  
print(result)  
  [1, 2, 3, 7, 9]
</pre>
</details>

**W5**: Erstellen Sie ein kleines Deutsch-Englisch-Wörterbuch für Zahlen. Beispielsweise soll woerter['eins'] die englische Bezeichnung 'one' liefern.

<details>
Wie die Aufgabenstellung schon andeutet, ist hier ein Dictionary die optimale Datenstruktur. Beachten Sie aber, dass das Wörterbuch nur in eine Richtung funktioniert! woerter['three'] würde einen Key Error liefern, weil ja ausschließlich deutsche Wörter als Schlüssel verwendet wurden.
<pre>
woerter = { 'eins': 'one', 'zwei': 'two', 'drei': 'three'}  
woerter['zwei']  
  'two'
</pre>
</details>

**W6**: Berechnen Sie die Fakultät der Zahlen von 1 bis 20. (Die Fakultät ist als das Produkt aller Zahlen bis n definiert. Die Fakultät von 6 ist also 1×2×3×4×5×6 = 720.)

<details>
<pre>
f = 1  
for i in range(1, 21):  
  f = f * i  
  print('Die Fakultät von', i, 'beträgt', f)
</pre>
</details>

**W7**: Berechnen Sie die Summe der Funktion 1/x^2, wenn Sie für x alle Zahlen zwischen 2 und 30 einsetzen.

<details>
<pre>
Die Summe von 1/2 + 1/4 + 1/9 + … + 1/900 berechnen Sie z. B. so:
sum = 0   
for i in range(2, 31):   
    sum += 1 / (i*i)
</pre>
</details>

**W8**: Was wird bei der Ausführung des folgenden Codes ausgegeben?

```python
for i in range(1, 3):
    for j in range(i):
        print(i+j)
```

<details>
Das Programm gibt die Zahlen 1, 2 und 3 aus. Die Begründung lautet: In der äußeren Schleife hat i zuerst den Wert 0. Für die innere Schleife gilt nun range(1), was eine Kurzschreibweise für range(0, 1) ist. Da die obere Schranke exklusiv, wird die Schleife nur einmal mit j=0 ausgeführt. Das führt zur Ausgabe 1.
In der äußeren Schleife erhält i nun den Wert 2. Die j-Schleife durchläuft mit range(2) (entspricht range(0, 2)) die Werte 0 und 1. Damit werden die Zahlen 2 und 3 ausgegeben.
</details>

**W9**: Schreiben Sie eine while-Schleife, die in 5er-Schritten von 100 bis 0 zählt.

<details>
<pre>
i=100  
while i>=0:  
  print(i)  
  i-=5
</pre>
</details>

**W10**: Formulieren Sie eine Schleife, um den Wertebereich zwischen 125 und 160 in elf Schritten zu durchlaufen. Das Programm soll alle elf Zahlen ausgeben, beginnend mit 125,0 und endend mit 160,0.

<details>
Der Lösungscode beginnt mit der Definition von vier Variablen: min und max legen die obere und untere Grenze des Zahlenbereichs fest. nmax bestimmt die Anzahl der Schleifendurchläufe. delta gibt an, wie stark sich die Zielvariable x mit jedem Durchlauf ändern soll. In der Schleife durchläuft i die Werte von 0 bis einschließlich nmax.
<pre>
min = 125.0  
max = 160.0  
nmax = 11    
delta = (max - min) / (nmax - 1)  
for i in range(nmax):  
  x = min + delta * i  
  print(x)  
# Ausgabe: 125.0  128.5 132.0 135.5 ... 156.5 160.0
</pre>
</details>