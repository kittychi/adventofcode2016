import inputs, re

def day16(init_state, final_length): 
	data = dragon_curve(init_state, final_length)
	return generate_checksum(data)


def dragon_curve(a, final_length): 
	while len(a) < final_length:
		b = ''.join(['0' if i == '1' else '1' for i in a][::-1])
		a = a+'0'+b
	return a[:final_length]

def generate_checksum(data): 
	while len(data) % 2 != 1:
		pairs = re.findall(r'(\d\d)', data)
		data = ''.join(['0' if data[2*i]!=data[2*i+1] else '1' for i in range(len(data)//2)])
	print(data)
	return data


day16(inputs.day16, 35651584)

# day16('111100001010', 40)
