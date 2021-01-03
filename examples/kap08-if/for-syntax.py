#!/usr/bin/env python3
print('\nSchleife mit range()')
for i in range(0, 20, 3): 
    print(i, end=' ')

print('\n\nSchleife mit range(), float')
for i in range(0, 11): 
    x = i / 10.0
    print(x, end=' ')

print('\n\nSchleife über Listenelemente')
for s in ['Python', 'macht', 'Spaß!']: 
    print(s)
    
print('\n\nList Comprehension mit Bedingung')    
lst = [1, 2, 3, 10]
result2 = [ x*x for x in lst if x%2==0 ]  
print(result2)

print('\n\nDictionary in Comprehension Syntax erzeugen')    
dict = { x: x*x for x in lst }
print(dict)

print('\n\nDictionary in Comprehension Syntax verarbeiten')    
dict = {'a':12, 'c':78, 'b':3, 'd':43}
resultset = { x for x in dict }
print(resultset)
resultlst = [ x for x in dict ]
print(resultlst)


print('\n\nSchleife mit else-Block')
for i in [7, 12, 3]:
    print(i)
else:
    print('else-Block')


