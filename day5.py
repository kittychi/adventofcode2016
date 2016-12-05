import inputs, hashlib

def day5(door_id): 
	counter = 0
	password = ''
	while len(password) < 8: 
		id_ = door_id + str(counter)
		m = hashlib.md5()
		m.update(id_.encode('utf-8'))
		if m.hexdigest()[:5] == '00000':
			password = password + m.hexdigest()[5:6]
			print(password)
		counter += 1
	print(password)

day5(inputs.day5input)