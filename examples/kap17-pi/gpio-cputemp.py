#!/usr/bin/env python3
import RPi.GPIO as gpio
import time

# je nach Temperatur die entsprechende LED einschalten
def turnOnOffLEDs(temp):
    if temp < 50: 
      (statR, statY, statG) = (0, 0, 1)
    elif temp > 60: 
      (statR, statY, statG) = (1, 0, 0)
    else:
      (statR, statY, statG) = (0, 1, 0)
    gpio.output(r, statR)     # rot
    gpio.output(y, statY)     # gelb
    gpio.output(g, statG)     # grün
      
# Setup
gpio.setmode(gpio.BOARD)      # Pin-Nummern verwenden
(r, y, g) = (22, 24, 26) 
for pin in [r, y, g]:
  gpio.setup(pin, gpio.OUT)   # als Ausgang verwenden
  gpio.output(pin, gpio.LOW)  # ausschalten

# LEDs einmal pro Sekunde aktualisieren
print('Programmende mit Strg+C')
fname = '/sys/class/thermal/thermal_zone0/temp'
try:
    while True:
        with open(fname, 'rt') as f:
            temp = int(f.readline()) / 1000
        print(temp)
        turnOnOffLEDs(temp)
        time.sleep(1)
except KeyboardInterrupt:
    print('Programmende')
finally:
    # GPIOs wieder freigeben
    gpio.cleanup()



