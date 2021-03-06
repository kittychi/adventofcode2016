import inputs, re, string
from collections import defaultdict

def day4(rooms_list):
	rooms = rooms_list.split('\n')
	sector_sum = 0
	for room in rooms: 
		matched = re.search('([a-z\-]+)(\d+)\[(\w+)\]', room)
		name = matched.group(1)
		sector = matched.group(2)
		checksum = matched.group(3)
		frequency = defaultdict(int)
		for letter in name: 
			if letter == '-':
				continue
			frequency[letter] += 1

		sorted_frequency = sorted(frequency.items(), key=lambda x:(-x[1], x[0]))
		sorted_letters = [letter for (letter, freq) in sorted_frequency]
		top_5_letters= ''.join(sorted_letters[0:5])

		if (top_5_letters == checksum):
			sector_sum += int(sector)
			decipher_room_name(name, sector)
	print(sector_sum)


def decipher_room_name(name, sector_id):
	alphabet = string.ascii_lowercase
	shift = int(sector_id) % 26
	shifted_alpha = alphabet[shift:] + alphabet[:shift]
	table = str.maketrans(alphabet, shifted_alpha)
	room_name = ' '.join(name.split('-'))
	decrypted_name = room_name.translate(table)
	bunny_words = ['candy', 'dye','rabbit', 'flower', 'jellybean', 'chocolate', 'basket', 'hunt', 'bunny', 'grass', 'egg']
	if not any(word in decrypted_name for word in bunny_words):
		print(decrypted_name, sector_id)


test = '''aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]'''

day4(inputs.day4input)

decipher_room_name('qzmt-zixmtkozy-ivhz', '343')