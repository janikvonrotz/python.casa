try:
    f = open('test.txt', 'rt')
    for line in f:
        print(line, end='')
    f.close() 
  
except BaseException as err:
    print('Fehler:', err)