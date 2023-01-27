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

⭐ [Fenster anpassen.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-11/Fenster%20anpassen.py)

### Aufgabe 11.2: Fester fixieren

Verwenden Sie den Code oder Lösung aus der Aufgabe 1.1. In dieser Aufgabe möchten Sie die Grösse des Fenster ändern und die Breite der der Zellen im Koordinatensystem festlegen. Dazu verwenden Sie diesen Code:

```python
fenster.geometry('300x200')
rows = 9
columns = 9
for i in range(rows):
    fenster.rowconfigure(index=i,weight=1)
for i in range(columns):
    fenster.columnconfigure(index=i, weight=1)
```

Fügen Sie diesen Code nach Zeile 7 ein.

Damit die Elemente in der Mitte platziert werden, verwenden Sie diesen Code:

```python
# Elemente mit Grid laden
anweisungs_label.grid(row=1, column=4, pady=10, padx=10)
change_button.grid(row=2, column=4, pady=10, padx=10)
exit_button.grid(row=3, column=4, pady=10, padx=10)
```

Führen Sie das Programm aus.

⭐ [Fenster fixieren.py](https://github.com/janikvonrotz/python.casa/blob/main/topic-11/Fenster%20fixieren.py)

### Aufgabe 11.3: Eingabefelder erstellen

### Aufabe 11.4: Messagebox anzeigen