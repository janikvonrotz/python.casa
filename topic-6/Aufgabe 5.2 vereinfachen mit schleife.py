def ansage(ort):
    print(f"Der nächste Zug fährt nach {ort}.")

orte = ['Bern','Luzern','Zürich','Genf','Chur']

[ansage(ort) for ort in orte]

# Oder it mehreren Parameter

def ansage(*orte):
    [print(f"Der nächste Zug fährt nach {ort}.") for ort in orte]

orte = ['Bern','Luzern','Zürich','Genf','Chur']

ansage(*orte[0:2],*orte[2:5])
