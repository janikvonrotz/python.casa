from datetime import datetime
from functools import reduce
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, QPen, QPolygon
from PyQt5.QtCore import Qt, QSize, QPoint, QRect

class Fenster(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self) # Konstruktor von QMainWindow aufrufen

        self.setMinimumSize(QSize(600, 400)) # Fenstergröße und Titel einstellen
        self.setWindowTitle('Temperaturkurve') 
        

    def paintEvent(self, event):
        p = QPainter()
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        
        w = self.size().width() # Fenstergröße und Temperaturbereich
        h = self.size().height()
        
        data = readData('Temperatur.txt')
        
        mintemp = min(itm[1] for itm in data)
        maxtemp = max(itm[1] for itm in data)
        tempdelta = maxtemp - mintemp

        # Gitternetz geviertelt
        # Platz für die Beschriftung
        x0 = 50 # links oben
        y0 = 10
        x1 = w - 10 # rechts unten
        y1 = h - 20
        gridw = x1 - x0
        gridh = y1 - y0
        labels = ['0:00', '6:00', '12:00', '18:00', '24:00']
        
        # Gitterlinien zeichnen
        for i in range(5): # von 0 bis 4
            
            y = y0 + gridh / 4 * i # horizontale Linien
            p.setPen(QPen(Qt.gray, 1))
            p.drawLine(x0, y, x1, y)
            
            x = x0 + gridw / 4 * i # vertikale Linien
            p.drawLine(x, y0, x, y1)
            p.setPen(QPen(Qt.black, 1)) # Beschriftung der X-Achse (unten)
            
            if i==0: # erster Eintrag linksbündig zur Achse
                p.drawText(QRect(x, y1+2, 40, 14), Qt.AlignLeft | Qt.AlignTop, labels[i])
            elif i==4: # letzter Eintrag rechtsbündig zur Achse
                p.drawText(QRect(x-40, y1+2, 40, 14), Qt.AlignRight | Qt.AlignTop, labels[i])
            else: # sonst: mittig
                p.drawText(QRect(x-20, y1+2, 40, 14), Qt.AlignCenter | Qt.AlignTop, labels[i])
            
            temp = maxtemp - (maxtemp - mintemp) / 4 * i # Beschriftung der Y-Achse (links)
            txt = '%.1f°' % (temp)
            p.drawText(QRect(0, y-10, 47, 20), Qt.AlignRight | Qt.AlignVCenter, txt.replace('.', ','))
            
        # Temperaturkurve innerhalb der Rechtecks
        # (x0, y0) -- (x1, y1) zeichnen
        p.setPen(QPen(Qt.red, 1))
        (xprev, yprev) = (None, None)
        
        for itm in data:
            x = x0 + itm[0] / 60 / 24 * gridw
            
            if tempdelta == 0:
                y = y1 - gridh / 2
            else:
                y = y1 - (itm[1] - mintemp) / tempdelta * gridh
            if xprev != None:
                p.drawLine(xprev, yprev, x, y)
                
            (xprev, yprev) = (x, y)
            
        p.end()

# List Temperaturdatei zeilenweise ein, liefert Liste in der
# Form [[n1, t1], [n2, t2], [n3, t3]], wobei n1 die Anzahl
# der Minuten seit Mitternacht ist, t die Temperatur zu diesem Zeitpunkt
def readData(fname):
    result = []
    try:
        with open(fname, 'rt') as f:
            for line in f:
                parts = line.strip().split('\t')
                
                if len(parts) != 2: continue
                
                dt = datetime.strptime(parts[0],'%Y-%m-%d %H:%M')
                minutes = dt.minute + dt.hour * 60
                temp = float(parts[1])
                result += [[minutes, temp]]

    except BaseException as err:
        print('Es ist ein Fehler aufgetreten:', err)
        
    return result

app = QtWidgets.QApplication([])
win = Fenster()
win.show()
app.exec_()
