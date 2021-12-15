# Übungen Thema 1

## Aufgaben

Aufgaben zum Thema.

### Aufgabe 1.1: Input, Process and Output

Erstellen sie ein Programm, das nach ihrem Namen fragt und diesen in Grossbuchstaben wieder ausgibt. Suchen sie im Internet nach `Python Grossbuchstaben` um eine HIlfestellung zu finden.

> Kopieren sie den Code nicht! Schreiben sie jedes Zeichen und Anweisung, nur so finden sie auch die Zeichen auf der Tastatur. 

:::tip
Setzen sie nach `name` die folgende Funktion an `.upper()`. 
:::

### Aufgabe 1.2: Kommentieren

Fügen sie zu jeder Anweisung des Programs aus Aufgabe 1 einen Kommentar hinzu.

### Aufgabe 1.3: VS Code IDE

Installieren sie den IDE-Editor [VS Code](https://code.visualstudio.com/). Öffnen sie ein Skript führen sie es mit VS Code aus.

Video: [Visual Studio Code für Windows installieren](https://www.youtube.com/watch?v=og51Lo5uKBA)

## Wiederholungsfragen

Wiederholungsfragen zum Thema.

* **W1**: Python-Scripts werden durch einen Interpreter ausgeführt. Was bedeutet das?

<details>
Python-Scripts müssen vor der Ausführung nicht kompiliert werden. Stattdessen liest python.exe bzw. python3 den Code (also gewissermaßen einen Text mit Python-Anweisungen) direkt aus der Script-Datei und führt ihn aus. python.exe bzw. python3 werden deswegen als Interpreter bezeichnet.
</details>

* **W2**: Welche Voraussetzungen müssen erfüllt sein, damit Python-Programme unter Windows gestartet werden können?

<details>
Das Python-Script muss die Endung *.py aufweisen. Außerdem muss natürlich Python (also das Programm python.exe) installiert sein.
</details>

* **W3**: Welche Voraussetzungen müssen erfüllt sein, damit Python-Programme unter Linux oder macOS gestartet werden können?

<details>
Das Shebang muss im Datei Header sein.
Die Datei muss ausführbar sein (chmod +x)
Python installiert und das Skript ist im Arbeitsordner.
</details>

* **W4**: Sind in Python mehrzeilige Anweisungen möglich?

<details>
Mehrzeilige Anweisungen sind möglich. Bei offenen Klammern ist in mehrzeiligen Anweisungen nicht einmal eine Kennzeichnung notwendig. Wenn aus der Struktur des Codes hingegen nicht klar hervorgeht, dass die aktuelle Zeile unvollständig ist und in der nächsten Zeile fortgesetzt wird, dann müssen Sie das Zeichen \ als Indikator für die mehrzeilige Konstruktion verwenden.
</details>

* **W5**: Wie können Sie mehrere Anweisungen in einer Zeile durchführen?

<details>
Um mehrere Anweisungen in einer Zeile auszuführen, trennen Sie sie durch Semikola – also z. B. a=3; print(a).
</details>

* **W6**: Welche Bedeutung hat eingerückter Code?

<details>
In Python wird die Struktur von Code in Verzweigungen, Schleifen und Funktionen nicht durch geschwungene Klammern definiert, sondern durch Einrückungen. Die Einrückungen sind daher zwingend erforderlich. Die übliche Einrücktiefe beträgt vier Zeichen pro Ebene.
</details>

* **W7**: Wie können Sie bei print den Zeilenumbruch nach der Ausgabe verhindern?

<details>
print(x, end='') gibt den Inhalt der Variablen x ohne einen nachfolgenden Zeilenumbruch aus.
</details>

* **W8**: Wie werden in Python Kommentare formuliert?

<details>
Kommentare werden in Python mit dem Zeichen # eingeleitet und gelten bis zum Ende der Zeile. Mehrzeilige Kommentare beginnen wie mehrzeilige Zeichenketten mit """ und enden mit """.
</details>

::: tip
Um Frage 7 zu beantworten folgender Hinweis: `help('print')`
:::

## Mehr zum Thema

* [Die Programmiersprache Python](http://openbook.rheinwerk-verlag.de/python/02_001.html#u2)