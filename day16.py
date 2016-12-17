import inputs, re

def day16(init_state, final_length): 
	data = dragon_curve(init_state, final_length)
	print(data)
	return generate_checksum(data)


def dragon_curve(a, final_length): 
	if len(a) >= final_length:
		return a[:final_length]
	b = ''.join([str(abs(int(a[len(a) - i-1])-1)) for i in range(len(a))])
	return dragon_curve(a+'0'+b, final_length)

def generate_checksum(data): 
	if len(data) % 2 == 1: 
		print(data)
		return data
	
	pairs = re.findall(r'(\d\d)', data)
	checksum = ''.join(['0' if pair[0]!=pair[1] else '1' for pair in pairs])
	return generate_checksum(checksum)


print(day16('11110010111001001', 272))