import inputs, collections

def day6(input_lines):
	lines = input_lines.split()
	chars = [''.join([a[i] for a in lines]) for i in range(len(lines[0]))]

	for char in chars:
		freq_ = collections.Counter(char).most_common(1)
		print(freq_)


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
day6(inputs.day6input)