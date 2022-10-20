from pathlib import Path
current = Path.cwd() # Gibt das aktuelle Verzichnis wo das Skript ausgeführt wird
print('Aktuelles Verzeichnis:', current.absolute())

print(type(current))
print('Aktueller Verzeichnisname:', current.name)