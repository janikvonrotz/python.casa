# Verschlüsseln

msg = 'SnapeKillsDumbledore'

msg = ''.join([c + 'L' for c in msg])
msg = msg[::-1]
msg = 'LeLr' + msg + 'LeLr' 

print(msg)

msg = msg[4:44]
msg = msg[::-1]
msg = msg[::2]

print(msg)