# Übungen Thema 3.5

## Aufgaben

Augaben zum Thema.

### Aufgabe 3.5.1: Tage seit Geburt

Entwickeln Sie eine Programm, dass nach ihrem Geburtsdatum im Format `'%d.%m.%Y'` fragt.

Berechne Sie die Anzahl Tage, die seit dem Geburtsdatum vergangen sind und geben Sie diese aus.

::: tip
Damit die Differenz berechent werden kann, muss das heutige Datum und das Geburtsdatum Format ohne Zeit sein.

```
differenz = date.today() - geburtsdatum.date()
```
:::

### Aufgabe 3.5.2: Tage bis Geburtstag

Erweitern das Programme mit einer Berechnung der Anzahl Tage bis zum nächsten Geburstag aus. 

Geben Sie sie folgenden Text aus: `'Sie haben in {differenz.days} Tagen an einem {geburtstag.strftime("%A")} Geburtstag.'`

### Aufgabe 3.5.3: Schnellschreiber

Schreiben Sie ein Programm, dass diesen Text ausgibt:

```
Am 19. Januar 2038 haben 32-Bit Computer ein Problem.
```

Anschliessend soll man den Text wieder eingeben.

Vergleichen Sie den originalen String und die Eingabe. Geben Sie den Vergleichswert (Boolean) aus.

Messen Sie die Zeit der ganzen Programmausführung und geben Sie diese in Sekunden aus.

ℹ️ Ausgabe heisst immer `print()` und Eingabe immer `input()`

## Wiederholungsfragen

**W1**: Geben Sie das heutige Datum in der Form Montag, 31. 12. aus, also mit Wochentag, aber ohne Jahreszahl.

<details>
Die folgende Lösung erfüllt die Fragestellung weitgehend. Ein wenig störend ist aber die Null beim Monat (also 06. anstelle von 6.).
<pre>
from datetime import datetime  
import locale    
now = datetime.now()  
locale.setlocale(locale.LC_ALL, 'de_DE.utf8')  # Linux    
locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8') # macOS  
locale.setlocale(locale.LC_ALL, 'german')      # Windows  
print(now.strftime('%A, %d.%m.'))  
  Mittwoch, 27.06.
</pre>
Python sieht keinen Formatcode für die Monatszahl ohne führende Null vor. Um diesen Mangel zu beheben, können Sie .0 durch . ersetzen:
<pre>
s=now.strftime('%A, %d.%m.')  
print(s.replace('.0', '.'))  
  Mittwoch, 27.6.
</pre>
</details>

**W2**: Ein Kinofilm beginnt um 19:30 Uhr und dauert 132 Minuten. Wann ist die Vorstellung zu Ende?

<details>
Python kann zu time-Objekten keine Zeitspannen addieren. Deswegen bildet das folgende Script aus dem time-Objekt (Variable start) zuerst ein entsprechendes datetime-Objekt (Variable starttoday) und führt die Zeitrechnung dann durch:
<pre>
from datetime import datetime, time  
start = time(19, 30)                                       
starttoday = datetime.combine(datetime.today(), start)     
length = timedelta(minutes=132)  
end = starttoday + length  
print(end.time())  
  21:42:00
</pre>
</details>

**W3**: Ermitteln Sie, wie viele Sekunden seit Mitternacht vergangen sind.

<details>
Um die Anzahl der Sekunden seit Mitternacht zu berechnen, wird in midnight ein neues datetime-Objekt gespeichert, das sich aus dem aktuellen Datum ohne Stunden, Minuten und Sekunden zusammensetzt. Damit kann die Differenz zur aktuellen Zeit berechnet werden.
<pre>
from datetime import datetime, timedelta  
now = datetime.now()  
midnight = datetime(now.year, now.month, now.day)  
sincemidnight = now - midnight  
print('Uhrzeit: ', now.time())  
  Uhrzeit:  20:28:36.657155  
print('Sekunden seit Mitternacht:', sincemidnight.seconds)  
  Sekunden seit Mitternacht: 73716
</pre>
</details>