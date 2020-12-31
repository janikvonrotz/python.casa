#!/usr/bin/env python3
import RPi.GPIO as gpio
import sys, time
from datetime import datetime, timedelta

# LED ein-/ausschalten
def turnLedOnOff(pin):
    global ledStatus, lastTime
    now = datetime.now()
    # 500 ms Entprellzeit
    if now - lastTime > timedelta(milliseconds=500):
        ledStatus = 1 - ledStatus
        gpio.output(26, ledStatus)
        lastTime = now

# Setup
gpio.setmode(gpio.BOARD)    # Pin-Nummern verwenden
gpio.setup(26, gpio.OUT)    # Pin 26 zur Datenausgabe
gpio.setup(21, gpio.IN)     # Pin 21 zur Dateneingabe
ledStatus = 0
gpio.output(26, ledStatus)  # LED anfänglich aus
lastTime = datetime.now()
gpio.add_event_detect(21, gpio.FALLING, bouncetime=50)
gpio.add_event_callback(21, turnLedOnOff)

# auf Tastendrücke warten
print('Programm endet nach 10 Sekunden')
time.sleep(10)
gpio.cleanup()
