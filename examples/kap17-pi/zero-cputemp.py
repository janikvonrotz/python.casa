#!/usr/bin/env python3
from gpiozero import LED
import time

# je nach Temperatur die entsprechende LED einschalten
def turnOnOffLEDs(temp):
    if temp < 50: 
      ledG.on();  ledY.off(); ledR.off()
    elif temp > 60: 
      ledG.off(); ledY.off(); ledR.on()
    else:
      ledG.off(); ledY.on();  ledR.off()
      
# Setup
ledR = LED(25)     # BCM-Nummern, entspricht Pin 22
ledY = LED(8)      # ... Pin 24
ledG = LED(7)      # ... Pin 26
for led in [ledR, ledY, ledG]:
  led.off()

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
