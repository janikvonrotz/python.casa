#!/usr/bin/env python3
from pathlib import Path
home = Path.home()
sum = 0
cnt = 0
for file in home.glob('**/*.py'):
    print(file, file.stat().st_size)
    sum += file.stat().st_size
    cnt += 1

print('Insgesamt', cnt, 'Dateien')
print('Gesamtgröße:', sum, 'Byte')    
    
