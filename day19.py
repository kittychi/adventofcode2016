import inputs

def day19(number): 
	bin = '{0:b}'.format(number)
	bin = bin[1:] + bin[0:1]
	pos = int(bin, 2)
	print(pos)

def day19b(number):
	elves = [1 + i for i in range(number)]
	while len(elves) > 4:
		half = len(elves) // 2
		if len(elves) % 2 == 0: 
			halved = elves[half-1::3]
			num_removed = len(elves[half-1:]) - len(halved)
			elves = elves[num_removed:half-1] + halved + elves[:num_removed]
		else:
			halved = elves[half+1::3]
			num_removed = len(elves[half:]) - len(halved)
			elves = elves[num_removed:half] + halved + elves[:num_removed]
	print(elves[0])

day19b(inputs.day19)
