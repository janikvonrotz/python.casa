#!/usr/bin/env python3
try:
    # Datei readme.txt öffnen
    f = open('readme.txt')
    # alle Zeilen der Datei lesen und ausgeben
    for line in f:
        print(line, end='')
except BaseException as err:
    print('Es ist ein Fehler aufgetreten:', err)
finally:
    if 'f' in locals() and f: 
        f.close()
