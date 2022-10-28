a = True
b = False

print(not (not (a)) and (b and (b or a)))

print(a and (b and (b or a))) # Doppelte Negation

print(a and b) # Absorption

a = False
b = True
print(a and b) # b wird nicht evaluiert.