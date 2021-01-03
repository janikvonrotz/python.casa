#!/usr/bin/env python3
import xml.etree.ElementTree as ET

tree = ET.parse('countries.xml')
root = tree.getroot()

print('Tag:', root.tag, 'Attribute:', root.attrib, 'Text:', root.text)
# Ausgabe: Tag: countries Attribute: {} Text: ''

print('root[2].text', root[2].text)
# Ausgabe Algeria

for c in root:  # Schleife über alle Einträge
  print('%44s: Code=%s, ISO=%s' % 
    (c.text, c.attrib['code'], c.attrib['iso']))
  # Ausgabe:       Afghanistan: Code=AF, ISO=4
  #                    Albania: Code=AL, ISO=8
  #                    Algeria: Code=DZ, ISO=12
                                                                    

# Dictionary Comprehension
dict = { c.attrib['code'] : c.text for c in root }
print(dict['DE'])
# Ausgabe Germany
