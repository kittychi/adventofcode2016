import inputs

def day3(triangles):
	num_triangles = 0
	for triangle in triangles.split('\n'):
		sides = [int(side) for side in triangle.split()]
		perimeter = sum(sides)
		largest_side = max(sides)
		if (perimeter - largest_side > largest_side): 
			num_triangles = num_triangles + 1
	print(num_triangles)

def day3b(triangles_list):
	num_triangles = 0
	triangles = triangles_list.split('\n')
	
	triangles = [[row.split()[i] for row in triangles] for i in range(3)]
	print(triangles)
	triangles = [one[x:x+3] for x in range(0, len(triangles[1]), 3) for one in triangles]
	print(triangles)
	for triangle in triangles: 
		print(triangle)
		sides = [int(side) for side in triangle]
		if (sum(sides) - max(sides) > max(sides)):
			num_triangles = num_triangles + 1
	print(num_triangles)

test1 = '''70  878  940
10 5 25'''

test2 = '''  330  143  338
  769  547   83
  930  625  317
  669  866  147
   15  881  210
  662   15   70
  273  277  707
   50  592  770
  280  313  407'''
day3(inputs.day3input)
day3b(inputs.day3input)

