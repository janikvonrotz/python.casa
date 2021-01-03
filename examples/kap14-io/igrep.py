#!/usr/bin/env python3
import sys

# Verwendung: igrep suchbegriff 
# liest aus Standardeingabe,
# schreibt an die Standardausgabe

if len(sys.argv) != 2:
    print('Sie müssen genau ein Argument übergeben!')
    sys.exit(1)

pattern = sys.argv[1].lower()

for line in sys.stdin:
    if pattern in line.lower():
        sys.stdout.write(line)
