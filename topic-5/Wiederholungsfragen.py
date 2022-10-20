s = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."

# Spezialzeichen entfernen
def text(s):
    return s.isalpha() or s == ' '
raw = ''.join(filter(text, list(s)))

# Liste aus Zeichen erstellen
words = raw.split(' ')

# Wortlänge für jedes Wort bestimmten und mit Reduce auf den höchsten Werte reduzieren
from functools import reduce
print(reduce(max, map(len, words)))