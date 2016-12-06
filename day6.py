import inputs, collections

def day6(input_lines):
	lines = input_lines.split()
	chars = [''.join([a[i] for a in lines]) for i in range(len(lines[0]))]

	part1 = ''
	part2 = ''
	for char in chars:
		freq_ = collections.Counter(char).most_common()
		part1 += freq_[0][0]
		part2 += freq_[-1][0]
	
	print(part1, part2)


test = ''' eedadn
	drvtee
	eandsr
	raavrd
	atevrs
	tsrnev
	sdttsa
	rasrtv
	nssdts
	ntnada
	svetve
	tesnvt
	vntsnd
	vrdear
	dvrsen
	enarar '''

day6(test)
day6(inputs.day6input)