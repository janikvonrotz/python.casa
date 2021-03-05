try:
    f = open('test.txt', 'wt') # Textdatei erstellen mit Berechtigungen
    f.write('Lorem ipsum dolor sit amet, ...\n')
    f.write('Unicode äöüß\n')
    f.close()
  
except BaseException as err:
    print('Fehler:', err)