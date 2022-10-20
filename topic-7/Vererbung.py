class Tier():
    def __init__(self, name, farbe, alter):
        self.rufname = name
        self.farbe   = farbe
        self.alter   = alter

class Katze(Tier): # Katze ist ein Tier
    def __init__(self, rufname, farbe, alter):
        super().__init__(rufname, farbe, alter) # Aufruf Konstruktor von Tier

katze = Katze("Sammy", "orange", 3)
print(katze.farbe)