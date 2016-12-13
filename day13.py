from astar import astar
import numpy as np

def day13(maze_size, start, end):
	maze = np.zeros(maze_size*maze_size)
	maze.shape=(maze_size, maze_size)
	for y in range(maze_size):
		for x in range(maze_size):
			num_ones = get_num_ones(x,y)
			maze[y,x] = num_ones % 2

	path_length = 1000
	iterations = 1
	while iterations < 1000:
		path = astar(maze, start, end)
		if path and len(path) < path_length:
			path_length = len(path)
			print(path_length)
			break
		else: 
			maze = add_row_and_col_to_maze(maze)
		iterations += 1

def get_num_ones(x, y):
	val = x*x + 3*x + 2*x*y + y + y*y + 1358
	binary_version = '{0:b}'.format(val)
	num_ones = binary_version.count('1')
	return num_ones

def add_row_and_col_to_maze(maze):
	rows, cols = maze.shape
	# extend maze
	new_maze = np.zeros((rows, cols+1))
	new_maze[:, :-1] = maze
	new_row = [0] * (int(cols)+1)
	new_maze =  np.vstack([new_maze, new_row])

	# calculate for new column: 
	y = cols
	for x in range(y):
		num_ones = get_num_ones(x, y)
		new_maze[y,x] = num_ones % 2
		num_ones = get_num_ones(y, x)
		new_maze[x,y] = num_ones % 2
	return new_maze

day13(35, (1, 1), (39,31))

