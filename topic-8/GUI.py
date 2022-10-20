import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget             
from PyQt5.QtCore import QSize

class MeinFenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(QSize(300, 100)) # Fenstergröße und Titel einstellen
        self.setWindowTitle('Hello, Qt!') # Fenstertitel festlegen

        title = QLabel('Hello, Qt!', self) # Label definieren
        title.setAlignment(QtCore.Qt.AlignCenter) # Label mittig in Fenster anzeigen
        self.setCentralWidget(title)

App = QtWidgets.QApplication(sys.argv) 
Fenster = MeinFenster() 
Fenster.show() # Fenster anzeigen
sys.exit(App.exec_())