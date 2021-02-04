Das folgende Programm benutzt zwei geschachtelte if Verzweigungen. Schreibe das Programm um, so dass es mit einer einzelnen Verzweigung auskommt:

```py
zahl = int(input("Gib eine Zahl ein: "))
   
if zahl % 2 == 0:
    if zahl % 3 == 0:
        print("Die eingegebene Zahl ist durch drei und zwei teilbar.")
    else:
        print("Die eingegebene Zahl ist nicht durch drei und zwei teilbar.")
else:
    print("Die eingegebene Zahl ist nicht durch drei und zwei teilbar.")
```