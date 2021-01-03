#!/usr/bin/env python3
import time, locale
name = input('Geben Sie Ihren Namen an: ')
print('Hallo %s!' % name)
# Datum und Zeit in aktueller Lokalisierung
# (Hinweis: die Lokalisierung funktioniert nicht, 
#  wenn Sie das Script in Thonny ausführen)
locale.setlocale(locale.LC_ALL, '')
time = time.strftime('Heute ist %A der %d. %B.')
print(time)
