
# https://adventofcode.com/2023/day/14

#######################
#### -- part 1A -- #### no moving 
#######################

import sys

def solve(grid):
	rows, cols = len(grid), len(grid[0])
	total = 0
	for c in range(cols):
		distance = rows
		for r in range(rows):
			if grid[r][c] == 'O':
				total += distance
				distance -= 1		
			elif grid[r][c] == '#':
				distance = rows - r - 1
	return total

if __name__ == '__main__':
	grid = []
	for line in sys.stdin:
		grid.append(line.strip('\n'))
	print(solve(grid))



#######################
#### -- part 1B -- #### moving 
#######################

import sys

def count_score(grid):
	res = 0
	rows, cols = len(grid), len(grid[0])
	for r in range(rows):
		for c in range(cols):
			if grid[r][c] == 'O':
				res += rows - r
	return res 

def tilt_north(grid):
	rows, cols = len(grid), len(grid[0])
	for c in range(cols):
		pos = float('inf')
		for r in range(rows):
			if grid[r][c] == '.':
				if pos > r:
					pos = r
			elif grid[r][c] == 'O':
				if pos <= r:
					grid[r][c], grid[pos][c] = '.', 'O'
					pos += 1
			else:
				pos = r + 1
	return grid

if __name__ == '__main__':
	grid = []
	for line in sys.stdin:
		grid.append(line.strip('\n'))
	print(count_score(tilt_north(grid)))


print(solve(['O....#....', 
			 'O.OO#....#', 
			 '.....##...', 
			 'OO.#O....O', 
			 '.O.....O#.', 
			 'O.#..O.#.#', 
			 '..O..#O..O', 
			 '.......O..', 
			 '#....###..', 
			 '#OO..#....']) == 136)


########################
##### -- part 2 -- ##### 
########################

import sys

def count_score(grid):
	res = 0
	rows, cols = len(grid), len(grid[0])
	for r in range(rows):
		for c in range(cols):
			if grid[r][c] == 'O':
				res += rows - r
	return res 


def tilt_north(grid):
	rows, cols = len(grid), len(grid[0])
	for c in range(cols):
		pos = float('inf')
		for r in range(rows):
			if grid[r][c] == '.':
				if pos > r:
					pos = r
			elif grid[r][c] == 'O':
				if pos <= r:
					grid[r][c], grid[pos][c] = '.', 'O'
					pos += 1
			else:
				pos = r + 1
	return grid


def rotate_grid_right(grid):
	rows, cols = len(grid), len(grid[0])
	new_grid = []
	for c in range(cols):
		new_grid.append([grid[r][c] for r in range(rows)][::-1])
	return new_grid

def one_cycle(grid):
	for i in range(4):
		grid = tilt_north(grid)
		grid = rotate_grid_right(grid)
	return grid

def totuple(x):
	return tuple(tuple(k) for k in x)

def solve(grid):
	seen = {}
	rseen = {}
	for i in range(1000000000):
		seen[totuple(grid)] = i
		rseen[i] = totuple(grid)
		grid = one_cycle(grid)
		key = totuple(grid)
		if key in seen:
			break
	start = seen[key]
	end = i + 1
	loop = end - start
	idx = ((1000000000 - start) % loop) + start
	return count_score(rseen[idx])

if __name__ == '__main__':
	grid = []
	for line in sys.stdin:
		grid.append(line.strip('\n'))
	print(count_score(tilt_north(grid)))

print(solve(['O....#....', 
			 'O.OO#....#', 
			 '.....##...', 
			 'OO.#O....O', 
			 '.O.....O#.', 
			 'O.#..O.#.#', 
			 '..O..#O..O', 
			 '.......O..', 
			 '#....###..', 
			 '#OO..#....']) == 64)

