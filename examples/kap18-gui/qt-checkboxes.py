#!/usr/bin/env python3
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QCheckBox, QRadioButton
from PyQt5.QtCore import QSize    

class MyWindow(QMainWindow):
    def __init__(self):
        global checkboxes, radios
        # Konstruktor von QMainWindow aufrufen
        super().__init__()

        # Fenstergröße und Titel einstellen
        self.setMinimumSize(QSize(300, 200))    
        self.setWindowTitle('Optionen') 

        for i in range(1, 6):
            c = QCheckBox('Checkbox %d' % (i), self)
            c.resize(100, 25)
            c.move(20, 30 * i)
            checkboxes += [c]
            c.toggled.connect(self.toggled)
            
            r = QRadioButton('Button %d' % (i), self)
            r.resize(100, 25)
            r.move(180, 30 * i)
            radios += [r]
            r.toggled.connect(self.toggled)
            
    # Reaktion auf Status-Änderung
    def toggled(self):
        c = self.sender()
        print(c.text(), c.isChecked())
    
# Fenster öffnen; das Programm läuft, bis das
# Fenster geschlossen wird
app = QtWidgets.QApplication([])
checkboxes = []
radios = []
win = MyWindow()
win.show()
app.exec_()

# vor dem Programmende den Zustand aller Optionen
# ausgeben
for c in checkboxes:
    print(c.text(), c.isChecked())
for r in radios:
    print(r.text(), r.isChecked())

        