#!/usr/bin/env python3
print('Verschachtelte Schleife')
for i in range(1, 3):
    for j in range(0, i):
        print(i+j)

print()
print('break')
i=0
j=9
while i<j:
    print(i, j)
    if i>=3:
        break
    i+=1
    j-=1
