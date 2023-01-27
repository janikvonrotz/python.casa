# Übungen Thema 11

## Aufgaben

Aufgaben zum Thema.

### Aufgabe 11.1: Fenster anpassen

Verwenden Sie den Code von [gui.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-11/gui.py) und passen Sie ihn wie folgt an:

* Bennen Sie den Titel des Fenster auf `Kalkulator` um.
* Ändern Sie den Text des `change_button` auf `Berechnen`.
* Ersetzen Sie die Funktion `button_action` mit dieser:

```python
def button_action(x=1, y=2):
	anweisungs_label.config(text=f'Sie Summe von {x} und {y} ist {x+y}')
```

* Ändern Sie den Text des `anweisungs_label` auf `Was ergibt 1 + 2?`.

Führen Sie das Programm aus.

⭐ [Fenster anpassen.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-11/gui.py)

### Aufgabe 11.2: Fenster mit Eingabe

### Aufgabe 11.3: Menü

### Aufabe 11.4: Messagebox