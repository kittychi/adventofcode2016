import inputs, hashlib

hashed = {}
path_dir = 'UDLR'

coord_dir = [(1,0), (-1, 0), (0, -1), (0, 1)]

def get_unlocked_doors(code, cur_coord): 
	global hashed
	if code not in hashed.keys():
		m = hashlib.md5()
		m.update(code.encode('utf-8'))
		key = m.hexdigest()[:4]
		hashed[code] = key
	doors = [not (hashed[code][h].isdigit() or  hashed[code][h] == 'a') for h in range(4)]
	next_keys = [code + path_dir[i] if doors[i] else False for i in range(4)]
	poss_rooms = [(cur_coord[0] + coord_dir[i][0], cur_coord[1] + coord_dir[i][1]) for i in range(4)]
	next_rooms =[x if x[0] >= 0 and x[0] < 4 and x[1] >= 0 and x[1] < 4 else False for x in poss_rooms]
	
	actual_doors = [(next_keys[i],next_rooms[i]) if next_keys[i] and next_rooms[i] else False for i in range(4)]
	actual_doors = list(filter(lambda x: x, actual_doors))
	return actual_doors


def find_shortest_path(code, start, end): 
	to_visit = []

	cur_coord = start
	cur_code = code
	while cur_coord != end: 
		to_visit.extend(get_unlocked_doors(cur_code, cur_coord))
		to_visit = sorted(to_visit, key=lambda x: -len(x[0]))
		(cur_code, cur_coord) = to_visit.pop()

	print(len(cur_code[len(code):]))


def find_longest_path(code, start, end):
	to_visit = [(code, start)]

	cur_coord = start
	cur_code = code
	longest = ''

	while to_visit:
		to_visit.extend(get_unlocked_doors(cur_code, cur_coord))
		to_visit = sorted(to_visit, key=lambda x: -len(x[0]))
		(cur_code, cur_coord) = to_visit.pop()

		while cur_coord == end: 
			path = cur_code[len(code):]
			if len(path) > len(longest): 
				longest = path
			(cur_code, cur_coord) = to_visit.pop()

	print(len(longest))

test1 = 'ihgpwlah'
test2 = 'kglvqrro'
test3 = 'ulqzkmiv'

# start at (3, 0), going to (0, 3)
find_shortest_path(inputs.day17, (3, 0), (0, 3))

find_longest_path(inputs.day17, (3, 0), (0, 3))