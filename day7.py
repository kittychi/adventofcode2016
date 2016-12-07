import inputs, re

def day7(address_list):
	addresses = address_list.split()

	count = 0
	for address in addresses: 
		invalid = re.search('\[[a-z]*(([a-z])([a-z])\\3\\2)[a-z]*\]', address)
		if invalid: 
			print(invalid.group(1), address)
			if invalid.group(1)[0] != invalid.group(1)[1]:
				continue
		outsides = re.split('\\[[a-z]*\\]', address)
		for outside in outsides: 
			valid = re.search('(([a-z])([a-z])\\3\\2)', outside)
			if valid and valid.group(1)[0] != valid.group(1)[1]: 
				count += 1
				print(count, valid.group(1), address)
				break

test= ''' abba[mnop]qrst
	abcd[bddb]xyyx
	aaaa[qwer]tyui
	ioxxoj[asdfgh]zxcvbn '''

day7(inputs.day7input)