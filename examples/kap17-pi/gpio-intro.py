#!/usr/bin/env python3
import RPi.GPIO as gpio
import time

# Setup
gpio.setmode(gpio.BOARD)    # Pin-Nummern verwenden
gpio.setup(26, gpio.OUT)    # Pin 26 zur Datenausgabe
gpio.setup(21, gpio.IN)     # Pin 21 zur Dateneingabe

# LED ein- und ausschalten
gpio.output(26, gpio.HIGH)  # GPIO auf High stellen
print('LED an Pin 26 leuchtet')
time.sleep(2)
gpio.output(26, gpio.LOW)   # GPIO auf Low stellen
print('LED an Pin 26 leuchtet nicht mehr')

# LED langsam heller und dunkler machen
pwm = gpio.PWM(26, 1000)    # Frequenz: 1000 Hertz
pwm.start(0)                # Duty 0 (dunkel)
print('LED wird immer heller')
for duty in range(0, 101):  
    pwm.ChangeDutyCycle(duty)    
    time.sleep(0.02)        # 20 ms warten
print('LED wird immer dunkler')
for duty in range(100, -1, -1):  
    pwm.ChangeDutyCycle(duty)    
    time.sleep(0.02)        # 20 ms warten
pwm.stop()

# Zustand eines Tasters auswerten
status = gpio.input(21)
print('Status an Pin 21:', status)

# GPIOs wieder freigeben
gpio.cleanup()

