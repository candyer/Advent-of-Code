# https://adventofcode.com/2017/day/22

import sys

def solve1(data):
	moveTo = [(0, -1), (1, 0), (0, 1), (-1, 0)] #up, right, down, left
	rows = len(data)
	cols = len(data[0])
	pos = (rows / 2, cols / 2)
	direction = 0
	grid = {}
	for i, line in enumerate(data):
		for j, state in enumerate(line):
			grid[(j, i)] = state

	res = 0
	for k in range(10000):
		if not pos in grid:
			grid[pos] = '.'

		# the current noce is infected, turn to right, it becomes cleaned
		if grid[pos] == '#':
			grid[pos] = '.'
			direction = (direction + 1) % 4

		# the current noce is clean, turn to left, it becomes infected
		# result increment one
		else:
			direction = (direction + 3) % 4
			grid[pos] = '#'
			res += 1
		pos = tuple(map(sum, zip(pos, moveTo[direction])))
	return res

if __name__ == '__main__':
	data = []
	for line in sys.stdin.readlines():
		data.append(line.strip())
	print 'part 1 result: {}'.format(solve1(data))


