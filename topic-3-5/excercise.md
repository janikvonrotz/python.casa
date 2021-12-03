# Übungen Thema 3.5

## Aufgaben

Augaben zum Thema.

### Aufgabe 3.5.1: Tage seit Geburt

Entwickeln sie eine Programm, dass nach ihrem Geburtsdatum im Format `'%d.%m.%Y'` fragt.

Berechne sie die Anzahl Tage, die seit dem Geburtsdatum vergangen sind und geben sie diese aus.

::: tip
Damit die Differenz berechent werden kann, muss das heutige Datum und das Geburtsdatum Format ohne Zeit sein.

```
differenz = date.today() - geburtsdatum.date()
```
:::

### Aufgabe 3.5.2: Tage bis Geburtstag

Erweitern das Programme mit einer Berechnung der Anzahl Tage bis zum nächsten Geburstag aus. 

Geben sie sie folgenden Text aus: `'Sie haben in {differenz.days} Tagen an einem {geburtstag.strftime("%A")} Geburtstag.'`

### Aufgabe 3.5.3: Schnellschreiber

Schreiben sie ein Programm, dass diesen Text ausgibt:

```
Am 19. Januar 2038 haben 32-Bit Computer ein Problem.
```

Anschliessend soll man den Text wieder eingeben.

Vergleichen sie den originalen String und die Eingabe. Geben sie den Vergleichswert (Boolean) aus.

Messen sie die Zeit der ganzen Programmausführung und geben sie diese in Sekunden aus.

ℹ️ Ausgabe heisst immer `print()` und Eingabe immer `input()`

## Wiederholungsfragen

* **W1**: Geben Sie das heutige Datum in der Form Montag, 31. 12. aus, also mit Wochentag, aber ohne Jahreszahl.
* **W2**: Ein Kinofilm beginnt um 19:30 Uhr und dauert 132 Minuten. Wann ist die Vorstellung zu Ende?
* **W3**: Ermitteln Sie, wie viele Sekunden seit Mitternacht vergangen sind.