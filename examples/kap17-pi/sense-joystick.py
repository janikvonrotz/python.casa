#!/usr/bin/env python3
from sense_hat import SenseHat
from time import sleep

# LED an aktueller Position einschalten, an der
# bisherigen ausschalten
def setLED(x, y):
    global oldX, oldY
    # LED an alter Position ausschalten ...
    sense.set_pixel(oldX, oldY, (0, 0, 0))
    # und an neuer Position einschalten (rot) und
    # diese Position merken
    sense.set_pixel(x, y, (255, 0, 0))
    (oldX, oldY) = (x, y)

# Setup
sense = SenseHat()
sense.clear()
(x, y)       = (4, 4)  # Startposition
(oldX, oldY) = (0, 0)  # vorige Position
setLED(x, y)

# Event-Loop
print('Programmende mit Strg+C')
try:
    while True:
        event = sense.stick.wait_for_event()
        if event.action == 'released':
            continue
        direct = event.direction
        if direct == 'left' and x>0:
            x -= 1
        if direct == 'right' and x<7:
            x += 1
        if direct == 'up' and y>0:
            y -= 1
        if direct == 'down' and y<7:
            y += 1
        # LED an neuer Position einschalten
        setLED(x, y)    
except KeyboardInterrupt:
    sense.clear()
    print('Programmende')
    
