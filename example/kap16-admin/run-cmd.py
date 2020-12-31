#!/usr/bin/env python3
import subprocess
from subprocess import PIPE
from subprocess import CalledProcessError

# führt ls aus; die Ausgaben erscheinen im Terminal
result = subprocess.run(['ls', '-l'])

# wie oben, aber die Ausgaben können in Python verarbeitet werden
result   = subprocess.run(['ls', '-l'], stdout=PIPE, stderr=PIPE)
output   = result.stdout
errormsg = result.stderr
for line in output.decode('utf-8').splitlines():
    print('Ergebnis:', line)    


# Kommando in der Shell ausführen, um das Pipe-Zeichen | ...
result = subprocess.run('dmesg | grep -i eth', 
  stdout=PIPE, stderr=PIPE, shell=True)
print('Shell1:\n', result.stdout.decode('utf-8'))  

# ... sowie Joker-Zeichen zu nutzen
result = subprocess.run('ls -l *.py',   
  stdout=PIPE, stderr=PIPE, shell=True)
print('Shell2:\n', result.stdout.decode('utf-8'))  

# mit Fehlerabsicherung
try:
    result = subprocess.run('lsabc', shell=True, check=True, stdout=PIPE, stderr=PIPE)
    exitcode = result.returncode
    if exitcode != 0:
        print('Fehlercode', exitcode)
    else:
        print('Alles bestens, Rückgabecode', exitcode)
except OSError as ex:
    print('OSError-Exception', ex)
except CalledProcessError as ex:
    print('CalledProcessError-Exception', ex)

    
