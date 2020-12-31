#!/usr/bin/env python3
for i in range(1, 11):
    for j in range(1, 11):
        print('%dx%d=%d\t' % (j, i, i*j), end='')
    print()
        
