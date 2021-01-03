#!/usr/bin/env python3

def pwquality(s):
  if len(s)<8:
    return 0
  q = 1
  
  # >6 unterschiedliche Zeichen
  if len(set(s)) > 6: q+=1
  
  # Groß- und Kleinbuchstaben, Ziffern, Sonderzeichen
  hasdigit = False
  hasspecial = False
  hasupper = False
  haslower = False
  for c in s:
    if str.isupper(c): hasupper = True
    if str.islower(c): haslower = True
    if str.isdigit(c): hasdigit = True
    if not str.isalnum(c): hasspecial = True
  if hasupper and haslower: q+=1
  if hasdigit: q+=1
  if hasspecial: q+=1
  
  # Ergebnis zurückgeben
  return q

# Funktion für einige Zeichenketten testen        
tst = ['abc', 'abcdefghij', 'ab1122$$!!', 'abcd1234$!']
for p in tst:
  print('%s:\t%d Punkte' % (p, pwquality(p)))
