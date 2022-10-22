# Übungen Thema 2

## Aufgaben

Aufgaben zum Thema.

### Aufgabe 2.1: Variablen dekalieren

Erstellen Sie ein Skript, welches die folgenden Variablen und Werte deklariert:

* Variable `pi` mit Wert `3.1415926535`
* Variable `erdumfang_km` mit Wert `40075`

Geben Sei zu jeder Variable den Variablentyp aus. Entsprechen die Datentypen ihren Erwartungen?

⭐ [Variablen.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-2/Variablen.py)

### Aufgabe 2.2: Zufall

Generieren Sie eine Zufallszahl vom Typ `float` im Bereich von 1.0 bis 10.0.

::: tip
Die Python Dokumentation bietet zu allen Module Informationen. Hier der Link zum Random-Modul: [random / Generate pseudo-random numbers](https://docs.python.org/3/library/random.html#module-random)

Verwenden Sie die `uniform`-Funktion für diese Aufgabe.

```python
from random import uniform
```
:::

⭐ [Zufall.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-2/Zufall.py)

### Aufgabe 2.3: Runden

Runden Sie die generierte Zahl auf 3 Stellen nach dem Komma.

⭐ [Zufall.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-2/Zufall.py)

### Aufgabe 2.4: Modulo

Fragen Sie den Benutzer nach einer ersten und einer zweiten Zahl. Geben Sie den Restwert einer Division der ersten durch die zweite Zahl aus.

::: warning
Wenn die Heap-Ansicht noch aktiviert ist, kann es sein, das Python nicht den Wert der Zahl liefert, sondern deren Referenz. Deaktivieren Sie die Heap-Ansicht um sicher zu gehen.
:::

⭐ [Modulo.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-2/Modulo.py)

### Aufgabe 2.5: Ungleich

Führen Sie das folgende Programm aus:

```python
a = True
b = 1
print(a == b) # Ausgabe: True
print(a is b) # Ausgabe: False
```

Warum sind sind die Werte im ersten Fall gleich und im zweiten Fall nicht?

⭐
<details>
Der Operator `is` vergleich nicht den Wert wie `==`, sondern die Adresse im RAM-Speicher.
</details>

## Wiederholungsfragen

**W1**: Der folgende Code löst einen Fehler aus. Warum?

```python
x=1; y=2
print(x+y+z)
```

<details>
Jeder Python-Variablen muss ein Wert zugewiesen werden, bevor Sie ausgewertet werden kann. Das war bei z nicht der Fall. Es gibt keinen Defaultzustand (etwa 0). So funktioniert der Code:
<pre>
x=1; y=2; z=0  
print(x+y+z)
</pre>
</details>

**W2**: Welchen Typ hat die Variable i nach der Zuweisung `i=3`?

<details>
In Python haben Variablen keinen Typ! Nach i=3 zeigt i auf ein Objekt mit der ganzen Zahl 3. Dieses Objekt (nicht die Variable) hat also den Typ int. Dementsprechend liefert type(i) das Ergebnis class 'int'. Allerdings kann bereits in der nächsten Anweisung i='abc' ausgeführt werden. Dann zeigt i auf ein Objekt mit einer Zeichenkette.
</details>

**W3**: Welche Werte gibt das folgende Programm aus?

```python
a = 'abcde'
b = a
a = a+'fg'
print(b)
```

<details>
Das folgende Programm endet mit der Ausgabe abcde. Die Zeichenketten, auf die a und b verweisen, sind voneinander unabhängig, weil es sich beim str-Typ um einen unveränderlichen Datentyp handelt (immutable). Die Veränderung von a hat daher keinen Einfluss auf b.
<pre>
a='abcde'  
b=a  
a=a+'fg'  
print(b)  
  abcde
</pre>
</details>

**W4**: Der folgende Code ist fehlerhaft. Warum? Wie könnte eine Lösung aussehen?

```python
n=22.7
msg='Die Temperatur beträgt ' + n + ' Grad.'
```

<details>
Python führt nur in Ausnahmefällen eine automatische Typumwandlung durch. Der Code aus der Wiederholungsfrage versucht, eine Zeichenkette und eine Zahl zu verbinden. Das ist in Python nicht zulässig. Die Fehlermeldung lautet unsupported operand, weil der Operator + nicht eine Zahl und eine Zeichenkette verarbeiten kann. Eine mögliche Lösung besteht darin, die Zahl mit der str-Funktion explizit in eine Zeichenkette umzuwandeln:
<pre>
msg='Die Temperatur beträgt ' + str(n) + ' Grad.'
</pre>
</details>

**W5**: Wie führen Sie eine ganzzahlige Division durch?

<details>
Ganzzahlige Divisionen werden mit dem Operator // durchgeführt. 12//7 ergibt 1.
</details>

**W6**: Welchem Zahlenwert ist True zugeordnet?

<details>
Wenn True in eine ganze Zahl umgewandelt wird, hat der Zustand den Wert 1: <pre>
print(int(True))  
  1
</pre>
</details>

**W7**: Sie wollen den Rest der Division 225 / 17 ermitteln. Wie gehen Sie vor?

<details>
<pre>
Den Rest der Division 225 / 17 ermitteln Sie mit dem %-Operator:
print(225 % 17) # Ergebnis 4
</pre>
</details>

## Mehr zum Thema

* Video: [Python3-Einstieg #3 - Zahlen (Teil 1)](https://youtu.be/uBi17MBFjL0)
* Video: [Python3-Einstieg #3 - Zahlen (Teil 2)](https://youtu.be/oHRNDPqXgpM)
* Beitrag: [Python Byte Code Hacks](http://www.bravegnu.org/blog/python-byte-code-hacks.html)