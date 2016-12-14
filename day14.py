from collections import defaultdict 
import inputs, hashlib, re

def day14(salt): 
	cur_index = 0
	keys = []
	pos_keys = defaultdict(list)
	while len(keys) < 65:
		to_hash = salt+str(cur_index)
		m = hashlib.md5()
		m.update(to_hash.encode('utf-8'))
		hashed = m.hexdigest()
		three = re.findall(r'((\w)\2{2})', hashed)
		five = re.findall(r'((\w)\2{4})', hashed)
		for _, letter in five:
			key = sorted([pkey for pkey in pos_keys[letter] if pkey+1000 > cur_index])
			# print(letter, cur_index, pos_keys[letter])
			keys.extend(key)

		if three:
			pos_keys[three[0][1]].append(cur_index)
		cur_index +=1

	print(len(keys), sorted(keys)[63], sorted(keys))

day14('abc')

day14(inputs.day14)

