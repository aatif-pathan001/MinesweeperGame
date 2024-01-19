"""Create Minesweeper matrix and add bombs in it."""

import random
width = 5
height = 10

grid = [[0]*width for i in range(height)]

print(grid)

for i in range(5):
	row = random.randint(0,height - 1)
	col = random.randint(0, width - 1)
	grid[row][col]= 'b'
print(row)
print(col)

print(grid)


for i in grid:
	print(i)



print(grid[1][3])

r = set()
r.add(6)
r.add(True)
print(r)
