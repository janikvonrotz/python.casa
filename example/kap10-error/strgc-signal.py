#!/usr/bin/env python3
import signal, sys

# Abbruchfunktion
def abbruch(signal, frame):
    # Aufräumarbeiten
    print('Strg+C wurde gedrückt, Programmende')
    sys.exit(0)

# Signal-Handler einrichten
signal.signal(signal.SIGINT, abbruch)

# Endlosschleife
cnt=0
while 1:
    cnt+=1
    print(cnt)
