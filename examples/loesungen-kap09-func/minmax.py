#!/usr/bin/env python3

def minmax(lst):
    min = lst[0]
    max = lst[0]
    for itm in lst:
        if itm<min:
            min = itm
        if itm>max:
            max = itm
    return (min, max)
        
nmbs = [-13, 27, 59, -70, 44]
a, b = minmax(nmbs)
print('Minimum: %d   Maximum: %d' % (a, b))
