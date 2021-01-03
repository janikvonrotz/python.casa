#!/usr/bin/env python3

def findAll(s, pattern):
    matches = []
    pos = s.find(pattern)
    while pos != -1:
        matches += [pos]
        pos = s.find(pattern, pos+1)
    return matches
    
print(findAll('abcefgabcxyzabcd', 'abc'))
