
# https://adventofcode.com/2023/day/13


########################
##### -- part 1 -- ##### 
########################

import sys

def rotate_pattern(pattern):
	r, c = len(pattern), len(pattern[0])
	new_pattern = []
	for j in range(c):
		new_pattern.append(''.join([pattern[i][j] for i in range(r)][::-1]))
	return new_pattern

# print(rotate_pattern(
# 			 ['#.##..##.', 
# 			  '..#.##.#.', 
# 			  '##......#', 
# 			  '##......#', 
# 			  '..#.##.#.', 
# 			  '..##..##.', 
# 			  '#.#.##.#.']))

def is_mirror(pattern, i):
	j = i + 1
	while i >= 0 and j < len(pattern):
		if pattern[i] != pattern[j]:
			return False
		i -= 1
		j += 1
	return True

def find_horizontal_mirror(pattern): #compare rows
	n = len(pattern)
	for i in range(n - 1):
		if is_mirror(pattern, i):
			return i + 1

def find_vertical_mirror(pattern):
	return find_horizontal_mirror(rotate_pattern(pattern))

def find_mirror(pattern):
	m = find_horizontal_mirror(pattern)
	if m: return m, 0
	return find_vertical_mirror(pattern), 1

def solve(patterns):
	vals = [0, 0]
	for pattern in patterns:
		m, i = find_mirror(pattern)
		vals[i] += m
	return 100 * vals[0] + vals[1]

# print(solve([['##..###..#.####',
# 			'.........#.##.#',
# 			'##...#...##..##',
# 			'##..##.##..##..',
# 			'##.###.##.####.',
# 			'......##..####.',
# 			'###.###.#......',
# 			'...#..###..##..',
# 			'....#..########',
# 			'..##.###.#.##.#',
# 			'###.###..#.##.#',
# 			'##.##.###.#..#.',
# 			'...#...##......',
# 			'##.......#.##.#',
# 			'..#####...####.',
# 			'...##.#...#..#.',
# 			'##.####.#######']]))

# print(solve([['#.##..##.', 
# 			  '..#.##.#.', 
# 			  '##......#', 
# 			  '##......#', 
# 			  '..#.##.#.', 
# 			  '..##..##.', 
# 			  '#.#.##.#.'], 

#              ['#...##..#', 
#               '#....#..#', 
#               '..##..###', 
#               '#####.##.', 
#               '#####.##.', 
#               '..##..###', 
#               '#....#..#']]))

if __name__ == '__main__':
	patterns = [[]]
	for line in sys.stdin:
		if line == '\n':
			patterns.append([])
		else:
			patterns[-1].append(line.strip('\n'))
	print(solve(patterns))











########################
##### -- part 2 -- ##### 
########################


import sys

def rotate_pattern(pattern):
	r, c = len(pattern), len(pattern[0])
	new_pattern = []
	for j in range(c):
		new_pattern.append(''.join([pattern[i][j] for i in range(r)][::-1]))
	return new_pattern

def hamming_distance(s1, s2):
	return sum(a != b for a, b in zip(s1, s2))

def is_mirror(pattern, i):
	j = i + 1
	edited = False
	while i >= 0 and j < len(pattern):
		hd = hamming_distance(pattern[i], pattern[j])
		if hd > 1:
			return False
		if hd == 1 and edited:
			return False
		if hd == 1:
			edited = True
		i -= 1
		j += 1
	return edited 

def find_horizontal_mirror(pattern): #compare rows
	n = len(pattern)
	for i in range(n - 1):
		if is_mirror(pattern, i):
			return i + 1

def find_vertical_mirror(pattern):
	return find_horizontal_mirror(rotate_pattern(pattern))

def find_mirror(pattern):
	m = find_horizontal_mirror(pattern)
	if m: return m, 0
	return find_vertical_mirror(pattern), 1

def solve(patterns):
	vals = [0, 0]
	for pattern in patterns:
		m, i = find_mirror(pattern)
		vals[i] += m
		# print(m)
	return 100 * vals[0] + vals[1]

# print(solve([['##..###..#.####',
# 			'.........#.##.#',
# 			'##...#...##..##',
# 			'##..##.##..##..',
# 			'##.###.##.####.',
# 			'......##..####.',
# 			'###.###.#......',
# 			'...#..###..##..',
# 			'....#..########',
# 			'..##.###.#.##.#',
# 			'###.###..#.##.#',
# 			'##.##.###.#..#.',
# 			'...#...##......',
# 			'##.......#.##.#',
# 			'..#####...####.',
# 			'...##.#...#..#.',
# 			'##.####.#######']]))

# print(solve([['#.##..##.', 
# 			  '..#.##.#.', 
# 			  '##......#', 
# 			  '##......#', 
# 			  '..#.##.#.', 
# 			  '..##..##.', 
# 			  '#.#.##.#.'], 

#              ['#...##..#', 
#               '#....#..#', 
#               '..##..###', 
#               '#####.##.', 
#               '#####.##.', 
#               '..##..###', 
#               '#....#..#']]))

if __name__ == '__main__':
	patterns = [[]]
	for line in sys.stdin:
		if line == '\n':
			patterns.append([])
		else:
			patterns[-1].append(line.strip('\n'))
	print(solve(patterns))
