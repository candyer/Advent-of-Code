import sys


def solve(array):
	grid = [[0 for i in range(1000)] for j in range(1000)]
	for left, top, width, height in array:
		for i in range(left, left + width):
			for j in range(top, top + height):
				if grid[i][j] == 0:
					grid[i][j] = 1
				else:
					grid[i][j] = 2
	count = 0
	for i in range(1000):
		for j in range(1000):
			if grid[i][j] == 2:
				count += 1
	return count



if __name__ == '__main__':
	array = []
	for line in sys.stdin:
		claim = line.strip('\n')
		ids, rectange = claim.split('@')
		pos, size = rectange.split(':')
		left, top = pos.split(',')
		width, height = size.split('x')
		left, top, width, height = map(int, [left, top, width, height])
		array.append([left, top, width, height])
	print solve(array)



