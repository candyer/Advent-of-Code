
# https://adventofcode.com/2023/day/3

import sys

########################
##### -- part 1 -- #####
########################

def is_adjacent_char_special(grid,r, c):
	''' 
	grid[r][c] is a digit,
	are there adjacent special symbols: not a digit, not a dot.
	if yes, return True, else return False.
	'''
	for i in range(-1, 2):
		for j in range(-1, 2):
			if not i == j == 0:
				if not grid[r + i][c + j].isdigit() and grid[r + i][c + j]!= '.':
					return True

def solve(grid):
	total = 0
	row, col = len(grid), len(grid[0])
	r = 1
	while r < row:
		c, tmp, flag = 1, 0, False
		while c < col:
			while grid[r][c].isdigit():
				tmp *= 10
				tmp += int(grid[r][c])
				if is_adjacent_char_special(grid, r, c):
					flag = True
				c += 1
			if flag:
				total += tmp
			tmp, flag = 0, False
			c += 1
		r += 1
	return total  #532445

########################
##### -- part 2 -- #####
########################

def adjacent_numbers(grid,r, c):
	''' 
	grid[r][c] is a *,
	return the beginning position of the adjacent numbers
	'''
	pos = set()
	for i in range(-1, 2):
		for j in range(-1, 2):
			if not i == j == 0:
				if grid[r + i][c + j].isdigit():
					k = 1
					while grid[r + i][c + j - k].isdigit():
						k += 1
					pos.add((r + i, c + j - k + 1))
	return pos

def get_numbers(grid, pos):
	'''
	pos store the position of beginning of each number, get the compelete numbers
	return product of these two numbers.
	'''
	numbers = []
	for r, c in pos:
		tmp = 0
		i = 0
		while grid[r][c + i].isdigit():
			tmp *= 10
			tmp += int(grid[r][c + i])
			i += 1	
		numbers.append(tmp)
	return numbers[0] * numbers[1]		


def solve(grid):
	total = 0
	row, col = len(grid), len(grid[0])
	r = 1
	while r < row:
		c, tmp = 1, 0
		while c < col:
			while grid[r][c] == "*":
				
				pos = adjacent_numbers(grid, r, c)
				if len(pos) == 2:
					total += get_numbers(grid, pos)
				c += 1
			c += 1
		r += 1
	return total  #79842967


if __name__ == '__main__':
	total = 0
	grid = []
	count = 0
	for line in sys.stdin:
		grid.append(["."] + list(line.rstrip('\n')) + ["."] )
		count += 1
	grid = [["."] * (count + 2)] + grid + [["."] * (count + 2)] 
	print(solve(grid))

# print(solve([
# 		['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
# 		['.', '4', '6', '7', '.', '.', '1', '1', '4', '.', '.', '.'], 
# 		['.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '.', '.'], 
# 		['.', '.', '.', '3', '5', '.', '.', '6', '3', '3', '.', '.'], 
# 		['.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.'], 
# 		['.', '6', '1', '7', '*', '.', '.', '.', '.', '.', '.', '.'], 
# 		['.', '.', '.', '.', '.', '.', '+', '.', '5', '8', '.', '.'], 
# 		['.', '.', '.', '5', '9', '2', '.', '.', '.', '.', '.', '.'], 
# 		['.', '.', '.', '.', '.', '.', '.', '7', '5', '5', '.', '.'], 
# 		['.', '.', '.', '.', '$', '.', '*', '.', '.', '.', '.', '.'], 
# 		['.', '.', '6', '6', '4', '.', '5', '9', '8', '.', '.', '.'], 
# 		['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]))


