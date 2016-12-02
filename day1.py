import inputs, re

facing = [(1, 0), (0, 1), (-1 ,0), (0, -1)]

def day1(directions):
	facing_index = 0
	current_pos = (0, 0)
	visited = [(0, 0)]
	for direction in directions:
		left_right = direction[0:1]
		if left_right == 'L': 
			facing_index = (facing_index - 1) % 4
		elif left_right == 'R':
			facing_index = (facing_index + 1) % 4

		number_blocks = int(direction[1:])
		for block in range(0, number_blocks):
			current_pos = traverse(current_pos, facing[facing_index])
			if current_pos in visited: 
				print("VISITED!")
				return (current_pos)
			else: 
				visited.append(current_pos)
	return(current_pos)


def traverse(position, blocks_to_add):
	return (position[0] + blocks_to_add[0], position[1] + blocks_to_add[1])

def multiply_block(number, point): 
	return (number * point[0], number * point[1])

test1 = ["R2", "L3"]
test2 = ["R2", "R2", "R2"]
test3 = ["R8", "R4", "R4", "R8"]
(x, y) = day1(inputs.day1input)
print(x, y)
print(abs(x)+abs(y))