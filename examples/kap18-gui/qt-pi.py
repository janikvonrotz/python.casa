#!/usr/bin/env python3
import RPi.GPIO as gpio
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QGridLayout, QLabel, QSlider
from PyQt5.QtCore import Qt, QSize, QTimer

# Klasse für das Hauptfenster
class MyWindow(QMainWindow):
    def __init__(self):
        
        # Konstruktor von QMainWindow aufrufen
        super().__init__()
        self.setMinimumSize(QSize(250, 120))    
        self.setWindowTitle('Qt auf dem Raspberry Pi') 

        # Grid-Layout für Widget in Main-Window (Layout von
        # Main-Window kann nicht verändert werden)
        wid = QWidget(self)
        self.setCentralWidget(wid)
        grid = QGridLayout()
        wid.setLayout(grid)
        
        # erste Reihe: Beschriftung
        row = 0
        for s in ['LED-Helligkeit:', 'CPU-Temperatur:', 
                  'Taster:']:
            lbl = QLabel(s)
            lbl.resize(lbl.sizeHint())
            grid.addWidget(lbl, row, 1, QtCore.Qt.AlignRight)
            row += 1 

        # zweite Reihe oben: Slider
        sld = QSlider(Qt.Horizontal)
        sld.setMinimum(0)
        sld.setMaximum(100)
        sld.valueChanged.connect(self.sliderChanged)
        grid.addWidget(sld, 0, 2)
        
        # zweite Reihe mitte: Label
        self.tempLbl = QLabel('---')
        grid.addWidget(self.tempLbl, 1, 2)

        # zweite Reihe unten: Label
        self.switchLbl = QLabel('---')
        grid.addWidget(self.switchLbl, 2, 2)

        # zweite Reihe ganz unten: Button
        btn = QPushButton('Ende')
        btn.clicked.connect(self.quit)
        grid.addWidget(btn, 3, 2, QtCore.Qt.AlignRight)
        
        # Timer
        timer = QTimer(self)
        timer.timeout.connect(self.timeout)
        timer.start(150)  # alle 150 ms aufrufen

    # Abbrechen-Button: Programmende
    def quit(self):
        app.quit()
        
    # Slider-Bewegung
    def sliderChanged(self, value):
        pwm.ChangeDutyCycle(value)
        
    # Timeout (wird regelmäßig aufgerufen)
    def timeout(self):
        # Temperatur ermitteln und anzeigen
        with open(fname, 'rt') as f:
            temp = int(f.readline()) / 1000
        print(temp)
        self.tempLbl.setText('%.1f°C' % (temp))
        
        # Status von Taster ermitteln
        status = gpio.input(21)
        if status == 0:
            self.switchLbl.setText('gedrückt')
        else:
            self.switchLbl.setText('nicht gedrückt')
            
# GPIO-Setup
gpio.setmode(gpio.BOARD)   # Pin-Nummern des J8-Headers
gpio.setup(21, gpio.IN)    # Pin 21 zur Dateneingabe
gpio.setup(26, gpio.OUT)   # Pin 26 zur Datenausgabe
pwm = gpio.PWM(26, 1000)   # Frequenz: 1000 Hertz
pwm.start(0)               # Duty 0 (dunkel)
fname = '/sys/class/thermal/thermal_zone0/temp'
        
# Fenster öffnen, auf Programmende warten
app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
gpio.cleanup()
