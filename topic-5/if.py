antwort = input("Möchtest du Feierabend?: ")

if antwort in ["Ja", "ja", "jep"]:
    print("Sehr gut!")
elif antwort in ["Nein", "nein", "niet"]:
	print("Du bist ein Workaholic!")
else:
    print("Ich glaube dir nicht!")