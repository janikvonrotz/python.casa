#!/usr/bin/env python3
from math import sin, cos, pi
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush, QPolygon, QFont
from PyQt5.QtCore import Qt, QSize, QPoint, QRect

class MyWindow(QMainWindow):
    def __init__(self, type):
        # Konstruktor von QMainWindow aufrufen
        QMainWindow.__init__(self)
        
        # Fenstergröße und Titel einstellen
        self.type = type
        self.setGeometry(50 + (i % 2) * 350, 50 + (i // 2) * 350, 300, 300)    
        self.setWindowTitle('Fenster %d' % (type+1)) 
        self.setStyleSheet('background-color: white;')

    def paintEvent(self, event):
        p = QPainter()
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        # Größe und Mittelpunkt des maximalen Quadrats im Fenster
        (w, h) = (self.size().width(), self.size().height())
        x0 = self.size().width() / 2
        y0 = self.size().height() / 2
        r = min(w, h) / 2 - 3
        if r<0: return
        if self.type==0: self.paintCircle(p, x0, y0, r)
        if self.type==1: self.paintSpiral(p, x0, y0, r)
        if self.type==2: self.paintLines(p, x0, y0, r)
        if self.type==3: self.paintPolygones(p, x0, y0, r)
        p.end()

    # Kreis zeichnen
    def paintCircle(self, p: QPainter, x0, y0, r):
        p.setPen(QPen(Qt.blue, 2))
        n = 100 # Kreis aus 100 kleinen Linien
        xprev = x0 + r
        yprev = y0
        for i in range(n+1):
            x = x0 + cos(2 * pi / n * i) * r
            y = y0 + sin(2 * pi / n * i) * r
            if i>0:
                p.drawLine(xprev, yprev, x, y)
            (xprev, yprev) = (x, y)

    # Spirale zeichnen
    def paintSpiral(self, p: QPainter, x0, y0, r):
        p.setPen(QPen(Qt.red, 2))
        n = 400
        xprev = x0 + r
        yprev = y0
        for i in range(n+1):
            x = x0 + cos(2 * pi / 100 * i) * r / (n+200) * (i+200)
            y = y0 + sin(2 * pi / 100 * i) * r / (n+200) * (i+200)
            if i>0:
                p.drawLine(xprev, yprev, x, y)
            (xprev, yprev) = (x, y)

    # graue Linien entlang einer Spirale zeichnen
    def paintLines(self, p: QPainter, x0, y0, r):
        n = 400
        xprev = x0 + r
        yprev = y0
        for i in range(n):
            grey = 190 / n * (n-i)
            p.setPen(QPen(QColor(grey, grey, grey), 1))
            radius = r / (n+200) * (i+200)
            ang1 = 2 * pi / 100 * i
            ang2 = ang1 + pi * 0.4
            x1 = x0 + cos(ang1) * radius
            y1 = y0 + sin(ang1) * radius
            x2 = x0 + cos(ang2) * radius
            y2 = y0 + sin(ang2) * radius
            p.drawLine(x1, y1, x2, y2)

    # bunte, verdrehte Polygone entlang eines
    # spiralförmigen Pfads zeichnen
    def paintPolygones(self, p: QPainter, x0, y0, r):
        n = 200
        for i in range(n):
            radius = r / (n+250) * (i+200)
            ang = 2 * pi / 100 * i
            x = x0 + cos(ang) * radius
            y = y0 + sin(ang) * radius
            color = QColor.fromHsv(i % 360, 255, 255)
            self.paintOnePolygon(p, x, y, -i / 50, color)

    # beliebig gedrehtes Dreieck rund um (x0, y0) zeichnen
    # color gibt die Füllfarbe an
    def paintOnePolygon(self, p: QPainter, x0, y0, baseangle, color):
        radius = 30
        degrees = [30, 150, 210, 330] # Grad -> Bogengrad 
        angles = list(map(lambda x: x / 180 * pi, degrees))
        pts =  []  # Koordinaten des Polygons
        for i in range(len(angles)):
            x = x0 + cos(baseangle + angles[i]) * radius
            y = y0 + sin(baseangle + angles[i]) * radius
            pts += [ QPoint(x, y) ]
        p.setPen(QPen(Qt.black, 2))
        p.setBrush(QBrush(color))
        p.drawPolygon(QPolygon(pts))
            
# 4 Fenster öffnen; das Programm läuft, bis alle
# Fenster geschlossen werden
app = QtWidgets.QApplication([])
winlist = []
for i in range(4):
    win = MyWindow(i)
    win.show()
    winlist += [win]
app.exec_()
