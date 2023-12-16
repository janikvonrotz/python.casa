class Kaffeemaschine:
    def __init__(self, pin):
        self.pin = pin

kaffeemaschine = Kaffeemaschine(5432)

kaffeemaschine.pin = 1234

print(kaffeemaschine.pin) # Ausgabe: 1234