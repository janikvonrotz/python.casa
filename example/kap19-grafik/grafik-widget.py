#!/usr/bin/env python3
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt, QSize

# Klasse für Fenster
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(300, 300))    
        self.setWindowTitle('Grafik in einem Widget') 

        # Button-Widgets
        b1 = QPushButton('Ende', self) 
        b1.move(230, 270)
        b1.resize(70, 25)
        b1.clicked.connect(self.clicked1)
        
        # Widget für Grafik erzeugen
        self.mw = MyWidget(self) 
        self.mw.move(10, 10)
        self.mw.resize(280, 250)

    def clicked1(self):
        # Bitmap speichern
        bitmap = self.mw.grab()
        bitmap.save('test.png')

        print('Programmende.')
        app.quit()

# Klasse für eigenes Widget
class MyWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

    # Paint-Event für das Widget
    def paintEvent(self, event):
        p = QPainter()  
        p.begin(self)
        w = self.geometry().width()
        h = self.geometry().height()
        p.setRenderHint(QPainter.Antialiasing)
        # weißer Hintergrund
        p.setPen(Qt.NoPen)
        p.setBrush(QBrush(Qt.white))
        p.drawRect(0, 0, w, h)
        # einfaches Muster zeichnen
        max = 50
        p.setPen(QPen(Qt.blue, 1))
        for i in range(max + 1):
            p.drawLine(0, h / max * i, w - w / max * i, 0)
        p.end() 
        
# Fenster öffnen; das Programm läuft, bis das
# Fenster geschlossen wird
app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
