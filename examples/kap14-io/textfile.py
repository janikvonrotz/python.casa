#!/usr/bin/env python3

try:
    # in eine Textdatei schreiben
    f1 = open('testfile.txt', 'wt')
    f1.write('Lorem ipsum dolor sit amet, ...\n')
    f1.write('Unicode äöüß\n')
    f1.close()

    # Textdatei zeilenweise auslesen
    f2 = open('testfile.txt', 'rt')
    for line in f2:
        print(line, end='')
    f2.close()
except BaseException as err:
    print('Fehler:', err)
