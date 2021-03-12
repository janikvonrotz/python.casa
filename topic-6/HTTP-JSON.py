
url = 'https://raw.githubusercontent.com/janikvonrotz/python.casa/main/topic-6/B%C3%BCcher.json'

import json
import urllib.request

response = urllib.request.urlopen(url)
data = json.loads(response.read().decode('utf-8'))
print(data)
