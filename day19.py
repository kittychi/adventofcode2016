import inputs

def day19(number): 
	bin = '{0:b}'.format(number)
	bin = bin[1:] + bin[0:1]
	pos = int(bin, 2)
	print(pos)

day19(3014603)
