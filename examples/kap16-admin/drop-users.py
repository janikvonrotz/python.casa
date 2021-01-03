#!/usr/bin/env python3
from subprocess import run
from subprocess import CalledProcessError
try:
    with open('newusers.txt', 'rt') as f:
        for line in f:
            username = line.strip()  # entfernt Zeilenumbruch
            print('Delete', username)
            run(['userdel', '-r', username], check=True)
except CalledProcessError as ex:
    print('Fehler:', ex)

