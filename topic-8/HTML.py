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

# HTML-Code generieren
html = doc.getvalue()

# HTML-Dokument schreiben
with open('example.html', 'w') as file:
    file.write(html)

# Die HTML-Dokument im Browser aufrufen
import webbrowser
from pathlib import Path
webbrowser.open('file://' + str(Path('example.html').absolute()))