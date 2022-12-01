class Tier:
    def __init__(self, name, farbe, laut):
        self.name = name
        self._farbe = farbe
        self.laut = laut

    def ausgabe(self):
        print(f"Das {self._farbe}e Tier namens {self.name} macht: {self.laut}")

class Hund(Tier):
    def __init__(self, name, farbe, laut, alter):
        super().__init__(name, farbe, laut)
        self.alter = alter

hund = Hund('Dogster', 'blau', 'Yikes!', 37)
hund.ausgabe()