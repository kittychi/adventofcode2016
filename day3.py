import inputs

def day3(triangles):
	num_triangles = 0
	for triangle in triangles.split('\n'):
		# print(triangle)
		sides = [int(side) for side in triangle.split()]
		perimeter = sum(sides)
		largest_side = max(sides)
		if (perimeter - largest_side > largest_side): 
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
   50  592  770'''
day3(inputs.day3input)

