#!/usr/bin/env python3

import urllib.request

try:
    url      = 'https://kofler.info'
    response = urllib.request.urlopen(url)
    # Download durchführen
    binary   = response.read()
    # Zeichensatz feststellen        
    cs  = response.headers.get_content_charset() 
    # Download in Zeichenkette umwandeln
    txt = binary.decode(cs)
    # die ersten 1000 Zeichen ausgeben
    print(txt[:1000])
except BaseException as ex:
    print('Fehler:', ex)
    




