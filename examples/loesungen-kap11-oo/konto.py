#!/usr/bin/env python3
class Konto():
    def __init__(self, name, startguthaben=0, rahmen=0):
        self.__name = name
        self.__guthaben = startguthaben
        self.__rahmen = rahmen

    def einzahlen(self, betrag):
        if betrag<=0:
            raise ValueError('Ungültige Parameter!')
        self.__guthaben += betrag
            
    def abheben(self, betrag):
        if betrag<=0:
            raise ValueError('Ungültige Parameter!')
        if betrag > self.__guthaben + self.__rahmen:
            print('Zuwenig Geld am Konto.')
            return False
        else:
            self.__guthaben -= betrag
            return True
            
    def __str__(self):
        s = 'Konto von %s:\n  Guthaben: %d\n' + \
            '  Überziehungsrahmen: %d\n'
        return s % (self.__name, self.__guthaben, self.__rahmen)
            
k1 = Konto('Michael', 200, 0)
k2 = Konto('Maria')
k3 = Konto('Peter', 1000, 500)
k1.einzahlen(100)
if k2.abheben(100):
  print('Geld von Konto 2 abgehoben')
if k3.abheben(1200):
  print('Geld von Konto 3 abgehoben')
for k in [k1, k2, k3]:
  print(k)
