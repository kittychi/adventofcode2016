import inputs, re

def day15(disks_start):
	disks_list = disks_start.split('\n')
	disks = []
	for disk in disks_list: 
		num, mod, _, start = re.findall(r'\d+', disk)
		disks.append((int(num), int(mod), int(start)))
	
	counter = 0
	while True: 
		count = [(start+num+counter) % mod for num, mod, start in disks]
		# print(count, sum(count))
		if sum(count) == 0:
			print(counter)
			break
		counter+=1
	print (disks)

test = ''' Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.'''

day15(inputs.day15)