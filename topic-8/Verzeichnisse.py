from pathlib import Path
current = Path.cwd() # cwd bedeutet Current Work Directory, sprich das aktuelle Arbeitsverzeichnis
print('Aktuelles Verzeichnis:', current.absolute())

print(type(current)) # Ausgabe Objekttyp
print('Aktueller Verzeichnisname:', current.name)