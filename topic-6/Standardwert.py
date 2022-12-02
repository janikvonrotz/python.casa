def wechsel(input_chf, rate=0.8):
	return input_chf * rate

input_chf = 500

output_eur = wechsel(input_chf)

print(output_eur)