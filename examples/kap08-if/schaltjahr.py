#!/usr/bin/env python3
jahr = 2018

if jahr % 400 == 0:
    schaltjahr = True
elif jahr % 100 == 0:
    schaltjahr = False
elif jahr % 4 == 0:
    schaltjahr = True
else:
    schaltjahr = False
  
if schaltjahr:
    print(jahr, 'ist ein Schaltjahr.')
else:
    print(jahr, 'ist kein Schaltjahr.')