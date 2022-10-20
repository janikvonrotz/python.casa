for c in 'abc':
    print(c)
    
for i in (17, 87, 4): 
    print(i, end=' ') # end Paramter verhindert Zeilenumbruch

dict = {'a':12, 'c':78, 'b':3, 'd':43}
for k in dict:
    print(k,dict[k])
for k,v in dict.items():
    print(k,v)
