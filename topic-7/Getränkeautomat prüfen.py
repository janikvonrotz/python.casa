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
        
    def Auflisten(self):
        print(f"Der Geränkeautomat {self._name} hat dieses Angebot:")
        for key,value in self.produkte.items():
            print(f"Auswal {key}: {value}")
    
    def Ausgabe(self, nummer):
        produkt = self.produkte[nummer]
        bestand = self.bestand[produkt]
        if(bestand > 0):
            print(f"Das Produkt {self.produkte[nummer]} wurde ausgeben.")
            self.bestand[produkt] = (bestand - 1)
            print(f"Es sind noch {self.bestand[produkt]} Stk. verfügbar.")
        else:
            print("Das gewählte Produkt ist nicht verfügbar.")

produkte = { 1: "Apfelsaft", 2: "Wasser", 3: "Redbull", 4: "Snickers"}

bestand = { "Apfelsaft": 3, "Wasser": 4, "Redbull": 0, "Snickers": 5}

automat = Getränkeautomat(produkte, bestand, "Gratis")

automat.Auflisten()
automat.name = "Redbull-o-mat"
automat.Auflisten()

