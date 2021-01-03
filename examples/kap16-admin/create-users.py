#!/usr/bin/env python3
from subprocess import run
from subprocess import CalledProcessError
from secrets import choice
pwchars = 'abcdefghijklmnopqrstuvwxyz0123456789'
try:
    with open('newusers.txt', 'rt') as fin, \
         open('user-pw.txt', 'wt') as fout:
        for line in fin:
            username = line.strip()  # entfernt Zeilenumbruch
            pw = ''.join(choice(pwchars) for _ in range(9))
            pwstr = username + ':' + pw
            print(pwstr)
            fout.write(pwstr + '\n')
            run(['useradd', username], check=True)
            # Alternative zum 2. run-Kommando
            # pwdata = bytes(pwstr + '\n', 'utf-8')
            # subprocess.run(['chpasswd'], input=pwdata, check=True)
            run('echo %s | chpasswd' % (pwstr), shell=True, check=True)
            run(['chage', '-d 0', '-E 2020-12-31', username], check=True)
except CalledProcessError as ex:
    print('Fehler:', ex)        
