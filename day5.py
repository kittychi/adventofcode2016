import inputs, hashlib

def day5(door_id): 
	counter = 0
	password_part1 = ''
	password_part2 = {}
	while len(password_part2) < 8: 
		id_ = door_id + str(counter)
		m = hashlib.md5()
		m.update(id_.encode('utf-8'))
		if m.hexdigest()[:5] == '00000':
			index = m.hexdigest()[5:6]
			password_part1 = password_part1 + index
			if index.isdigit() and int(index) < 8 and index not in password_part2.keys():
				password_part2[index] = m.hexdigest()[6:7]
			# 	print('2: ', password_part2)
			# print('1: ', password_part1)
		counter += 1
		print('.' * (counter % 5))
	print(password_part1)
	print(''.join([y for (x, y) in sorted(password_part2.items())]))

day5(inputs.day5input)