def ansage(ort):
    if isinstance(ort, str):
        print(f"Der nächste Zug fährt nach {ort}.")

ansage('Luzern')
ansage(6005)