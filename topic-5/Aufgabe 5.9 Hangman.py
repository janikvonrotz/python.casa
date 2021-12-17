
# Einstellungen
wort = list("python".upper())
laenge = len(wort)
zensiert = list(laenge * '_')
versuche = 5
gefunden = []
gewonnen = False

while versuche > 0  and not gewonnen:
    eingabe = input("Geben sie einen Buchstaben ein: ").upper()

    if eingabe in wort:
        gefunden.extend([eingabe])
        
        for i in range(0, laenge):
            if wort[i] in gefunden:
                zensiert[i] = wort[i]
        
        print(f"Treffer! Der aktuelle Stand: {zensiert}.")
        print(f"Treffer! Deine Treffer: {gefunden}.")
        
        if '_' not in zensiert:
            gewonnen = True
            print("Du hast gewonnen!")
        
    else:
        versuche -= 1
        print(f"Schade! Du hast noch {versuche} Versuche.")

if not gewonnen:
    print("Du hast verloren!")
