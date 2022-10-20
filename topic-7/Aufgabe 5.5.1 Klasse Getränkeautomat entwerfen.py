class Getränkeautomat:
    def __init__(self, produkte, bestand, name):
        self.produkte = produkte
        self.bestand = bestand
        self.name = name
        
    def Auflisten(self):
        for key,value in self.produkte.items():
            print(f"Auswahl {key}: {value}")
    
    def Ausgabe(self, nummer):
        bestand = self.bestand[nummer]
        if(bestand > 0):
            print(f"Das Produkt {self.produkte[nummer]} wurde ausgeben.")
            self.bestand[nummer] = (bestand - 1)
            print(f"Es sind noch {self.bestand[nummer]} Stk. verfügbar.")
        else:
            print("Das gewählte Produkt ist nicht verfügbar.")