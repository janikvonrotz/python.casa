l1 = [1,2,3,9,345,36,33]

l2 = list(filter(lambda x: x%3==0, l1))
print(l2) # Ausgabe [3, 9, 345, 36, 33]