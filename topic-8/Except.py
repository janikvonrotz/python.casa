try:
    print(z)
except NameError as error:
    print(error)
    
try:
    print(z)
except:
    print("Ein Fehler im Code.")
