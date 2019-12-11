'''
Brute Force:

- for each *current # point* that is not on the border, check the slope of this coordinate with every *other # points*
  (except the same row, otherrwise ZeroDivisionError will occur)
- special case:it's possible that the certain point is in between of two visible points
- save all these slopes in a dictionary = {(slope, position above / below the current point), times of the }
- check if there are points visible on the same row

'''

import sys
from collections import defaultdict
from typing import List
def slope(point1: List[int], point2: List[int]) -> float:
	x1, y1 = point1
	x2, y2 = point2
	x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
	return  (y2 - y1) / (x2 - x1)

def sight(grid: List[str], rows: int, cols: int, r: int, c: int) -> int:
	d = defaultdict(int)
	for i in range(rows):
		for j in range(cols):
			if grid[i][j] == '#' and (r != i):
				s = slope([r, c], [i, j])
				if i < r:
					d[(s, 'above')] += 1
				else:
					d[(s, 'below')] += 1
	res = len(d)
	for j in range(c - 1, -1, -1):
		if grid[r][j] == '#':
			res += 1
			break
	for j in range(c + 1, cols):
		if grid[r][j] == '#':
			res += 1
			break		
	return res

def solve(grid: List[str]) -> int:
	rows = len(grid)
	cols = len(grid[0])
	res = 0
	for r in range(1, rows - 1):
		for c in range(1, cols - 1):
			if grid[r][c] == '#':
				res = max(res, sight(grid, rows, cols, r, c))
	return res

if __name__ == '__main__':
	grid = []
	for line in sys.stdin:
		grid.append(line.strip('\n'))
	print(solve(grid))


assert(solve([
	'......#.#.', 
	'#..#.#....', 
	'..#######.', 
	'.#.#.###..', 
	'.#..#.....', 
	'..#....#.#', 
	'#..#....#.', 
	'.##.#..###', 
	'##...#..#.', 
	'.#....####']
	) == 33)

assert(solve([
	'#.#...#.#.', 
	'.###....#.', 
	'.#....#...', 
	'##.#.#.#.#', 
	'....#.#.#.', 
	'.##..###.#', 
	'..#...##..', 
	'..##....##', 
	'......#...', 
	'.####.###.']
	) == 35)

assert(solve([
	'.#..#..###', 
	'####.###.#', 
	'....###.#.', 
	'..###.##.#', 
	'##.##.#.#.', 
	'....###..#', 
	'..#.#..#.#', 
	'#..#.#.###', 
	'.##...##.#', 
	'.....#.#..']
	) == 41)

assert(solve([
	'.#..##.###...#######', 
	'##.############..##.', 
	'.#.######.########.#', 
	'.###.#######.####.#.', 
	'#####.##.#.##.###.##', 
	'..#####..#.#########', 
	'####################', 
	'#.####....###.#.#.##', 
	'##.#################', 
	'#####.##.###..####..', 
	'..######..##.#######', 
	'####.##.####...##..#', 
	'.#####..#.######.###', 
	'##...#.##########...', 
	'#.##########.#######', 
	'.####.#.###.###.#.##', 
	'....##.##.###..#####', 
	'.#.#.###########.###', 
	'#.#.#.#####.####.###', 
	'###.##.####.##.#..##']
	) == 210)


assert(solve([
	'#.#.###.#.#....#..##.#....', 
	'.....#..#..#..#.#..#.....#', 
	'.##.##.##.##.##..#...#...#', 
	'#.#...#.#####...###.#.#.#.', 
	'.#####.###.#.#.####.#####.', 
	'#.#.#.##.#.##...####.#.##.', 
	'##....###..#.#..#..#..###.', 
	'..##....#.#...##.#.#...###', 
	'#.....#.#######..##.##.#..', 
	'#.###.#..###.#.#..##.....#', 
	'##.#.#.##.#......#####..##', 
	'#..##.#.##..###.##.###..##', 
	'#..#.###...#.#...#..#.##.#', 
	'.#..#.#....###.#.#..##.#.#', 
	'#.##.#####..###...#.###.##', 
	'#...##..#..##.##.#.##..###', 
	'#.#.###.###.....####.##..#', 
	'######....#.##....###.#..#', 
	'..##.#.####.....###..##.#.', 
	'#..#..#...#.####..######..', 
	'#####.##...#.#....#....#.#', 
	'.#####.##.#.#####..##.#...', 
	'#..##..##.#.##.##.####..##', 
	'.##..####..#..####.#######', 
	'#.#..#.##.#.######....##..', 
	'.#.##.##.####......#.##.##'
	]) == 269)

