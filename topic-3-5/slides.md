### Aktuelles Datum und Uhrzeit

```py
from datetime import datetime  
now = datetime.now()  
print(now)
```

### Einzelne Zeitkomponten ausgeben


```py
print(now.year)
print(now.month)
```

### Datum und Zeit formatieren


```py
print(now.isoformat())
print(now.strftime('%d.%m.%Y %H:%M'))
```

<https://docs.python.org/3/library/time.html#time.strftime>

```py
print(now.strftime('%A, %d. %B %Y'))
```

### Datum und Zeit lokalisieren

```py
import locale  
locale.setlocale(locale.LC_ALL, 'de_DE.utf8')  # Linux    
locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8') # macOS  
locale.setlocale(locale.LC_ALL, 'german')      # Windows  
print(now.strftime('%A, %d. %B %Y'))
```

### Datum einlesen

```py
s = '2018-08-01 18:47'  
dt = datetime.strptime(s, '%Y-%m-%d %H:%M')

```

### Datum ohne Zeit


### Zeit ohne Datum


### Zeitzonen

### Mit Zeiten rechnen

### Laufzeit von Code messen