import time, math
start = time.process_time()

# Sinnlos Zeit totschlagen  
for i in range(1, 1000000):    
  x=math.sin(i)

end = time.process_time()    
print(end - start, 'Sekunden')