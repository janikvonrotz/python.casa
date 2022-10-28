## Datum und Zeit

[◀️ Thema 4](README.md)

⚡[Anwesenheit bestätigen](https://moodle.medizintechnik-hf.ch/mod/attendance/manage.php?id=8024)

📖 Kapitel 6 Datum und Zeit

---
### Lernziele

Ich kann ...
* Datum und Uhrzeit einlesen und in einer Variable speichern.
* Datum und Uhrzeit in einem bestimmten Format ausgeben.
* Zeitdifferenzen in Stunde, Tagen und Jahren berechnen.

---

### Timestamp

🤔 Wie speichert der Computer die aktuelle Uhrzeit?

🙋 <https://www.unixtimestamp.com/>

---

### IDE vorbereiten

🎬 Führen Sie diese Aktionen aus:
* Neuer Ordner `Thema4` erstellen
* Neue Datei `Datum und Zeit.py` erstellen

---

### Aktuelles Datum und Uhrzeit

🎬 Das aktuelle Datum und Uhrzeit ausgeben.

```python
from datetime import datetime # Neue Funktionen aus der Python-Bibliothek
now = datetime.now()
print(now) # Ausgabe: YYYY-MM-DD HH:MM:SS
```

---

### Unix Timestamp ausgeben

🎬 Anzahl Sekunden seit 01.01.1970

```python
print(now.timestamp())
```

ℹ️ Im Jahr 2038 haben 32-Bit Computer ein Problem.

---

### Jahr 2038

Wann haben 32-Bit Computer ein Problem?

```python
from datetime import datetime
sekunden = int(datetime.now().timestamp())
sekunden_binär = bin(sekunden)
anzahl_bits = len(str(sekunden_binär))-2 # Ist 31

print(f'Maximales Datum: {2**anzahl_bits}')
```

Output eingeben unter: <https://www.unixtimestamp.com/>

ℹ️ Mehr dazu <https://de.wikipedia.org/wiki/Unixzeit#Jahr-2038-Problem>.

---

### Einzelne Zeitkomponten ausgeben

🎬 Jahr oder Monat ausgeben.

```python
print(now.year)
print(now.month)
```

---

### Datum und Zeit formatieren

🎬 Datum und Zeit können formatiert werden.

```python
print(now.isoformat())
print(now.strftime('%d.%m.%Y %H:%M'))
```

ℹ️ Dateinamen am besten mit ISO-Format bennen. Dann stimmt die Sortierung.

---

### Eigenes Datumsformat

Liste der Platzhalter: <https://docs.python.org/3/library/time.html#time.strftime>

🎬 Erstellen Sie eine eigene Formatierung.

```python
print(now.strftime('%A, %d. %B %Y'))
```

---

### Datum und Zeit lokalisieren

🎬 Ausgabe in der lokalen Sprache.

```python
import locale  
locale.setlocale(locale.LC_ALL, 'de_DE.utf8')  # Linux    
locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8') # macOS  
locale.setlocale(locale.LC_ALL, 'german')      # Windows  

from datetime import datetime
print(datetime.now.strftime('%A, %d. %B %Y'))
```

---

### Datum aus String lesen

🎬 Bei der Eingabe eines Datum ist das Format entscheidend.

```python
from datetime import datetime
s = '2018-08-01 18:47'  
dt = datetime.strptime(s, '%Y-%m-%d %H:%M')
print(dt)
```

---

### Datum ohne Zeit

Wir haben keine Zeit.

```python
from datetime import date
print(date.today())
```

ℹ️ Wir importieren `date` und verwendent `today`.

---

### Zeit ohne Datum

Wir haben kein Datum.

```python
from datetime import datetime
print(datetime.now().time())
```

---

### Mit Zeiten rechnen

🎬 Mit `timedelta` können Sie Zeit dazu rechnen.

```python
from datetime import datetime, timedelta
today = datetime.now()
week = timedelta(weeks=1)
print(today)
print(week)
print(today + week)
```

---
### Zeitdifferenz berechnen

🎬 Verwendet man `today()` kann die Differenz in Tagen berechnen.

```python
from datetime import date, timedelta  
today = date.today()  
weihnachten = date(today.year, 12, 24)  
warten = weihnachten - today  
print('Noch', warten.days, 'Tage bis Weihnachten.')
```

---
### Aufgaben 1

Lösen Sie die ersten zwei [Aufgaben](excercise.md#aufgaben) 4.1 und 4.2.

⚡Aufteilung in Gruppen/Breakout-Rooms ⏱️ 10 Minuten

---

### Zeitzonen

Wir leben in verschiedenen Zeitzonen.

![](../zeitzonen.png)

---

### Datum UTC

🎬 Wir geben das Datum in der Zeitzone Coordinated Universal Time (UTC) aus.

```python
from datetime import datetime  
import pytz  
utc = datetime.now(pytz.utc)  
print(utc)
```

---

### Datum bestimmte Zeitzone

🎬 Wir können ein Datum einer bestimmten Zeitzone zuordnen.

```python
berlin = pytz.timezone('Europe/Berlin')
berlintime = berlin.localize(datetime.now())
print(berlintime)
```

---

### Laufzeit von Code messen

Wie lange braucht der Computer für eine Berechnung?

🎬 Führen Sie dieses Programm aus.

```python
import time, math
start = time.process_time()

# Sinnlos Zeit totschlagen  
for i in range(1, 1000000):    
  x=math.sin(i)

end = time.process_time()    
print(end - start, 'Sekunden')
```

ℹ️  Mit `import math` erhalten Sie Zugriff auf mathematische Funktionen.

---

### Laufzeit der Programmausführung messen

Wie lange wird das Programm ausgeführt?

🎬 Führen Sie dieses Programm aus.

```python
from datetime import datetime
start = int(datetime.now().timestamp())

s = input()

end = int(datetime.now().timestamp())
print(end - start, 'Sekunden')
```

---
### Aufgaben 2

Lösen Sie die restlichen [Aufgaben](excercise.md#aufgaben).

⚡Aufteilung in Gruppen/Breakout-Rooms ⏱️ 10 Minuten

---
### Review

🎯 Wurden die [Lernziele](#lernziele) erreicht?

⚡ Feedback zu den Zielen einholen.
