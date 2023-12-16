class Kaffeemaschine:
    def __init__(self, pin):
        self._pin = pin

kaffeemaschine = Kaffeemaschine(5432)

kaffeemaschine._pin = 1234 

print(kaffeemaschine._pin)