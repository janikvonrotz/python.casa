# Übungen Thema 3

## Aufgaben

Aufgaben zum Thema.

### Aufgabe 3.1 Vereinfachen

Vereinfachen sie den folgenden Ausdruck:

```py
not (not (a or (a and b))) and (b and (b or a))
```

### Aufgabe 3.2 Kurzschluss

Nehmen sie den logischen Ausdruck von Aufgabe 3.1 und bestimmen sie, ob dieser unter den folgenden Bedinungen vollständig evaluiert wird oder nicht:

Bedingung 1:

```
a = True
b = False
```

Bedingung 2:

```
a = False
b = True
```

### Aufgabe 3.3 DNA

Eine Analyse hat eine DNA-Sequenz zurückgeben. 

```
ATAGCTGATCGTAGCTACGTACGATCG
```

Wir möchten herausfinden, ob diese Sequenz auch wirklich DNA enthält. Zählen sie die Buchstaben A, T, G und C in der Sequenz zu einer Summe.

### Aufgabe 3.4 DNA 2

Rechnen sie die Summe geteilt durch die Anzahl Zeichen der Sequenz. Das Ergebnis ist eine Prozentzahl. Formatiert die Ausgabe so, dass die Zahl zwei Stellen nach dem Komma und mit Prozentzeichen ausgegeben wird.

### Aufgabe 3.5 Unicode

Wir haben eine geheime Zeichensequenz erhalten:

```
1x1A1H1R1Y1J1S151g1H1o
```

Zum entschlüsseln, müssen wir die Reihenfolge umkehren, jedes zweite Zeichen lesen und `x` mit `0` ersetzen.

### Aufgabe 3.6 Bonusaufgabe

Die Nachricht verrät nicht viel. Der Internet-Kenner weiss aber, dass es sich um eine Youtube-ID handelt. Vervollständigen sie den folgenden Code und führen sie ihn aus:

```py
import webbrowser

youtube_id = 
webbrowser.open('https://www.youtube.com/watch?v=%s' % ())
```

## Wiederholungsfragen

* W1: Wie bilden Sie eine Zeichenkette, die selbst ein Anführungszeichen enthält?

ℹ️ Anführungszeichen sind Zeichen aus der Programmier-Syntax.

* W2: Wie bilden Sie Zeichenketten, die das Zeichen \\ enthalten?
* W3: Extrahieren Sie aus der folgenden Zeichenkette das Tag zwischen den eckigen Klammern:

`bla [wichtig] mehr bla`

* W4: Zerlegen Sie den folgenden Dateinamen in Linux-Notation in die Verzeichnisangabe (bis zum letzten /-Zeichen) und den eigentlichen Dateinamen (ab dieser Position):

`/home/kofler/Bilder/foto1.jpg`

* W5: Fordern Sie den Anwender eines Scripts auf, seinen Namen einzugeben, und entfernen Sie dann alle Leerzeichen am Beginn und Ende der Eingabe.
* W6: Geben Sie Hello, World! in umgekehrter Reihenfolge aus.