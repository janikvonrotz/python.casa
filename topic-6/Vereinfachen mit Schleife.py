# Lösung 1

def ansage(ort):
    print(f"Der nächste Zug fährt nach {ort}.")

orte = ['Bern','Luzern','Zürich','Genf','Chur']

for ort in orte:
    ansage(ort)

# Lösung 2

def ansage(orte):
    for ort in orte:
        print(f"Der nächste Zug fährt nach {ort}.")

orte = ['Bern','Luzern','Zürich','Genf','Chur']

ansage(orte)
