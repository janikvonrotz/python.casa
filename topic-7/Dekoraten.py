# Dekoraten-Funktion
def hello(func):                                                                                            
    def inner():                                                                                            
        print("Hello ")                                                                                     
        func()                                                                                              
    return inner                                                                                 

# Funktion wird mit Dekorator erweitert
@hello
def name():                                                                                                 
    print("Alice")                                                                                          
                                                                                                                                                                                
name()
