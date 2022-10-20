from datetime import datetime
sekunden = int(datetime.now().timestamp())
sekunden_binär = bin(sekunden)
anzahl_bits = len(str(sekunden_binär))-2 # Ist 31

print(f'Maximales Datum: {2**anzahl_bits}')