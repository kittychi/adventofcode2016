import inputs

def day20(ranges):
	ranges = sorted([tuple(map(lambda x: int(x), range_.split('-'))) for range_ in ranges.split()], key = lambda x: x[0])
	_, end = ranges[0]
	ips = []
	for min_, max_ in ranges[1:]: 
		if end > max_: 
			continue
		if min_ == end + 1 or (end > min_ and end < max_): 
			end = max_
		else: 
			ips.extend(list(range(end+1, min_)))
			end = max_
	print(ips, '\n', len(ips))

day20(inputs.day20)