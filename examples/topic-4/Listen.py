lst = [1, 2.3, 'abc', 'efg', 12]
print(lst[2]) # Ausgabe: abc

lst = list(range(10, 101, 10))
print(lst) # Ausgabe: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

lst = list('Hello, World!')
print(lst) # ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']
[print(s) for s in lst]