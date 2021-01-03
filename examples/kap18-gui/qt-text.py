#!/usr/bin/env python3
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit, QMessageBox
from PyQt5.QtCore import QSize    

class MyWindow(QMainWindow):
    def __init__(self):
        global txts
        
        # Konstruktor von QMainWindow aufrufen
        super().__init__()

        # Fenstergröße und Titel einstellen
        self.setMinimumSize(QSize(350, 200))    
        self.setWindowTitle('Textfelder im Grid-Layout') 

        # Grid-Layout für Widget in Main-Window (Layout von
        # Main-Window kann nicht verändert werden)
        wid = QWidget(self)
        self.setCentralWidget(wid)
        grid = QGridLayout()
        wid.setLayout(grid)
        
        # erste Reihe: Beschriftung
        row = 0
        for s in ['Name', 'E-Mail', 'Passwort',
                  'Passwort (Wiederholung)']:
            lbl = QLabel(s)
            lbl.resize(lbl.sizeHint())
            grid.addWidget(lbl, row, 1, QtCore.Qt.AlignRight)
            row += 1 

        # zweite Reihe: Textfelder
        for row in range(4):
            txt = QLineEdit()
            if row >= 2:
                txt.setEchoMode(QLineEdit.Password)
            grid.addWidget(txt, row, 2)
            txts += [txt]
            row += 1 

        # fünfte Zeile: Buttons
        b = QPushButton('Abbrechen')
        b.clicked.connect(self.cancel)
        grid.addWidget(b, 4, 1, QtCore.Qt.AlignRight)
        b = QPushButton('OK')
        b.clicked.connect(self.ok)
        grid.addWidget(b, 4, 2, QtCore.Qt.AlignLeft)

    # Abbrechen-Button: Programmende
    def cancel(self):
        app.quit()
        
    # OK-Button: Textfelder auswerten
    def ok(self):
        if txts[0].text().strip() == '':
            QMessageBox.about(self, 'Fehler', 'Geben Sie Ihren Namen an!')
            return
        if txts[1].text().strip() == '': 
            QMessageBox.about(self, 'Fehler', 'Geben Sie Ihre E-Mail-Adresse an!')
            return
        if txts[2].text() != txts[3].text(): 
            QMessageBox.about(self, 'Fehler', 'Die Passwörter stimmen nicht überein!')
            return
        if len(txts[2].text())<8:
            QMessageBox.about(self, 'Fehler', 'Die Passwörter sind zu kurz!')
            return
        # alles OK: Daten ausgeben, Ende
        print(txts[0], txts[1], txts[2])
        app.quit()
                    
        
# Fenster öffnen; das Programm läuft, bis das
# Fenster geschlossen wird
txts = []
app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
