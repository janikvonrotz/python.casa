# Übungen Thema 3

## Aufgaben

Aufgaben zum Thema.

### Aufgabe 3.1:  Wahr oder Falsch  🚧

### Aufgabe 3.2: Vereinfachen

Vereinfachen Sie den folgenden Ausdruck:

```python
not (not (a)) and (b and (b or a))
```

Bestimmen sie, ob dieser unter den folgenden Bedinungen vollständig evaluiert wird oder nicht:

Bedingung 1:

```python
a = True
b = False
```

Bedingung 2:

```python
a = False
b = True
```

### Aufgabe 3.3: Suchen und Erstetzen 🚧

### Aufgabe 3.4: DNA

Eine Analyse hat eine DNA-Sequenz zurückgeben. 

```
ACTNGTGCTYGATRGTAGC
```

Wir möchten herausfinden, ob diese Sequenz auch wirklich DNA enthält [^1]. Zählen Sie die Anzahl der Buchstaben A, T, G und C in der Sequenz zu einer Summe.

### Aufgabe 3.5: DNA 2

Rechnen Sie die Summe geteilt durch die Anzahl Zeichen der Sequenz. Das Ergebnis ist eine Prozentzahl. Formatieren Sie Ausgabe so, dass die Zahl zwei Stellen nach dem Komma und mit Prozentzeichen ausgegeben wird.

### Aufgabe 3.6: Geheim 🚧

Wir haben eine geheime Zeichensequenz erhalten:

```
1x1A1H1R1Y1J1S151g1H1o
```

Zum entschlüsseln müssen wir ...
* die Reihenfolge umkehren
* jedes zweite Zeichen lesen
* `x` mit `0` ersetzen

Wie lautet die geheime Nachricht.

## Wiederholungsfragen

**W1**: Wie bilden Sie eine Zeichenkette, die selbst ein Anführungszeichen enthält?

ℹ️ Anführungszeichen sind Zeichen aus der Programmier-Syntax.

<details>
Eine Möglichkeit besteht, zur Abgrenzung von Zeichenketten das jeweils andere Zeichen zu verwenden, also:
<pre>
s1="O'Reilly"  
s2='It is "O Reilly"'
</pre>
Eine zweite Möglichkeit bieten die Spezialcodes \' und \":
<pre>
s3='abc \" def \' ghi'  # ergibt: abc " def ' ghi
</pre>
</details>

**W2**: Wie bilden Sie Zeichenketten, die das Zeichen \\ enthalten?

<details>
Wenn der Backslash nicht zur Kennzeichnung von Sonderzeichen verwendet werden soll, formulieren Sie Zeichenketten am besten in der Raw-Syntax mit vorangestelltem r:
<pre>
s=r'C:\verzeichnis\readme.txt'
</pre>
</details>

**W3**: Extrahieren Sie aus der folgenden Zeichenkette das Tag zwischen den eckigen Klammern:

`bla [wichtig] mehr bla`

<details>
<pre>
s='bla [wichtig] mehr bla'  
start=s.find('[')+1    # Startposition  
end=s.rfind(']')       # Endposition  
print(s[start:end])    # Teilzeichenkette auslesen  
  'wichtig'
</pre>
</details>

**W4**: Zerlegen Sie den folgenden Dateinamen in Linux-Notation in die Verzeichnisangabe (bis zum letzten /-Zeichen) und den eigentlichen Dateinamen (ab dieser Position):

`/home/kofler/Bilder/foto1.jpg`

<details>
<pre>
s='/home/kofler/Bilder/foto1.jpg'  
pos=s.rfind('/')+1  
pfad=s[:pos]  
datei=s[pos:]  
print('Pfad:', pfad, 'Datei:', datei)  
  Pfad: /home/kofler/Bilder/   Datei: foto1.jpg
</pre>
</details>

**W5**: Fordern Sie den Anwender eines Scripts auf, seinen Namen einzugeben, und entfernen Sie dann alle Leerzeichen am Beginn und Ende der Eingabe.

<details>
<pre>
name = input('Geben Sie Ihren Namen an: ')  
name = name.strip()
</pre>
</details>

**W6**: Geben Sie Hello, World! in umgekehrter Reihenfolge aus.

<details>
<pre>hello = 'Hello, World!'  
print(hello[::-1])  
  !dlroW ,olleH
</pre>
</details>

**W7**: Was ist die *Short-Circuit-Evaluation*? Nennen Sie ein Beispiel!

<details>
Die logischen Operatoren and und or verzichten auf die Auswertung des zweiten Operanden, wenn der erste Operand bereits zum Ergebnis führt. Wenn im folgenden Beispiel rechenfunktion(x) den Wert 0 oder eine negative Zahl liefert, dann wird rechenfunktion(y) nicht aufgerufen. Das ist nicht notwendig, weil and nur dann True liefern kann, wenn beide Teilergebnisse True sind.
<pre>
x=2  
y=3  
if rechenfunktion(x)>0 and rechenfunktion(y)>0:   
    # Code ...
</pre>
</details>

## Quellen

[^1]: [How to count non-DNA bases in a sequence using Python](https://pythonforbiologists.com/counting-non-dna-bases-in-a-sequence.html)