#!/usr/bin/env python3
import locale, platform
if platform.system() == 'Windows':
    locale.setlocale(locale.LC_ALL, 'german')
if platform.system() == 'Linux':
    locale.setlocale(locale.LC_ALL, 'de_DE.utf8')
else:
    locale.setlocale(locale.LC_ALL, 'de_DE.UTF8')
    
s = input('Länge des Rechtecks: ')
laenge = locale.atof(s)
s = input('Breite des Rechtecks: ')
breite = locale.atof(s)
flaeche = laenge * breite
s = locale.format_string('%.2f', flaeche)
print('Flächeninhalt: ', s)
