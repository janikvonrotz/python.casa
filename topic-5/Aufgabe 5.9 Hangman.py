
# Einstellungen
wort = list("esel".upper())
laenge = len(wort)
zensiert = list(laenge * '_')
versuche = 5
gefunden = []
gewonnen = False

print(wort, laenge, zensiert, versuche, gewonnen)

while versuche > 0  and not gewonnen:
    eingabe = input("Geben Sie einen Buchstaben ein: ").upper()

    if eingabe in wort:
        gefunden.extend([eingabe])
        
        for i in range(0, laenge):
            if wort[i] in gefunden:
                zensiert[i] = wort[i]
        
        print(f"Treffer! Der aktuelle Stand: {' '.join(zensiert)}.")
        print(f"Deine Treffer: {' '.join(gefunden)}.")
        
        if '_' not in zensiert:
            gewonnen = True
            print("Du hast gewonnen!")
        
    else:
        versuche -= 1
        print(f"Schade! Du hast noch {versuche} Versuche.")

if not gewonnen:
    print("Du hast verloren!")
