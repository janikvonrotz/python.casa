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
        o = sense.get_orientation()
        print(o)
        if 20 < o['pitch'] < 90 and x>0:
            x -= 1
        if 270 < o['pitch'] < 340 and x<7:
            x += 1
        if 270 < o['roll'] < 340 and y>0:
            y -= 1
        if 20 < o['roll'] < 90 and y<7:
            y += 1
        # LED an neuer Position einschalten
        setLED(x, y)    
        sleep(0.3)

except KeyboardInterrupt:
    sense.clear()
    print('Programmende')
    
