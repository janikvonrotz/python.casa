## Datum und Zeit

[Thema 3.5](README.md)\
Umfang ⏱️: 1 Lektion

⚡[Anwesenheit bestätigen](https://moodle.medizintechnik-hf.ch/mod/attendance/manage.php?id=4479) und Webcam einschalten.

📖 Kapitel 6 Datum und Zeit

---

### Timestamp

🤔 Wie speichert der Computer eine Uhrzeit?

🙋 <https://www.unixtimestamp.com/>

---

### Aktuelles Datum und Uhrzeit

Das aktuelle Datum und Uhrzeit ausgeben.

```py
from datetime import datetime
now = datetime.now()
print(now) # Ausgabe: YYYY-MM-DD HH:MM:SS
```

---

### Unix Timestamp ausgeben

Anzahl Sekunden seit 01.01.1970

```
print(now.timestamp())
```

ℹ️ Im Jahr 2038 haben 32-Bit Computer ein Problem.

---

### Jahr 2038

Wann haben 32-Bit Computer ein Problem?

```py
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

Jahr oder Monat ausgeben.

```py
print(now.year)
print(now.month)
```

---

### Datum und Zeit formatieren

```py
print(now.isoformat())
print(now.strftime('%d.%m.%Y %H:%M'))
```

ℹ️ Dateinamen am besten mit ISO-Format bennen. Dann stimmt die Sortierung.

---

### Eigenes Datumsformat

<https://docs.python.org/3/library/time.html#time.strftime>

```py
print(now.strftime('%A, %d. %B %Y'))
```

---

### Datum und Zeit lokalisieren

Ausgabe in der lokalen Sprache.

```py
import locale  
locale.setlocale(locale.LC_ALL, 'de_DE.utf8')  # Linux    
locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8') # macOS  
locale.setlocale(locale.LC_ALL, 'german')      # Windows  

from datetime import datetime
print(datetime.now.strftime('%A, %d. %B %Y'))
```

---

### Datum einlesen

Bei der Eingabe eines Datum ist das Format entscheidend.

```py
from datetime import datetime
s = '2018-08-01 18:47'  
dt = datetime.strptime(s, '%Y-%m-%d %H:%M')
print(dt)
```

---

### Datum ohne Zeit

Wir haben keine Zeit.

```py
from datetime import date
print(date.today())
```

ℹ️ Wir importieren `date` und verwendent `today`.

---

### Zeit ohne Datum

Wir haben kein Datum.

```py
from datetime import datetime
print(datetime.now().time())
```

---

### Mit Zeiten rechnen

Mit `timedelta` können sie Zeit dazu rechnen.

```py
from datetime import datetime, timedelta
today = datetime.now()
week = timedelta(weeks=1)
print(today)
print(week)
print(today + week)
```

---
### Zeitdifferenz berechnen

Verwendet man `today()` kann die Differenz in Tagen berechnen.

```py
from datetime import date, timedelta  
today = date.today()  
weihnachten = date(today.year, 12, 24)  
warten = weihnachten - today  
print('Noch', warten.days, 'Tage bis Weihnachten.')
```

---
### Aufgaben 1

Lösen sie die ersten zwei [Aufgaben](excercise.md#aufgaben).

⚡Aufteilung in Gruppen/Breakout-Rooms ⏱️ 10 Minuten

Ziel: Aufgabe 3.5.1 und 3.5.2 sind gelöst.

---

### Zeitzonen

![](../zeitzonen.png)

---

### Datum UTC

Wir geben das Datum in der Zeitzone Coordinated Universal Time (UTC) aus.

```py
from datetime import datetime  
import pytz  
utc = datetime.now(pytz.utc)  
print(utc)
```

---

### Datum bestimmte Zeitzone

Wir können ein Datum einer bestimmten Zeitzone zuordnen.

```py
berlin = pytz.timezone('Europe/Berlin')
berlintime = berlin.localize(datetime.now())
print(berlintime)
```

---

### Laufzeit von Code messen

Wie lange braucht der Computer für eine Berechnung?

```py
import time, math
start = time.process_time()

# Sinnlos Zeit totschlagen  
for i in range(1, 1000000):    
  x=math.sin(i)

end = time.process_time()    
print(end - start, 'Sekunden')
```

---

### Laufzeit der Programmausführung messen

Wie lange wird das Programm ausgeführt?

```
from datetime import datetime
start = int(datetime.now().timestamp())

s = input()

end = int(datetime.now().timestamp())
print(end - start, 'Sekunden')
```

---
### Aufgaben 2

Lösen sie die dritte [Aufgabe](excercise.md#aufgaben).

⚡Aufteilung in Gruppen/Breakout-Rooms ⏱️ 10 Minuten

Ziel: Aufgabe 3.5.3 ist gelöst.
