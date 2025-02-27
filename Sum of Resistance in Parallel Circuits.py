def series_resistance(lst):
	# tab = []
	# tab = lst
	suma = sum(lst)
	# for element in tab:
	# 	suma += element
	
	return f"{suma} ohms" if suma > 1 else f"{suma} ohm"

print(series_resistance([0.5, 0.5]))