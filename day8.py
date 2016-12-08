import inputs, collections

def day8(instructs_str):
	instructs = instructs_str.split('\n')
	print(instructs)

	screen = [['.' for x in range(50)] for y in range(6)]

	for instruct in instructs: 
		parts = instruct.split()
		print(parts)
		if parts[0] == 'rect':
			row, col = parts[1].split('x')
			for x in range(int(row)):
				for y in range(int(col)):
					screen[y][x] = '#'
		elif parts[0] == 'rotate': 
			direction = parts[1]
			if direction == 'row': 
				row = int(parts[2].split('=')[1])
				offset = int(parts[4])
				screen[row] = screen[row][-offset:] + screen[row][:-offset]
			elif direction == 'column':
				col_index = int(parts[2].split('=')[1])
				offset = int(parts[4])

				col = [row[col_index] for row in screen]
				col = col[-offset:] + col[:-offset]
				for y in range(len(col)): 
					screen[y][col_index] = col[y]

		for row in range(len(screen)):
			print(''.join(screen[row]))

	on = 0
	for row in screen: 
		on += row.count('#')
	print(on)

test= ''' rect 3x2
	rotate column x=1 by 1
	rotate row y=0 by 4
	rotate column x=1 by 1
'''

day8(inputs.day8input)	


