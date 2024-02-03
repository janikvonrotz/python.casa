produkte = { 1: "Apfelsaft", 2: "Wasser", 3: "Redbull", 4: "Snickers"}
bestand = { "Apfelsaft": 3, "Wasser": 4, "Redbull": 0, "Snickers": 5}

automat = Getränkeautomat(produkte, bestand, "Gratis")

automat.Auflisten()
automat.Ausgeben(2)
automat.Ausgeben(2)
automat.Ausgeben(3)
