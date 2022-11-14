liste = ['Schwalbe', 'Kokosnuss', 13, 'Spam', 3.14]
liste[2] = 666 # Drittes Element wird mit neuem Wert überschreiben
len(liste) # Länge der Liste: 5
liste.append('Ni') # Neues Element wird angefügt
liste.extend([4, 5, 3.14]) # Liste wird mit Liste erweitert
liste.insert(2, 'Taube') # An dritter Stelle wird Element einfgügt.
liste.count(3.14) # Element kommt so oft vor: 2
liste.index(3.14) # An Position kommt Element vor: 5
liste.remove(3.14) # Erste Instanz von Element wird entfernt
liste.pop() # Letztes Element wird entfernt
liste.reverse() # Liste wird umgekehrt
sum([1,3,5]) # Direkte Summenbildung aus Liste