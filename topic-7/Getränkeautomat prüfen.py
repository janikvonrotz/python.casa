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
        bestand = self.bestand[nummer]
        if(bestand > 0):
            print(f"Das Produkt {self.produkte[nummer]} wurde ausgeben.")
            self.bestand[nummer] = (bestand - 1)
            print(f"Es sind noch {self.bestand[nummer]} Stk. verfügbar.")
        else:
            print("Das gewählte Produkt ist nicht verfügbar.")

produkte = { 1: "Redbull", 2: "Redbull", 3: "Redbull"}
bestand = { 1: 3, 2: 4, 3: 0}

automat = Getränkeautomat(produkte, bestand, "Gratis")

automat.Auflisten()
automat.name = "Redbull-o-mat"
automat.Auflisten()

