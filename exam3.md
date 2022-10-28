# Leistungsnachweis

Ziel: Die Studierenden definieren ein Problem oder Projekt und lösen dieses mithilfe eines selbstgeschriebenen Programms.

Aufwand: 8 Stunden\
Anteil Gesamtnote: 50%

## Durchführung

Der Prozess für den Leistungsnachweis sieht wie folgt aus:
1. Studierende suchen sich eine Problemstellung oder Thema, dass Sie mit einem Python-Programm lösen möchten
2. Die Studierenden formulieren dazu einen Projektvorschlag und laden diesen auf Moodle
3. Der Dozierende gibt ein Feedback und teilt mir, ob der Projektvorschlag den Erwartungen gerecht wird
4. Die Studierenden haben Zeit um den Leistungsnachweis zu erarbeiten und eine Dokumentation zu erstellen
5. Der Dozierende gibt Inputs und kann bei Problemen kontaktiert werden
6. Die Studierenden laden das Resultat auf Moodle hoch
7. Der Dozierende macht eine Bewertung anhand der [Kriterien](#Kriterien)

## Resultat

Auf [Moodle](https://moodle.medizintechnik-hf.ch/mod/assign/view.php?id=6716) geben Sie zwei Dateien ab:
* `Code.zip`: Python-Programm (gezippter Ordner mit Pyton-Dateien)
* `Dokumentation.{pdf,epub,docx}:` Dokumentation zum Programm (4-8 Seiten, ohne Cover)

## Themenwahl

Hier einige Ideen für Projekte:

| Titel                                                                                                                                                            | Schwierigkeitsgrad |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| Suche nach bestimmten Begriffen in [Log-Dateien](https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs)        |                    |
| Wort mit LED und Raspberry Pi als Morsecode ausgeben                                                                                                             |                    |
| Daten aus Postgres Datenbank lesen und schreiben                                                                                                                 |                    |
| Wetter-Informationen abrufen und als HTML-Dokument ausgeben                                                                                                      |                    |
| Tweet von Twitter-Account anzeigen lassen                                                                                                                        |                    |
| Datei auf Dropbox speichern                                                                                                                                      |                    |
| Textbasiertes Hangman                                                                                                                                            |                    |
| Detektion von Herzfrequenz anhand [EKG-Daten](https://github.com/janikvonrotz/python.casa/blob/main/ekg-data..csv)                                               |                    |
| Temperaturdaten ploten und Min/Max bestimmen. Daten von  [https://sarneraa.huetstock.ch](https://sarneraa.huetstock.ch) können auf Anfrage bereitgestellt werden |                    |
| Passwortgenerator gemäss [xkcd-Comic](https://xkcd.com/936/)                                                                                                     |                    |
| Covid-Daten mit Python verarbeiten und als HTML-Bericht präsentieren                                                                                                                                                                 |                    |

## Projektvorschlag

Der Projektvorschlag wird auf Moodle mitgeteilt und besteht im wesentlichen aus einem Titel und einer kurzen Beschreibung (~100 Wörter).

![](./moodle-kurs.png)

## Dokumentation

Kapitelüberschriften der Dokumentation:

* **Einleitung**: Um was geht es in diesem Dokument?
* **Problemstellung**: Beschreibung des Problems.
* **Vorgehen**: Vorgehen um das Problem zu lösen. Visualisierung mittels Flowchart.
* **Umsetzung**: Wie wurde die Lösung effektiv implementiert? Beschreibung der wichtigsten Programm-Teile.
* **Rückblick**: Gab es Problem bei der Umsetzung? Was lief gut und was nicht?
* **Technische Anleitung**: Wie kann man das Program ausführen? Welche Vorbereitungen müssen getroffen werden?

::: tip
Auf <https://carbon.now.sh/> kann man seinen Code einfügen und als Bild darstellen lassen.

Mit [draw.io](https://draw.io) kann man Flowcharts erstellen und so den Code dokumentieren.
:::

Eine Vorlage für ein `.docx` kann [hier heruntergeladen](https://janikv.cloud/s/KaJ7zTdETxr8HAK) werden.

## Kriterien

Punkte in eckigen Klammern.

### Dokumentation

Punkte: 9

* **Vollständigkeit \[1\]**: Alle Kapitel gemäss Vorgaben sind enthalten.
* **Formatierung \[1\]**: Die Formatierung des Dokuments enspricht einem professionellen Standard.
* **Sprache \[2\]**: Die Dokumentation ist in korrektem Deutsch formuliert und Fachwörter werden korrekt verwendet.
* **Visualisierung \[3\]**: Der Code ist mithilfe einem Flowchart visualisiert. (Formatierung, Vollständigkeit, Logik)
* **Reflexion \[2\]**: Die konfrontierten Herausforderungen und der entsprechende Lerneffekt sind reflektiert.

### Code

Punkte: 17

* **Kommentare \[2\]**: Die Code-Anweisungen und Blöcke sind sinnvoll und vollständig kommentiert.
* **Struktur \[6\]**: 
	* Der Code ist sinnvoll strukturiert (Module und Funktionen).
	* Die Variablen, Dateien und Ordner sind gemäss ihrer Funktion benannt.
	* Die Formatierung des Codes unterstützt die Lesbarkeit.
* **Authentizität \[2\]**: Der Code ist selber verfasst. Code-Teile von Dritten werden als solche deklariert.
* **Ausführbar \[2\]**: Der Code kann gemäss "Technische Anleitung" ausgeführt werden.
* **Optimierung \[2\]**: Schleifen und Funktionen werden genutzt.
* **Komplexität \[3\]**: Die Problemstellung entspricht HF-Niveau.