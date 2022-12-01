class Tier:
    def __init__(self, name, farbe, laut):
        self.name = name
        self._farbe = farbe
        self.laut = laut

    @property
    def farbe(self):
        return self._farbe
    
    @farbe.setter
    def farbe(self, farbe):
        self._farbe = farbe

    def ausgabe(self):
        print(f"Das {self.farbe}e Tier namens {self.name} macht: {self.laut}")

katze = Tier('Pixel', 'grau', 'Joink!')
katze.ausgabe()

katze.farbe = 'weiss'
katze.ausgabe()