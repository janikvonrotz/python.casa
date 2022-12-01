def wechsel(input_chf, rate):
	return input_chf * rate

rate = 0.95
input_chf = 500

output_eur = wechsel(input_chf, rate)

print(output_eur)