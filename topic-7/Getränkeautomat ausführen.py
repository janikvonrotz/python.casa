produkte = { 1: "Apfelsaft", 2: "Wasser", 3: "Redbull"}
bestand = { 1: 3, 2: 4, 3: 0}

automat = Getränkeautomat(produkte, bestand, "Gratis")

automat.Auflisten()
automat.Ausgeben(2)
automat.Ausgeben(2)
automat.Ausgeben(3)