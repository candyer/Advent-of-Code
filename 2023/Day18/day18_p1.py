
# https://adventofcode.com/2023/day/18

######################
### -- part 1 -- #####
######################

import sys
from collections import defaultdict

move = {
	'U': (-1,  0),
	'D': ( 1,  0),
	'L': ( 0, -1),
	'R': ( 0,  1),
}

def find_bounding_box(border):
	rowl, coll, rowh, colh = float('inf'), float('inf'), float('-inf'), float('-inf')
	for r, c in border:
		rowl, coll, rowh, colh = min(rowl, r), min(coll, c), max(rowh, r), max(colh, c)
	return rowl, coll, rowh, colh

def find_one_dot_inside(border):
	rowl, coll, rowh, colh = find_bounding_box(border)
	for r in range(rowl, rowh + 1):
		prev, pre = False, False
		for c in range(coll - 2, colh + 1):
			curr = (r, c) in border
			if (prev, pre, curr) == (False, True, True):
				break
			if (prev, pre, curr) == (False, True, False):
				return (r, c)
			prev = pre
			pre = curr
	raise Exception('should never happen')

def flood_fill(border):
	queue = [find_one_dot_inside(border)]
	flooded = set(border)
	while queue:
		r, c = queue.pop()
		flooded.add((r, c))

		# check 4 directions
		for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
			row = r + dr
			col = c + dc
			if (row, col) not in flooded:
				queue.append((row, col))
	return len(flooded)

def solve(plan):
	border = set()
	r, c = 0, 0
	for direction, steps, color in plan:
		dr, dc = move[direction]
		for _ in range(steps):
			r += dr
			c += dc
			border.add((r, c))
	return flood_fill(border)

assert(solve([('R', 6, '(#70c710)'), 
			 ('D', 5, '(#0dc571)'), 
			 ('L', 2, '(#5713f0)'), 
			 ('D', 2, '(#d2c081)'), 
			 ('R', 2, '(#59c680)'), 
			 ('D', 2, '(#411b91)'), 
			 ('L', 5, '(#8ceee2)'), 
			 ('U', 2, '(#caa173)'), 
			 ('L', 1, '(#1b58a2)'), 
			 ('U', 2, '(#caa171)'), 
			 ('R', 2, '(#7807d2)'), 
			 ('U', 3, '(#a77fa3)'), 
			 ('L', 2, '(#015232)'), 
			 ('U', 2, '(#7a21e3)')]) == 62)
# [
# (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), 
# (1, 0),                                         (1, 6), 
# (2, 0), (2, 1), (2, 2),                         (2, 6), 
#                 (3, 2),                         (3, 6), 
#                 (4, 2),                         (4, 6), 
# (5, 0), (5, 1), (5, 2),         (5, 4), (5, 5), (5, 6), 
# (6, 0),                         (6, 4), 
# (7, 0), (7, 1),                 (7, 4), (7, 5), (7, 6), 
#         (8, 1),                                 (8, 6), 
#         (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6)]


if __name__ == '__main__':
	plan = []
	for line in sys.stdin:
		direction, steps, color = line.strip('\n').split(' ')
		plan.append((direction, int(steps), color))
	print(solve(plan)) #46359


