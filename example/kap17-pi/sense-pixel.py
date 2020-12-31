#!/usr/bin/env python3
from sense_hat import SenseHat
import time

sense = SenseHat()
sense.rotation = 180

blue = (0, 0, 255)
sense.clear(blue)
time.sleep(1)
sense.clear()       # Display ausschalten

# LED links oben rot leuchten lassen
red = (255, 0, 0)
sense.set_pixel(0, 0, red)
time.sleep(1)

# alle Pixel verändern (Farbmuster)
lst = []
for row in range(8):
    for col in range(8):
        lst += [(row*32, col*32, 0)]
sense.set_pixels(lst)

time.sleep(1)
sense.clear()       # Display ausschalten
