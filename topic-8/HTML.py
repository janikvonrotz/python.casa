from yattag import Doc

# HTML-Funktionen abrufen
doc, tag, text = Doc().tagtext()

# HTML-Dokument mit Elementen erstellen
with tag('html'):
    with tag('body'):
        with tag('p', id = 'main'):
            text('Beispiel')
        with tag('a', href='https://example.com'):
            text('Linktext')

html = doc.getvalue() # HTML-Code generieren

with open('example.html', 'wt') as file:
    file.write(html)

# Die HTML-Datei im Browser aufrufen
import webbrowser
from pathlib import Path
webbrowser.open('file://' + str(Path('example.html').absolute()))