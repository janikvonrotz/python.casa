#!/usr/bin/env python3
import xml.etree.ElementTree as ET
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QGridLayout, QLabel, QListWidget, QComboBox
from PyQt5.QtCore import QSize    

# Klasse für Fenster
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(250, 100))    
        self.setWindowTitle('Länderauswahl') 

        # Grid-Layout
        wid = QWidget(self)
        self.setCentralWidget(wid)
        grid = QGridLayout()
        wid.setLayout(grid)
        
        # ComboBox initialisieren
        self.cb = QComboBox()
        for c in countries:
            self.cb.addItem(c[0])
        self.cb.currentIndexChanged.connect(self.comboIndexChanged)
        grid.addWidget(self.cb, 1, 1)

        # zwei Labels und ein 'Ende'-Button
        self.lbl1 = QLabel('---')
        grid.addWidget(self.lbl1, 2, 1)
        self.lbl2 = QLabel('---')
        grid.addWidget(self.lbl2, 3, 1)
        b = QPushButton('Ende')
        b.clicked.connect(self.quit)
        grid.addWidget(b, 4, 1, QtCore.Qt.AlignRight)

    # ComboBox-Auswahl
    def comboIndexChanged(self, index):
        self.lbl1.setText('Auswahl: ' + countries[index][0])
        self.lbl2.setText(countries[index][1] + ' / ' + 
                          countries[index][2])

    # Ende-Button: Programmende
    def quit(self):
        app.quit()        

# Ländercodes in Liste einlesen
tree = ET.parse('countries.xml')
root = tree.getroot()
countries = [ (c.text, c.attrib['code'], c.attrib['iso']) for c in root]

# Programmende, wenn Fenster geschlossen wird        
app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
