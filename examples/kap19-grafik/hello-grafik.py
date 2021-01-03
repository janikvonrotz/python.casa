#!/usr/bin/env python3
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush, QPolygon, QFont
from PyQt5.QtCore import Qt, QSize, QPoint, QRect

class MyWindow(QMainWindow):
    def __init__(self):
        # Konstruktor von QMainWindow aufrufen
        QMainWindow.__init__(self)

        # Fenstergröße und Titel einstellen
        self.setMinimumSize(QSize(500, 500))    
        self.setWindowTitle('Mein erstes Grafikprogramm') 
        

    def paintEvent(self, event):
        p = QPainter()
        p.begin(self)
        # Antialiasing aktivieren
        p.setRenderHint(QPainter.Antialiasing)
        # Linie zeichnen
        blue = QColor(0, 0, 255)
        p.setPen(QPen(blue, 3))
        p.drawLine(10, 10, 200, 100) # x1, y1, x2, y2
        
        # Rechteck, roter Rand, gelb gefüllt
        p.setPen(QPen(Qt.red, 3))
        p.setBrush(QBrush(Qt.yellow))
        p.drawRect(350, 50, 100, 30) # x, y, w, h
        
        # Polygon
        pts = [ QPoint(200, 50), QPoint(300, 200), QPoint(400, 150)]
        p.drawPolygon(QPolygon(pts))        
        
        # Kreis ohne Rand
        p.setBrush(QBrush(Qt.green))
        p.setPen(Qt.NoPen)
        p.drawEllipse(QRect(150, 150, 100, 100))
        
        # Ellipse ohne Füllung
        p.setBrush(Qt.NoBrush)
        p.setPen(QPen(Qt.magenta, 10))
        p.drawEllipse(QRect(280, 200, 200, 100))
        
        # einzeilger Text
        p.setFont(QFont('Helvetica', 15, QFont.Bold, italic=True))
        p.setPen(Qt.black)
        p.drawText(QPoint(30, 250), 'Text äöü')
        
        # Text mit Umbruch
        p.setFont(QFont('Helvetica', 12))
        txt = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.'
        p.drawText(QRect(30, 280, 200, 100), Qt.AlignLeft + Qt.TextWordWrap, txt)
        
        p.end()
        

# Fenster öffnen; das Programm läuft, bis das
# Fenster geschlossen wird
app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
