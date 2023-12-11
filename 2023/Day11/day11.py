
# https://adventofcode.com/2023/day/11

########################
##### -- part 1 -- ##### expand the universe
########################

import sys

def manhattan_distance(pair):
	(x1, y1), (x2, y2) = pair
	return abs(x1 - x2) + abs(y1 - y2)

def solve(galaxies):
	res = 0
	n = len(galaxies)
	for i in range(n):
		for j in range(i + 1, n):
			pair = [galaxies[i], galaxies[j]]
			res += manhattan_distance(pair)
	return res

assert(solve([(0, 4), (1, 9), (2, 0), (5, 8), (6, 1), (7, 12), (10, 9), (11, 0), (11, 5)]) == 374)

if __name__ == '__main__':
	grid = []
	cols_with_galaxies = set()
	# galaxies = []
	for line in sys.stdin:
		line = list(line.strip('\n'))
		grid.append(line)
		flag = True
		for c, s in enumerate(line):
			if s == '#':
				cols_with_galaxies.add(c) 
				flag = False				
		if flag:
			grid.append(line)

	#expand the galaxy one time
	rows = len(grid)
	cols = len(grid[0])
	new = []
	galaxies = []
	for r in range(rows):
		new.append([])
		tmp = 0
		for c in range(cols):
			new[-1].append(grid[r][c])
			if c not in cols_with_galaxies:
				new[-1].append('.')
				tmp += 1
			if grid[r][c] == '#':
				galaxies.append((r, c + tmp))

	print(solve(galaxies))



########################## 
##### -- part 1/2 -- ##### don't expand the universe
##########################

import sys

def manhattan_distance(x1, y1, x2, y2):
	return abs(x1 - x2) + abs(y1 - y2)

def expand_in_between(start, end, empty_space, size):
	if start > end:
		start, end = end, start
	count = 0
	for num in empty_space:
		if start < num < end:
			count += 1
	return count * (size - 1)

def solve(galaxies, cols_without_galaxies, rows_without_galaxies, size):
	res = 0
	n = len(galaxies)
	for i in range(n):
		for j in range(i + 1, n):
			x1, y1 = galaxies[i]
			x2, y2 = galaxies[j]
			res += manhattan_distance(x1, y1, x2, y2)
			res += expand_in_between(x1, x2, rows_without_galaxies, size)
			res += expand_in_between(y1, y2, cols_without_galaxies, size)
	return res


if __name__ == '__main__':
	grid = []
	cols_with_galaxies = set()
	rows_without_galaxies = set()
	galaxies = []
	for i, line in enumerate(sys.stdin):
		line = line.strip('\n')
		grid.append(line)
		for c, s in enumerate(line):
			if s == '#':
				cols_with_galaxies.add(c) 
				galaxies.append((i, c))
		if '#' not in line:
			rows_without_galaxies.add(i)

	rows, cols = len(grid), len(grid[0])
	cols_without_galaxies = set()
	for r in range(rows):
		if r not in cols_with_galaxies:
			cols_without_galaxies.add(r)

	# size = 1 # part 1, small input 374, big input 9974721
	# size = 10 # part 2, small input 1030
	# size = 100 # part 2, small input 8410
	size = 1000000 # part 2, big input 702770569197
	print(solve(galaxies, sorted(cols_without_galaxies), sorted(rows_without_galaxies),size))




