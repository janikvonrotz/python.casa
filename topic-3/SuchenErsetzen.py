text = 'The quick brown fox jumps over the lazy dog'

print(text.find('fox'))

print(text.replace('fox', 'cat'))

print(text[:text.find('brown')])

print(text[text.find('brown') + 6:])

print(text[:text.find('brown')] + text[text.find('brown') + 6:])