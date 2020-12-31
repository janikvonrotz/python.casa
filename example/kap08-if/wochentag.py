#!/usr/bin/env python3
tag = 3   # 1 = Montag, ..., 7 = Sonntag
if tag in (1, 2, 3, 4, 5):
    print('arbeiten ...')
elif tag in (6, 7):
    print('wochenende')
else:
    print('ungültig')

if tag==1:
  s = 'Montag'
elif tag==2:            
  s = 'Dienstag'
elif tag==3:            
  s = 'Mittwoch'
elif tag==4:            
  s = 'Donnerstag'
elif tag==5:            
  s = 'Freitag'
elif tag==6:            
  s = 'Samstag'
elif tag==7:            
  s = 'Sonntag'
else:
  s = 'ungültig'  
print("Wochentag:", s)

alletage = { 1: 'Montag', 2: 'Dienstag', 3: 'Mittwoch', 
  4: 'Donnerstag', 5: 'Freitag', 6: 'Samstag', 
  7: 'Sonntag'}
if tag in alletage:
  s = alletage[tag]
else:
  s = 'ungültig'
print("Wochentag:", s)  