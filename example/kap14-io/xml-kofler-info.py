#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import urllib.request
url      = 'https://kofler.info/feed'
response = urllib.request.urlopen(url)
binary   = response.read()        # binäre Daten
sitemap  = binary.decode('utf-8') # als Text interpretieren


root = ET.fromstring(sitemap)

# alle <link>-Tags durchlaufen
#for lnk in root.iter('link'):
#    print(lnk.text)
    
# Alternative Vorgehensweise
channel = root[0]
for itm in channel.findall('item'): # Schleife über alle <item>s
    print(itm.find('link').text)
      
