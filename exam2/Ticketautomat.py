class Ticketautomat:
    def __init__(self, ticket_preis):
        self.ticket_preis = ticket_preis
        self.guthaben = 0
    
    def geld_einwerfen(self, betrag):
        self.guthaben += betrag
    
    def ticket_drucken(self):
        if self.guthaben >= self.ticket_preis:
            print("Drucke Ticket...")
            self.guthaben -= self.ticket_preis
        else:
            print("Nicht genug Guthaben. Bitte mehr einwerfen.")
    
    def guthaben_ausgeben(self):
        if self.guthaben > 0:
            print(f"Gebe {self.guthaben} Euro aus...")
            self.guthaben = 0
        else:
            print("Kein Guthaben zum Ausgeben.")

ticketautomat = Ticketautomat(9)
ticketautomat.geld_einwerfen(10)
ticketautomat.ticket_drucken()
ticketautomat.guthaben_ausgeben()