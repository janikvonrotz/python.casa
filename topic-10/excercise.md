# Übungen Thema 10

## Aufgaben

Aufgaben zum Thema.

### Aufgabe 10.1: Projekt auschecken

Auf GitHub haben sie das vielversprechende Repository <https://github.com/fluentpython/example-code> entdeckt und möchten nun den Code lokal ausführen. Kopieren sie die HTTPS-Url und klonen sie das Projekt mit VSCode.

![git-clone](../git-clone.gif)

Suchen sie das Programm `bus.py` mithilfe der Suchfunktion <kbd>ctrl</kbd> + <kbd>p</kbd>. Fügen sie dem Programm den Code unten an und führen sie das Beispiel aus:

```py
bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
print(bus1.passengers)
bus1.pick('Bob')
print(bus1.passengers)
```

Haben sie das Programm verstanden?

### Aufgabe 10.2: Branch erstellen

Erstellen sie einen Branch `my-example` und comitten sie die gemachten Änderungen.

![git-branch](../git-branch.gif)

Wie wechseln sie zwischen dem Branch `master` und `my-example`?

### Aufgabe 10.3: Branch zusammenführen

Wechseln sie zum `master` Branch und *mergen* sie den `my-example` branch. Geben sie dazu diesem Befehl auf dem Terminal ein: `git merge my-example -m "merge my example"`.

Schauen sie sich die Datei `bus.py` an. Sind ihre Änderungen jetzt auf dem `master` Branch vorhanden?