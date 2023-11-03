# Übungen Thema 3

## Aufgaben

Aufgaben zum Thema.

### Aufgabe 3.1:  Wahr oder Falsch

Es folgt ein Skript mit 3 Ausgaben (`print`). Bestimmen Sie für jede Ausgabe ob der Ausdruck `True` oder `False` ist.

```python
x = False
y = True
z = 1

print(x and y and z)
print(x or z)
print(not(x and not y))
```

Konnten Sie die Ausgaben richtig bestimmen? Prüfen Sie ihre Antworten indem Sie das Skript ausführen.

⭐ [WahrFalsch.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-3/WahrFalsch.py)

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

⭐ [Vereinfachen.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-3/Vereinfachen.py)

### Aufgabe 3.3: Geheim

Wir haben eine geheime Zeichensequenz erhalten:

```
msg = 'LeLrLeLrLoLdLeLlLbLmLuLDLsLlLlLiLKLeLpLaLnLSLeLr'
```

Zum entschlüsseln müssen wir ...
* die Position 4 bis 44 herausschneiden
* die Reihenfolge umkehren
* jede zweite Position lesen

Zur Hilfe haben wir diese Slice-Anweisungen:

```python
msg = msg[::-1]
msg = msg[::2]
msg = msg[4:44]
```

Wie lautet die geheime Nachricht?

⭐ [Geheim.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-3/Geheim.py)

### Aufgabe 3.4: Formatierung 🚧

<!-- Einfache Aufgabe mit String als Variable und Ausgeben in text. -->

### Aufgabe 3.4: Suchen und Ersetzen

Sie erhalten diesen Text:

```python
text = 'The quick brown fox jumps over the lazy dog'
```

Führen Sie diese Anweisungen aus:

* Suchen Sie nach dem Wort `fox`. Sie erhalten die Position als Antwort.
* Ersetzen Sie das Wort `fox` mit `cat`.

Wenn das zu einfach war führen Sie diese Anweisungen aus:
1. Alle Zeichen bis zum Wort `brown` ausgeben.
2. Alle Zeichen ab Wort `brown` ausgeben.
3. Die Anweisungen 1 und 2 kombinieren damit `The quick fox jumps over the lazy dog` ausgeben wird.

⭐ [SuchenErsetzen.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-3/SuchenErsetzen.py)

### Aufgabe 3.5: DNA

Eine Analyse hat eine DNA-Sequenz zurückgeben. 

```
ACTNGTGCTYGATRGTAGC
```

Wir möchten herausfinden, ob diese Sequenz auch wirklich DNA enthält [^1]. Zählen Sie die Anzahl der Buchstaben A, T, G und C in der Sequenz zu einer Summe.

⭐ [DNA.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-3/DNA.py)

### Aufgabe 3.6: DNA 2

Rechnen Sie die Summe geteilt durch die Anzahl Zeichen der Sequenz. Das Ergebnis ist eine Prozentzahl. Formatieren Sie Prozentzahl so, dass die Zahl zwei Stellen nach dem Komma und mit Prozentzeichen ausgegeben wird.

⭐ [DNA2.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-3/DNA2.py)

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