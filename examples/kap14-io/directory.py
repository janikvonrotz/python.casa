#!/usr/bin/env python3
from pathlib import Path
import os
import tempfile

current = str(Path.cwd().absolute())
print('Aktuelles Verzeichnis:', current)

srcpath = Path(__file__).parent.absolute()
print('Code-Verzeichnis:', srcpath)

home = Path.home()
print('Heimatverzeichnis:', home)

tmp = tempfile.gettempdir()
print('Temporäres Verzeichnis:', tmp)

f = tempfile.NamedTemporaryFile(mode='w+t')
print('Temporäre Datei:', f.name)
f.write('Lorem ipsum')
f.close()   # löscht die temporäre Datei wieder

# relativ zum aktuellen Verzeichnis
# zwei Unterverzeichnisse erzeugen ...
try:
    subdir = Path('mydir/subdir')
    subdir.mkdir(exist_ok=True, parents=True)
except BaseException as err:
    print('Fehler beim Erzeugen des Verzeichnisses:', err)
    
# ... und wieder löschen
try:
    Path('mydir/subdir').rmdir()
    Path('mydir').rmdir()
except BaseException as err:
    print('Fehler beim Löschen des Verzeichnisses:', err)

# *.py-Dateien im aktuellen Verzeichnis suchen
print('glob *.py')
for p in Path.cwd().glob('*.py'):
    print('  ', p)
    
# *.py-Dateien im übergeordneten Verzeichnis und allen deren Subverzeichnissen suchen
print('glob **/*.py')
for p in Path.cwd().parent.glob('**/*.py'):
    print('  ', p)
    
    
