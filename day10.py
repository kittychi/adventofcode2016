import inputs, re
from collections import defaultdict
from functools import reduce 

bots = defaultdict(list)
instructs = {}
outputs = defaultdict(list)

def day10(instructions, parta, partb):
	instructions = instructions.split('\n')
	has_two = []
	a = ''
	b = []

	for instruction in instructions:
		bot_instruct = re.findall(r'(bot \d+) gives low to (\w+ \d+) and high to (\w+ \d+)', instruction)
		init_bot = re.findall(r'value (\d+) goes to (bot \d+)', instruction)

		if len(bot_instruct) > 0:
			bot, low, high = bot_instruct[0]
			instructs[bot] = (low, high)
		else:		
			value, bot = init_bot[0]
			bots[bot].append(int(value))
			if len(bots[bot]) > 1: 
				has_two.append(bot)

	while len(has_two) > 0:
		bot = has_two.pop()
		low, high = sorted(bots[bot])
		if low == parta[0] and high == parta[1]:
			a = bot
		gives_low, gives_high = instructs[bot]
		bots[bot] = []
		if (gives(low, gives_low)):
			has_two.append(gives_low)	
		if (gives(high, gives_high)):
			has_two.append(gives_high)
	

	print('part a', a)
	for index in partb:
		b.extend(outputs[index])
	print('part b', reduce(lambda x, y: x*y, b))

def gives(value, instruct):
	receiver, number = instruct.split()
	if receiver == 'bot': 
		bots[instruct].append(value)
		if len(bots[instruct]) > 1: 
			return True
	elif receiver == 'output':
		outputs[int(number)].append(value)
	return False

test = '''value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2'''

day10(inputs.day10, (17, 61), [0,1,2])