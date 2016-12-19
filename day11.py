import inputs, re, itertools, copy
from collections import defaultdict
from random import randint

def day11(setup):
	floors = parse_input(setup)
	s_floors = stringify(floors, 1)
	# print('STARTING\n', s_floors, '\nTHINKING\n')

	closedSet = set()

	gScore = {}
	gScore[s_floors] = 0
	fScore = {}
	fScore[s_floors] = floors_heuristic(floors)

	openSet = [(floors, s_floors, 1)]
	cameFrom = {}
	highest = 0
	while openSet: 
		# print(fScore.items())

		
		openSet = sorted(openSet, key= lambda x: (-fScore[x[1]], -gScore[x[1]]) )
		# print("CURRENT OPEN")
		# for (_, item, _) in openSet: 
		# 	print(item, fScore[item], gScore[item])

		# var = input("continue? y/n \n")
		# if var == 'n':
		# 	return
		# print("END CURRENT OPEN")

		floors, floor_s, cur_floor = openSet.pop()
		
		if (floors_heuristic(floors)) == 0: 
			# reconstruct_path(floor_s, cameFrom)
			print(gScore[floor_s])
			return (floor_s, cameFrom)

		for_closed_set = generate_for_closed_set(floors, cur_floor)
		closedSet.add(for_closed_set)

		next_moves = find_next_valid_move(cur_floor, floors)
	
		for (next_floors, next_floor_number) in next_moves: 
			next_floors_s = stringify(next_floors, next_floor_number)
			next = (next_floors, next_floors_s, next_floor_number)
			closed_set_check = generate_for_closed_set(next_floors, next_floor_number)
			if closed_set_check in closedSet: 
				continue
			tent_score = gScore[floor_s] + 1
			if next not in openSet:
				openSet.append(next)
			elif tent_score >= gScore[next_floors_s]: 
				continue

			cameFrom[next_floors_s] = floor_s
			gScore[next_floors_s] = tent_score
			if gScore[next_floors_s] > highest: 
				highest = gScore[next_floors_s]
				print(highest)
			fScore[next_floors_s] = tent_score + floors_heuristic(next_floors)
	print(False)

def reconstruct_path(current, came_from): 
	total_path = current;
	while current in came_from.keys():
		current = came_from[current]
		total_path = current + '\n' + total_path
	print(total_path)

def stringify(floors, cur_floor):
	all_items = sorted([item for items in floors.values() for item in items])
	val = ''
	for key, items in floors.items(): 
		elevator = 'E' if key == cur_floor else ' '
		floor_ = str(key) + ' ' + elevator + ' '
		floor_ += ''.join([item+' ' if item in items else '.  ' for item in all_items])
		val = floor_ + '\n' + val
	return val

def generate_for_closed_set(floors, cur_floor): 
	components = defaultdict(int)
	for key, value in floors.items(): 
		for item in value:
			components[item] = key
	sorted_items = sorted(components.items(), key = lambda x: x[0])
	simplified = ['%dx%d' % (sorted_items[2*i][1], sorted_items[2*i+1][1]) for i in range(len(sorted_items) //2)]
	return str(cur_floor)+'|'+'|'.join(sorted(simplified))

num_on_top_floor = 0

# bigger = worse
def floors_heuristic(floors): 
	val = 0
	max_floors = len(floors.keys())
	for floor, items in floors.items():
		val += len(items) * (max_floors - floor)
	return val

valid_floor_moves = { 1: [2], 2:[1,3], 3:[2,4], 4:[3]}

def add_items_to_floor(floor_items, item1, item2):
	floor_items.extend([item1, item2])
	floor_items = list(filter(lambda x: x != '', floor_items))
	return floor_items

def find_next_valid_move(cur_floor, floors):
	cur_floor_items = floors[cur_floor]
	possible_moves = list(itertools.combinations(cur_floor_items, 2))
	singles = [(item, '') for item in cur_floor_items]
	possible_moves.extend(singles)
	valid_move=[]
	for new_floor_number in valid_floor_moves[cur_floor]:
		for item1, item2 in possible_moves:
			new_floor = copy.copy(floors[new_floor_number])
			new_floor = add_items_to_floor(new_floor, item1, item2)
			updated_cur = list(filter(lambda x: x not in [item1, item2], cur_floor_items))

			if has_fried_microchip(updated_cur) or has_fried_microchip(new_floor): 
				continue
			else:
				floors_n = {}
				for key, item in floors.items(): 
					floors_n[key] = copy.deepcopy(item)
				floors_n[cur_floor] = updated_cur
				floors_n[new_floor_number] = new_floor
				valid_move.append((floors_n, new_floor_number))
	return valid_move



def has_fried_microchip(cur_floor_items):
	generators = [item[0] for item in list(filter(lambda x: x[1] == 'G', cur_floor_items))]
	microchips = [item[0] for item in list(filter(lambda x: x[1] == 'M', cur_floor_items))]
	is_fried = len(generators) > 0 and any([chip not in generators for chip in microchips])
	return is_fried
	
def parse_input(setup):
	floor_converter = {'first': 1,
					'second': 2,
					'third': 3,
					'fourth': 4}
	floor = {}
	floors_setup = setup.split('\n')
	for floor_setup in floors_setup:
		matches = re.findall(r'The (\w+) floor contains ([\w\-\, ]+)', floor_setup) 
		floor_num, item_list = matches[0]
		items = re.findall(r'a ([\w\-]+ [\w]+)', item_list)
		floor[floor_converter[floor_num]] = []
		for item in items: 
			element, component = item.split()

			cm = 'g' if len(element.split('-')) < 2 else 'm'
			shortened = element[0] + cm
			floor[floor_converter[floor_num]].append(shortened.upper())

	return floor

example = '''The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.'''



finish_test = '''The first floor contains nothing relevant.
The second floor contains nothing relevant.
The third floor contains nothing relevant.
The fourth floor contains a hydrogen-compatible microchip, a lithium generator, a hydrogen generator, and a lithium-compatible microchip.'''

# test = parse_input(inputs.day11)

# generate_for_closed_set(test, 1)

(floor, came_from) = day11(inputs.day11)
reconstruct_path(floor, came_from)
