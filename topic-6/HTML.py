from yattag import Doc

doc, tag, text = Doc().tagtext() # HTML-Funktionen abrufen

with tag('html'): # HTML-Dokumente mit den Elementen zusammenstellen
    with tag('body'): # Mit with werden Funktionsaufrufe aneinander gereiht
        with tag('p', id = 'main'):
            text('Beispiel')
        with tag('a', href='https://example.com'):
            text('Linktext')

html = doc.getvalue() # HTML-Code generieren