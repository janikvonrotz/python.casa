#!/usr/bin/env python3

try:
    # in eine Textdatei schreiben
    with open('testfile.txt', 'wt') as f1:
        f1.write('Lorem ipsum dolor sit amet, ...\n')
        f1.write('Unicode äöüß\n')

    # Textdatei zeilenweise auslesen
    with open('testfile.txt', 'rt') as f2:
        for line in f2:
            print(line, end='')

except BaseException as err:
    print('Fehler:', err)
