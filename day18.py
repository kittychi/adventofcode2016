import inputs

trap = ['^^.', '.^^', '^..', '..^']

def day18(start_row, num_rows): 
	rows = [start_row]

	while len(rows) < num_rows: 
		rows.append(get_next_row(rows[len(rows) - 1])) 

	print(sum([row.count('.') for row in rows]))


def get_next_row(row):

	next_row = ''.join(['^' if get_tiles(row, i) in trap else '.' for i in range(len(row))])
	return next_row


def get_tiles(row, index): 
	if index == 0: 
		return '.' + row[:index+2]
	elif index == (len(row) - 1):
		return row[index-1:] + '.'
	else:
		return row[index-1:index+2]

day18(inputs.day18, 400000)