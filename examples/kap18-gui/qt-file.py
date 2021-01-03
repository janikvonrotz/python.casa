#!/usr/bin/env python3
import os, sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QGridLayout, QLabel, QFileDialog
from PyQt5.QtCore import QSize    

class MyWindow(QMainWindow):
    def __init__(self):
        global txts
        
        # Konstruktor von QMainWindow aufrufen
        super().__init__()

        # Fenstergröße und Titel einstellen
        self.setMinimumSize(QSize(450, 150))    
        self.setWindowTitle('Dateiauswahl') 

        # Grid-Layout für Widget in Main-Window (Layout von
        # Main-Window kann nicht verändert werden)
        wid = QWidget(self)
        self.setCentralWidget(wid)
        grid = QGridLayout()
        wid.setLayout(grid)
        
        # erste Reihe: Beschriftungs-Label
        row = 0
        for s in ['Dateiname:', 'Größe:', 'Anzahl der Zeilen:']:
            lbl = QLabel(s)
            lbl.resize(lbl.sizeHint())
            grid.addWidget(lbl, row, 1, QtCore.Qt.AlignRight)
            row += 1 

        # zweite Reihe: Label für Dateiname, -größe und Zeilen
        self.lbls = []  # Referenzen auf Label hier speichern
        for row in range(3):
            self.lbls += [QLabel('---')]
            grid.addWidget(self.lbls[row], row, 2)

        # vierte Zeile: Buttons
        b = QPushButton('Datei auswählen')
        b.clicked.connect(self.select)
        grid.addWidget(b, 3, 1, QtCore.Qt.AlignRight)
        b = QPushButton('Ende')
        b.clicked.connect(self.quit)
        grid.addWidget(b, 3, 2, QtCore.Qt.AlignLeft)

    # Ende-Button: Programmende
    def quit(self):
        app.quit()
        
    # Dateiauswahl-Button: 
    def select(self):
        (fname, _) = QFileDialog.getOpenFileName(self)
        if fname != '':
            self.lbls[0].setText(fname)
            try:
                size = os.path.getsize(fname)
                self.lbls[1].setText(
                    '%d Byte' % (size))
                with open(fname, 'rt') as f:
                    n = len(f.readlines())
                    self.lbls[2].setText(
                        '%d Zeilen' % (n))
            except BaseException as ex:
                print('Fehler', ex)
            
        
# Fenster öffnen; das Programm läuft, bis das
# Fenster geschlossen wird
app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
