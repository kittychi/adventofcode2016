import inputs

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
	
test= 'X(8x2)(3x3)ABCY'

day9(inputs.day9input)
