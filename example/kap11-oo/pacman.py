#!/usr/bin/env python3
class Player():
  # Konstruktor, initialisiert x und y mit Startposition
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  # Methoden zur Bewegung der Spielfigur
  def moveLeft(self):
    if self.x>0: # plus Test, dass keine Wand
      self.x-=1
      # Code, um Player auf dem Bildschirm neu zu zeichnen
      return True
    else:
      return False
  
  # analoger Code wie oben ...
  def moveRight(self): 
    if self.x<10: # plus Test, dass keine Wand
      self.x+=1
      # Code, um Player auf dem Bildschirm neu zu zeichnen
      return True
    else:
      return False
  
  def moveUp(self):    
    if self.y<10: # plus Test, dass keine Wand
      self.y+=1
      # Code, um Player auf dem Bildschirm neu zu zeichnen
      return True
    else:
      return False

  def moveDown(self): 
    if self.y>0: # plus Test, dass keine Wand
      self.y-=1
      # Code, um Player auf dem Bildschirm neu zu zeichnen
      return True
    else:
      return False
  
# Pacman-Objekt an der Position x=4, y=8 erzeugen
pacman = Player(4, 8)
ok = pacman.moveLeft()
ok = pacman.moveLeft()
ok = pacman.moveUp()
print('Aktuelle Position: %d %d' % (pacman.x, pacman.y))
