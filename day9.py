import inputs, re

def day9(compressed):
	decompressed = ''
	skip = 0
	for i in range(len(compressed)):
		if skip > 0: 
			skip -= 1
			continue
		if compressed[i] != '(': 
			decompressed += compressed[i]
			continue
		
		end_bracket =  i + compressed[i:].find(')')
		marker = compressed[i+1:end_bracket]
		count, repeat = marker.split('x')

		decompressed += compressed[end_bracket+1:end_bracket+1+int(count)] * int(repeat) 

		skip = end_bracket + int(count) - i

	print(len(decompressed), decompressed)
	
def day9b(compressed):
	markers = re.findall(r'\((\dx\d)\)', compressed)
	decompressed_count = 0
	cur_index = 0
	while len(markers) > 0: 
		marker = markers.popleft()
		open_ = compressed[cur_index:].find(marker)


def get_decompress_count(compressed, multiplier):
	markers = re.findall(r'\((\d*x\d*)\)', compressed)
	# print(markers, compressed)
	if len(markers) == 0:
		# print('-', compressed, multiplier, 'returning', len(compressed) * multiplier)
		return len(compressed) * multiplier
	markers.reverse()
	marker = markers.pop()
	count, mul = list(map(lambda x: int(x),marker.split('x')))
	# print('', mul, multiplier)
	start_bracket = compressed.find(marker) - 1
	end_bracket = start_bracket + len(marker) + 1
	left = get_decompress_count(compressed[end_bracket+1:end_bracket+count+1], mul)
	right = get_decompress_count(compressed[end_bracket+count+1:], multiplier)
	# print(compressed, 'left', left, 'right', right)
	return start_bracket * multiplier + right + (left*multiplier) 

test= 'X(8x2)(3x3)ABCY'
test2 ='(27x12)(20x12)(13x14)(7x10)(1x12)A'
test3 = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'
# # day9b(test)
# day9b(inputs.day9input)

print(get_decompress_count(inputs.day9input, 1))

