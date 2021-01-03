#!/usr/bin/env python3
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget
from PyQt5.QtCore import QSize    

class MyWindow(QMainWindow):
    def __init__(self):
        # Konstruktor von QMainWindow aufrufen
        super().__init__()

        # Fenstergröße und Titel einstellen
        self.setMinimumSize(QSize(300, 100))    
        self.setWindowTitle('Hello, Qt!') 

        # Title-Widget erzeugen und in Fenster einbetten
        title = QLabel('Hello, Qt!', self) 
        title.setAlignment(QtCore.Qt.AlignCenter) 
        self.setCentralWidget(title)

# Fenster öffnen; das Programm läuft, bis das
# Fenster geschlossen wird

# 'offizielle' Variante
# app = QtWidgets.QApplication(sys.argv)
# mainWin = MyWindow()
# mainWin.show()
# sys.exit( app.exec_() )

# einfachere Variante
app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
