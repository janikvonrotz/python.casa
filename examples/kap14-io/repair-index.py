#!/usr/bin/env python3
from pathlib import Path

# eine Zeile auswerten, gegebenenfalls \index-Eintrag
# ändern und zurückgeben
def transform(s):
    # wenn kein Indexeintrag: unverändert zurückgeben
    if not s.startswith(r'\index{'):
        return s
    
    # \index{*-Funktion/Methode/Variable/...}
    keywords = {'Funktion', 'Methode', 'Variable', 
      'Klasse', 'Eigenschaft', 'Typ', 'Datentyp', 
      'Dekorator', 'Anweisung', 'Schlüsselwort'}
    for word in keywords:
        if '-' + word + '}' in s:
            new = s.replace('-' + word, ' (' + word + ')')
            print(' - ', s, ' + ', new, end='', sep='')
            return new
    
    # \index{*-Modul}
    if '-Modul}' in s:
        pos = s.find('-Modul}')
        new1 = r'\index{Module!' + s[7:pos] + '}\n'
        new2 = s.replace('-Modul', ' (Modul)')
        print(' - ', s, ' + ', new1, ' + ', new2, end='', sep='')
        return new1 + new2
        
    # Index-Eintrag unverändert lassen
    return s
        

# Schleife über alle *.md-Dateien
for md in Path.cwd().glob('*.md'):
    print('\nBearbeite', md.name)
    # Backup erstellen
    bak = md.with_suffix('.bak')
    md.rename(bak)
    
    # Backup lesen, in neue *.md-Datei schreiben
    with open(bak, 'rt') as fin, \
         open(md, 'wt') as fout:
        # Datei zeilenweise verarbeiten
        for line in fin:
            fout.write(transform(line))
            
    
    
    
