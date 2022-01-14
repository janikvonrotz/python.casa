class Getränkeautomat:
    def __init__(self, produkte, bestand, name):
        self.produkte = produkte
        self.bestand = bestand
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
