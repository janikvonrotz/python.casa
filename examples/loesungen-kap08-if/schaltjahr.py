#!/usr/bin/env python3
jahr = 2018
monat = 2

if jahr % 400 == 0:
    schaltjahr = True
elif jahr % 100 == 0:
    schaltjahr = False
elif jahr % 4 == 0:
    schaltjahr = True
else:
    schaltjahr = False
  
if monat in (1, 3, 5, 7, 8, 10, 12):
  tage = 31
elif monat in (4, 6, 9, 11):
  tage = 30
elif monat == 2:
  tage = 28 if schaltjahr else 29
else:
  print('Ungültiges Monat!')
  tage = 0

print('Das %d. Monat im Jahr %d hat %d Tage.' 
      % (monat, jahr, tage)) 
                
