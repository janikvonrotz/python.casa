with open('Limerick.txt') as f:
	for line in f:
		print(line.replace('Python', 'C#'), end='')

limerick = """
Python was a language for you and for me
It was simple and clean, but slow we agree.
But that was ok,
We loved it anyway.
Until it went from version 2 to version 3.
"""

with open('Limerick.txt', 'w') as f:
	f.write(limerick)
