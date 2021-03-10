import urllib.request
url = 'https://example.com'
response = urllib.request.urlopen(url)
binary = response.read() # Download durchführen
html = binary.decode('utf-8')

f = open('index.html', 'wt')
f.write(html)
f.close