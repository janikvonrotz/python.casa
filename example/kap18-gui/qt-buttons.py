#!/usr/bin/env python3
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton
from PyQt5.QtCore import QSize    

class MyWindow(QMainWindow):
    def __init__(self):
        # Konstruktor von QMainWindow aufrufen
        super().__init__()

        # Fenstergröße und Titel einstellen
        self.setMinimumSize(QSize(300, 100))    
        self.setWindowTitle('Buttons') 

        # Button-Widgets erzeugen und in Fenster einbetten
        b1 = QPushButton('Button 1', self) 
        b1.move(50, 30)
        b1.resize(120, 25)
        b1.clicked.connect(self.clicked1)
        # Größe eines Widgets ermitteln
        # print(b1.geometry().width(), b1.geometry().height())
        
        b2 = QPushButton('Button 2 (Programmende)', self) 
        b2.move(50, 60)
        b2.resize(b2.sizeHint())
        b2.clicked.connect(self.clicked2)

    def clicked1(self):
        print('Button 1 wurde angeklickt.')
    
    def clicked2(self):
        print('Button 2 wurde angeklickt.')
        print('Programmende.')
        app.quit()

# Fenster öffnen; das Programm läuft, bis das
# Fenster geschlossen wird
app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
