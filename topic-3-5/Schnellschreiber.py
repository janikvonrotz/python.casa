from datetime import datetime
start = int(datetime.now().timestamp())

s = "Am 19. Januar 2038 haben 32-Bit Computer ein Problem."
eingabe = input(f'Geben Sie den folgenden Text ein: "{s}" ')
print(s == eingabe)

end = int(datetime.now().timestamp())
print(end - start, 'Sekunden')