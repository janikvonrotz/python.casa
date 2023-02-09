# Übungen Thema 13

## Aufgaben

Aufgaben zum Thema.

### Aufgabe 13.1: Git-Projekt erstellen

Erstellen Sie ein neues Git-Projekt indem Sie die folgenden Aktionen ausführen:

* Ordner `Thema 13.1` erstellen
* Eine Datei `app.py` mit Inhalt `print('Hello Git')` hinzufügen
* Das lokale Git-Repository initialisieren
* Einen ersten Commit mit Nachricht `Init app` erstellen
* Eine zusätzliche Datei `db.py` mit Inhalt `print('Hello SQLite')` hinzufügen
* Die neue Datei ebenfalls committen

Geben Sie die Git History mit dem Befehl `git log` aus.

⭐ [Git-Projekt erstellen](https://github.com/janikvonrotz/python.casa/tree/main/topic-13/Git-Projekt%20erstellen)

### Aufgabe 13.2: Projekt auschecken

Auf GitHub haben Sie das vielversprechende Repository <https://github.com/fluentpython/example-code> entdeckt und möchten nun den Code lokal ausführen. Kopieren Sie die HTTPS-Url und klonen Sie das Projekt mit VSCode.

![git-clone](../git-clone.gif)

Suchen Sie das Programm `bus.py` mithilfe der Suchfunktion <kbd>ctrl</kbd> + <kbd>p</kbd>. Fügen Sie dem Programm den Code unten an und führen Sie das Beispiel aus:

```python
bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
print(bus1.passengers)
bus1.pick('Bob')
print(bus1.passengers)
```

Haben Sie das Programm verstanden?

### Aufgabe 13.3: Branch erstellen

Erstellen Sie einen Branch `my-example` und comitten Sie die gemachten Änderungen.

![git-branch](../git-branch.gif)

Wie wechseln Sie zwischen dem Branch `master` und `my-example`?

⭐ [Branch erstellen](https://github.com/janikvonrotz/python.casa/tree/main/topic-13/Branch%20erstellen)

### Aufgabe 13.4: Branch zusammenführen

Wechseln Sie zum `master` Branch und *mergen* Sie den `my-example` branch. Geben Sie dazu diesem Befehl auf dem Terminal ein: `git merge my-example -m "merge my example"`.

Schauen Sie sich die Datei `bus.py` an. Sind ihre Änderungen jetzt auf dem `master` Branch vorhanden?