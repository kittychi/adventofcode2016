import inputs, re

def day7(address_list):
	addresses = address_list.split()

	tls_count = 0
	for address in addresses:
		invalid = re.search('\[[a-z]*(([a-z])([a-z])\\3\\2)[a-z]*\]', address)
		if invalid: 
			if invalid.group(1)[0] != invalid.group(1)[1]:
				continue
		outsides = re.split('\\[[a-z]*\\]', address)
		for outside in outsides: 
			valid = re.search('(([a-z])([a-z])\\3\\2)', outside)
			if valid and valid.group(1)[0] != valid.group(1)[1]: 
				tls_count += 1
				break
	print(tls_count)

def day7b(address_list):
	addresses = address_list.split()

	ssl_count = 0
	for address in addresses: 
		braces = re.finditer(r'\[([a-z]*)\]', address)
		matched = []
		for brace in braces:
			matched.extend(re.findall(r'(([a-z])(?=([a-z])\2))', brace.group(1)))
		for match, a, b in matched: 
			if a == b:
				continue
			outsides = re.split('\\[[a-z]*\\]', address)
			bab = b+a+b
			if any(bab in outside for outside in outsides): 
				ssl_count+=1
				break
	print(ssl_count)
				


test= ''' abba[mnop]qrst
	abcd[bddb]xyyx
	aaaa[qwer]tyui
	ioxxoj[asdfgh]zxcvbn '''

test2 = ''' nesmourutitzqtolwd[rurfefjvljejcufm]jagkqdwpkefkjdz[cctohikipqxyxbdjxsg]badmffkslhmgsxqscf '''

day7(inputs.day7input)
day7b(inputs.day7input)