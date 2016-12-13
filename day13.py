from astar import astar
import numpy as np

def day13(maze_size, start, end):
	maze = np.zeros(maze_size*maze_size)
	maze.shape=(maze_size, maze_size)
	for y in range(maze_size):
		for x in range(maze_size):
			num_ones = get_num_ones(x,y)
			maze[y,x] = num_ones % 2

	reachable = get_all_shortest_path(maze, start, [])
	print(len(reachable))

def get_num_ones(x, y):
	val = x*x + 3*x + 2*x*y + y + y*y + 1350
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

def get_all_shortest_path(maze, start, reachable):
	rows, cols = maze.shape
	for y in range(rows):
		for x in range(cols):
			if (x, y) not in reachable: 
				path = astar(maze, (1, 1), (y, x))
				if path and len(path)<=50:
					reachable.append((x, y))
	return reachable

day13(50, (1, 1), (39,31))

