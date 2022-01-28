## Module und Import

[Thema 7](./README.md)

⚡[Anwesenheit bestätigen](https://moodle.medizintechnik-hf.ch/mod/attendance/manage.php?id=6139) und Webcam einschalten.

📖 Kapitel 12 Module

---

### Python-Module

 Die `import` Anweisung importiert Code aus der Python-Bibliothek.

 Sie importieren damit Python-Module.

 Dieser modulare Ansatz von Python schauen wir genauer an.

---

### Python-Module auflisten

🎬 In der Python-Konsole geben sie den Befehl `help('modules')` ein und erhalten so eine Liste der verfügbaren Module.

🎬 Details zu den Modulen erhalten sie beispielsweise mit `help('glob')`.

---

### Visual Studio Code installieren

Wir werden selber Python-Module erstellen und deshalb brauchen wir ein IDE-Upgrade.

🎬 Installatieren sie [Visual Studio Code](https://code.visualstudio.com/) auf ihrem Computer.

---

### VSCode Python-Erweiterung installieren

Visual Studio Code (VSCode) unterstützt verschiedene Programmiersprachen. Damit Python verwendet werden kann, braucht es eine Erweiterung.

🎬 Installatieren sie die [Python extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

Je nach dem müssen sie noch [Python](https://www.python.org/downloads/) installieren.

---

### Projektordner erstellen

VSCode stellt nicht nur einzelne Dateien dar, sonderrn ganze Ordner.

🎬 Führen sie diese Aktionen aus:
* Neuer Ordner `Thema7` erstellen
* Ordner mit VSCode öffnen

---

### Ordner mit VSCode öffnen

Wenn sie VSCode starten, sollten sie die Aktion *Open Folder ...* sehen.

![](../vscode-start.png)

---

### Hello.py erstellen

🎬 Erstellen sie im Ordner die Datei `Hello.py`

```
msg = "Hello World"
print(msg)
```

Es sollte dann so aussehen:

![](../vscode-hello.png)


---

### Python Interpreter bestimmen

Stellen sie sicher, dass VSCode den Python-Interpreter erkannt hat.

![](../vscode-python.png)

---

### Python-Code ausführen

🎬 Führen sie das Skript `Hello.py` mit dem dem Knopf oben rechts aus.

![](../vscode-execute.png)

Der Output des Skript wird unterhalb im *Terminal* angezeigt.

---

### Linx-Probleme beheben

Falls sie ein Linux-Computer haben, kann es gut sein, dass sie eine andere Shell verwenden müssen.

![](../Pasted%20image%2020220127192628.png)

---

### Wichtige Tastaturkürzel

Mit der Tastatur ist man immer schneller.

<kbd>ctrl</kbd>+ <kbd>shift</kbd> + <kbd>p</kbd>: VSCode-Befehle aufrufen

<kbd>ctrl</kbd> + <kbd>p</kbd>: Datei anzeigen

---

### Modul mit Funktion erstellen

Nun erstellen wir unser erstes Python-Modul.

🎬 Erstellen sie die Datei `lib.py` im geöffneten Ordner mit diesem Inhalt:

```py
def world():
	print('World')
```

---

### Modul importieren

🎬 Aktualisieren sie `Hello.py` mit diesem Inhalt und führen sie das Skript aus.

```py
import lib

msg = "Hello "
print(msg)
lib.world()
```

ℹ️ Sie haben die Funktion `world` aus dem Modul `lib` geladen.

---

### Modul mit mehreren Funktionen

Dasselbe funktioniert für mehrere Funktionen.

🎬 Aktualisieren sie `lib.py` mit diesem Inhalt:

```py
def world():
    print('World')

def hello():
    print('Hello')
```

ℹ️ Sie können Klassen auf dieselbe art in einem Modul bereitstellen.

---

### Nur Funktionen/Klassen importieren

🎬 Und so importieren sie mehre Funktionen in `Hello.py`:

```py
from lib import world,hello

hello()
world()
```

---

### Mehrere Module bündeln

Mehre Module können in einem Paket-Ordner gebündelt werden.

🎬 Erstellen sie im Projektordner ein Ordner `paket` mit zwei Dateien:

**paket/hello.py**

```py
def hello():
	return 'Hello '
```

**paket/world.py**

```py
def world():
	return 'World!'
```

**paket/__init__.py**

Datei leer lassen.

---

### Module aus Bündel importieren

🎬 Erstellen sie eine neue Datei `main.py` mit diesem Inhalt:

```py
from paket import hello, world

print(hello.hello(), world.world())
```

---

### Pakete, Module und mehr

Python-Pakete beinhalten Module und Module beinhalten Funktionen, Klassen oder weitere Python-Module.

Mit dem modularen Ansatz können komplexe Projektstrukturen erzeugt werden.

![](../complex.project.png)

---

## Python-Pakete

Bis anhain haben wir vorhandene Python-Pakete verwenden. Zusätzliche Python-Pakete können mit dem Python-Packet-Manager `pip` installiert werden.

---

### Python-Paket installieren

Wir möchten das Python-Paket [`cowsay`](https://pypi.org/project/cowsay/) installieren.

🎬 Öffnen sie das Terminal in VSCode und führen sie den Befehl `pip install cowsay` aus.

![](../pip-install-cowsay.png)

---

### Python-Paket importieren

🎬 Erweitern sie `main.py` mit:

```py
import cowsay
cowsay.cow('pip is great.')
```

Führen sie das Programm aus.

![](../Pasted%20image%2020220128114449.png)

---

### Installationsort der Pakete

Wo Pakete von pip instaliert werden, kann je nach Entwicklungsumgebung unterschiedlich sein. Mit dem Befehl `pip show cowsay` zeigt pip wo genau das Paket installiert wurde.

![](../pip-location.png)

---

### Aufgaben 1

Lösen sie die ersten zwei Aufgaben.

⚡Aufteilung in Gruppen/Breakout-Rooms ⏱️ 10 Minuten

Ziel: Aufgabe 7.1 und 7.2 gelöst.

---
