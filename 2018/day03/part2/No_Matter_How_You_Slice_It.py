

import sys

def solve(array):
	res = set([])
	grid = [[0 for i in range(1000)] for j in range(1000)]
	for num, left, top, width, height in array:
		flag = False
		for i in range(left, left + width):
			for j in range(top, top + height):
				if grid[i][j] == 0:
					grid[i][j] = num
					res.add(num)
				else:
					flag = True
					if grid[i][j] in res:
						res.remove(grid[i][j])
					grid[i][j] = num
		if flag and num in res:
			res.remove(num)
					
	return next(iter(res)) # or res.pop()



if __name__ == '__main__':
	array = []
	for line in sys.stdin:
		claim = line.strip('\n')
		ids, rectange = claim.split('@')
		num = ids[1:]
		pos, size = rectange.split(':')
		left, top = pos.split(',')
		width, height = size.split('x')
		num, left, top, width, height = map(int, [num, left, top, width, height])
		array.append([num, left, top, width, height])
	print solve(array)



