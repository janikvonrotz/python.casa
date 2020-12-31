#!/usr/bin/env python3
try:
    # Endlosschleife
    cnt=0
    while 1:
        cnt+=1
        print(cnt)
except KeyboardInterrupt:
    # Aufräumarbeiten ...
    print('Strg+C wurde gedrückt, Programmende')
