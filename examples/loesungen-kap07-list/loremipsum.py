#!/usr/bin/env python3
from functools import reduce
s = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.'

# Satzeichen eliminieren
plain = ''.join(filter(lambda c: str.isalpha(c) or c==' ', list(s)))
print(plain)
# Lorem ipsum dolor sit amet consetetur sadipscing elitr sed ...

# Wörter bilden
words = plain.split(' ')
print(words)
# ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consetetur', ...

# Variante 1 (langsam): nach Länge sortieren
sortedwords = sorted(words, key=len, reverse=True)
print(sortedwords)
print('Maximale Wortlänge:', len(sortedwords[0]))

# Variante 2 (viel schneller): reduce und map
maxlen = reduce(max, map(len, sortedwords))
print('Maximale Wortlänge:', maxlen)
