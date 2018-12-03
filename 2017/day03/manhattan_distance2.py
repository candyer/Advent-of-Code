# # http://adventofcode.com/2017/day/3

# # As a stress test on the system, the programs here clear the grid and 
# # then store the value 1 in square 1. Then, in the same allocation order 
# # as shown above, they store the sum of the values in all adjacent squares, 
# # ncluding diagonals.

# # So, the first few squares' values are chosen as follows:

# # Square 1 starts with the value 1.
# # Square 2 has only one adjacent filled square (with value 1), so it also 
# # 	stores 1.
# # Square 3 has both of the above squares as neighbors and stores the sum 
# # 	of their values, 2.
# # Square 4 has all three of the aforementioned squares as neighbors and 
# # 	stores the sum of their values, 4.
# # Square 5 only has the first and fourth squares as neighbors, so it gets 
# # 	the value 5.
# # Once a square is written, its value does not change. Therefore, the first 
# # few squares would receive the following values:

# # 147  142  133  122   59
# # 304    5    4    2   57
# # 330   10    1    1   54
# # 351   11   23   25   26
# # 362  747  806--->   ...
# # What is the first value written that is larger than your puzzle input?

def val(x, y, grid):
	res = 0
	for i in range(-1, 2):
		for j in range(-1, 2):
			res += grid.get((x + i, y + j), 0)
	return res

def f(n):
	states = [
		#while condition /  move to
		((-1, 0), (0, 1)), #up
		((0, -1), (-1, 0)), #left
		((1,  0), (0, -1)), #down
		((0,  1), (1, 0)) #right
	]

	x, y = 1, 0
	grid = {(0,0): 1}

	state = 0
	while True:
		condition = states[state][0]
		move = states[state][1]
		while (x + condition[0], y + condition[1]) in grid:
			grid[(x, y)] = val(x, y, grid)
			if grid[(x, y)] > n:
				return grid[(x, y)]
			x += move[0]
			y += move[1]
		state = (state + 1) % 4 # 4 is the length of states

assert f(312051) == 312453
assert f(27) == 54







