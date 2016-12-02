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

test1 = ["ULL", "RRDDD", "LURDL", "UUUUD"]

day2(inputs.day2input)