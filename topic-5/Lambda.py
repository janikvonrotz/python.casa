x = lambda a : a + 10  
print(x(5))

data = [1,2,3,9,345,36,33]

filtered = list(filter(lambda x: x%3==0, data))
print(filtered) # Ausgabe [3, 9, 345, 36, 33]
