import inputs, re, itertools, copy
from collections import defaultdict
from random import randint


closedSet = set()
def day11(setup, starting_floor):
	floors = parse_input(setup)
	s_floors = stringify(floors, starting_floor)

	# floors = parse_stringified(setup)
	# s_floors = setup

	global closedSet
	for_closed_set = generate_for_closed_set(floors, starting_floor)
	gScore = {}
	gScore[for_closed_set] = 0
	fScore = {}
	fScore[for_closed_set] = floors_heuristic(floors)

	
		
	openSet = {for_closed_set: (floors, s_floors, starting_floor)}
	cameFrom = {}
	highest = 0

	solutions = []
	while openSet: 
		
		sorted_open = sorted(openSet.items(), key= lambda x: (-fScore[x[0]], -gScore[x[0]]) )

		for_closed_set = sorted_open[-1][0]
		floors, floor_s, cur_floor = openSet.pop(for_closed_set)
		
		
		closedSet.add(for_closed_set)
		
		if (floors_heuristic(floors)) == 0: 
			solutions.append((gScore[for_closed_set], floor_s, cameFrom))
			return solutions

		next_moves = find_next_valid_move(floors, cur_floor)
		
		for (config, next_floors, next_floor_number) in next_moves: 
			next_floors_s = stringify(next_floors, next_floor_number)
			next = (next_floors, next_floors_s, next_floor_number)
			
			tent_score = gScore[for_closed_set] + len([item for item in next_floors[next_floor_number] if item not in floors[next_floor_number]])
			
			if config not in openSet.keys():
				openSet[config] = next
			elif tent_score >= gScore[config]: 
				continue

			cameFrom[next_floors_s] = floor_s
			gScore[config] = tent_score
			if len(next_floors[4]) > highest: 
				highest = len(next_floors[4])
				print(highest, len(openSet))
			fScore[config] = tent_score + floors_heuristic(next_floors)

	return solutions

def reconstruct_path(current, came_from): 
	total_path = current;
	step_count = 0
	while current in came_from.keys():
		current = came_from[current]
		total_path = current + '\n' + total_path
		step_count += 1
	print(total_path, '\n', step_count)

def stringify(floors, cur_floor):
	all_items = sorted([item for items in floors.values() for item in items])
	val = ''
	for key, items in floors.items(): 
		elevator = 'E' if key == cur_floor else ' '
		floor_ = str(key) + ' ' + elevator + ' '
		floor_ += ''.join([item+' ' if item in items else '.  ' for item in all_items])
		val = floor_ + '\n' + val
	return val

def get_type_pairs(floors, cur_floor):
	pairs = defaultdict(list)
	for key, value in sorted(floors.items()): 
		for item in sorted(value):
			pairs[item[0]].insert(0 if item[1] =='G' else 1, key)
	return pairs

def generate_for_closed_set(floors, cur_floor): 
	pairs = get_type_pairs(floors, cur_floor)
	simplified = ['%dx%d' % (item[0], item[1]) for item in pairs.values()]
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

def find_next_valid_move(floors, cur_floor):
	cur_floor_items = floors[cur_floor]
	possible_moves = get_possible_moves_for_floor(floors, cur_floor)
	configs = set()

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

				new_config = generate_for_closed_set(floors_n, new_floor_number)
				if new_config in closedSet: 
					continue
				if new_config not in configs: 
					valid_move.append((new_config, floors_n, new_floor_number))
					configs.add(new_config)
	return valid_move

def get_possible_moves_for_floor(floors, cur_floor_num):
	pairs = get_type_pairs(floors, cur_floor_num)
	pairs_on_floor = [pair for pair in pairs.items() if cur_floor_num in pair[1]]
	distinct_pair_locations = set([tuple(pair[1]) for pair in pairs_on_floor])
	distinct_pair_item_on_floor = []
	for pair in distinct_pair_locations:
		distinct_pairs = list(filter(lambda x: tuple(x[1]) == pair, sorted(pairs_on_floor)))[:2]
		itemgroup = []
		for distinct_pair in distinct_pairs:
			group = []
			if distinct_pair[1][0] == cur_floor_num: 
				group.append(distinct_pair[0]+'G')
			if distinct_pair[1][1] == cur_floor_num: 
				group.append(distinct_pair[0]+'M')
			itemgroup.append(group)
		distinct_pair_item_on_floor.append(tuple(itemgroup))

	possible_moves = set()
	mixed = []
	for pairs in distinct_pair_item_on_floor: 
		mixed.extend(pairs[0])

		flatted_pairs = [subitem for item in list(pairs) for subitem in item]
		flatted_pairs.append('')
		for pair in list(itertools.combinations(flatted_pairs, 2)): 
			possible_moves.add(pair)
	
	for pair in list(itertools.combinations(mixed, 2)): 
		possible_moves.add(pair)
		
	return list(possible_moves)

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

def parse_stringified(floors):
	floors = floors.split('\n')
	floors_d = {}
	for floor in floors: 
		items = re.findall(r'(\w\w)', floor)
		floors_d[int(floor[0])] = sorted(items)
	return floors_d


example = '''The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.'''



finish_test = '''The first floor contains nothing relevant.
The second floor contains nothing relevant.
The third floor contains nothing relevant.
The fourth floor contains a hydrogen-compatible microchip, a lithium generator, a hydrogen generator, and a lithium-compatible microchip.'''

step_test = '''The first floor contains a strontium generator and a strontium-compatible microchip.
The second floor contains a ruthenium generator, a curium generator, and a curium-compatible microchip.
The third floor contains a plutonium-compatible microchip and a ruthenium-compatible microchip.
The fourth floor contains a plutonium generator, a thulium-compatible microchip and a thulium generator.'''

test_step = '''4   .  CM .  PM .  .  .  .  .  .  
3   .  .  .  .  .  .  .  .  TG TM 
2 E CG .  PG .  RG RM SG SM .  .  
1   .  .  .  .  .  .  .  .  .  .  '''

test_step2 = '''4 E CG CM .  .  .  . PG PM RG RM SG SM TG TM 
3   .  .  .  .  .  .  .  .  .  .  .  .  .  .  
2   .  .  .  .  .  .  .  .  .  .  .  .  .  .  
1   .  .  DG DM EG EM .  .  .  .  .  .  .  .  '''


possible_solutions = sorted(day11(inputs.day11b, 1), key=lambda x: x[0])
reconstruct_path(possible_solutions[0][1], possible_solutions[0][2])