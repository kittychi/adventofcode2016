import inputs
from collections import defaultdict

def day12(in_):
	registers = defaultdict(int)
	lines = in_.split('\n')
	i = 0
	registers['c'] = 1;
	while i < len(lines):
		# print(lines[i], registers)
		line = lines[i].split()
		# print('start', i, line)
		if 'cpy' in line:
			_, x, y = lines[i].split();
			if x.isdigit():
				registers[y] = int(x)
			else: 
				registers[y] = registers[x]
			i+=1
		elif 'inc' in line:
			var = line[1].strip()
			registers[var] += 1
			i+=1
		elif 'dec' in line: 
			var = line[1].strip()
			registers[var] -= 1
			# print(registers[var])
			i+=1
		elif 'jnz' in line: 
			_, x, y = lines[i].split()
			# print('jnz', x, y, registers)
			if x.isdigit() and x != 0: 
				i += int(y)
			elif registers[x] != 0:
				i += int(y)
			else: 
				i+=1
		# print("end", i)

	# 	print(registers)

	print(registers)

test = '''cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a'''

day12(inputs.day12)
