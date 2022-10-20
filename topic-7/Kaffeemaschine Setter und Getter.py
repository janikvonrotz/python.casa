class Kaffeemaschine:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

maschine = Kaffeemaschine("Jura")
print(maschine.name)
maschine.name = "Gaccia"
print(maschine.name)