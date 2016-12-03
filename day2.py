import inputs

start = 5

instructions = {'U': lambda x: x-3 if x > 3 else x,
				'D': lambda x: x+3 if x < 7 else x,
				'L': lambda x: x-1 if x % 3 != 1 else x, 
				'R': lambda x: x+1 if x % 3 != 0 else x }

def day2(lines):
	digit = 5
	for line in lines: 
		for instruct in line[:]:
			digit = instructions[instruct](digit)
		print(digit)

binstruct = {'U': {'1':'1', '2':'2', '3':'1', '4':'4', '5':'5', '6':'2', '7':'3', '8':'4', '9':'9', 'A':'6', 'B':'7', 'C':'8', 'D':'B' },
			 'D': {'1':'3', '2':'6', '3':'7', '4':'8', '5':'5', '6':'A', '7':'B', '8':'C', '9':'9', 'A':'A', 'B':'D', 'C':'C', 'D':'D' },
			 'L': {'1':'1', '2':'2', '3':'2', '4':'3', '5':'5', '6':'5', '7':'6', '8':'7', '9':'8', 'A':'A', 'B':'A', 'C':'B', 'D':'D' }, 
			 'R': {'1':'1', '2':'3', '3':'4', '4':'4', '5':'6', '6':'7', '7':'8', '8':'9', '9':'9', 'A':'B', 'B':'C', 'C':'C', 'D':'D' }}

cinstruct = {'U': lambda x: x-2 if x in [3, 13] else x-4 if x > 4 and x not in [5, 9] else x, 
			 'D': lambda x: x+2 if x in [1, 11] else x+4 if x < 10 and x not in [5, 9] else x, 
			 'L': lambda x: x-1 if x % 4 != 2 and x not in [1, 5, 13] else  x, 
			 'R': lambda x: x+1 if x % 4 != 0 and x not in [1, 9, 13] else x}

def day2b(lines):
	digit = '5'
	for line in lines: 
		for instruct in line[:]:
			digit = binstruct[instruct][digit]
		# print("final ", hex(digit)[-1:])
		print(digit)


test1 = ["ULL", "RRDDD", "LURDL", "UUUUD"]

# print("part 1:")
# day2(inputs.day2input)
print("part 2:")
day2b(inputs.day2input)