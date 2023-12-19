
# https://adventofcode.com/2023/day/18

######################
### -- part 2 -- #####
######################

import sys
from collections import defaultdict

move = {
	'U': (-1,  0),
	'D': ( 1,  0),
	'L': ( 0, -1),
	'R': ( 0,  1),
}

def find_top_edge(corners):
	''' 
	   A     B
	   +-----+   +---+
	   |     |   |   |
	   | +-+ +---+   |
	   | | |         |
       | | |         |
       +-+ +---------+
	'''
	A = min(corners)
	corners.remove(A)
	B = min(corners)
	corners.remove(B)
	# print(f'{A=} {B=}')
	assert A[0] == B[0], 'A and B should be on the same row'
	return A, B

def find_bottom_edge(corners, A, B):
	''' 
	   A     B
	   +-----+   +---+
highest|     |   |   |
row -> | +-+ +---+   |
	   | | |         |
       | | |         |
       +-+ +---------+
	'''
	between = {corner for corner in corners if A[1] <= corner[1] <= B[1]}
	highest_row = min(between)[0]
	# bottom_edges = {corner for corner in between if corner[0] == highest_row}
	return highest_row


def flip_corner(corners, corner):
	''' remove if exists, add otherwise '''
	if corner in corners:
		corners.remove(corner)
		return
	corners.add(corner)

def trim(corners, A, B, highest_row):
	flip_corner(corners, (highest_row, A[1]))
	flip_corner(corners, (highest_row, B[1]))
	area = (highest_row - A[0] + 1) * (B[1] - A[1] + 1) 
	return area

def trim_highest(corners, edges):
	A, B = find_top_edge(corners)
	highest_row = find_bottom_edge(corners, A, B)
	edges[A[0]].append((A[1], B[1]))
	edges[highest_row].append((A[1], B[1]))
	return trim(corners, A, B, highest_row)

def trim_all(corners, edges):
	total = 0
	while corners:
		total += trim_highest(corners, edges)
	return total

def overlap(edges):
	total = 0
	for row in edges.values():
		stack = []
		for left, right in row:
			stack.append((left, 1))
			stack.append((right, -1))
		stack.sort()
		opened = 0
		last = None
		for curr, delta in stack:
			if opened > 1:
				total += (curr - last + 1) * (opened - 1)
			opened += delta
			last = curr
	return total

def solve(plan):
	corners = set()
	edges = defaultdict(list)
	r, c = 0, 0

	for direction, steps in plan:
		dr, dc = move[direction]
		r += dr * steps
		c += dc * steps
		corners.add((r, c))
	area = trim_all(corners, edges)
	return area - overlap(edges)

assert solve([('R', 461937), 
			 ('D', 56407), 
			 ('R', 356671), 
			 ('D', 863240), 
			 ('R', 367720), 
			 ('D', 266681), 
			 ('L', 577262), 
			 ('U', 829975), 
			 ('L', 112010), 
			 ('D', 829975), 
			 ('L', 491645), 
			 ('U', 686074), 
			 ('L', 5411), 
			 ('U', 500254)]) == 952408144115


assert solve([('R', 6), 
		 ('D', 5), 
		 ('L', 2), 
		 ('D', 2), 
		 ('R', 2), 
		 ('D', 2), 
		 ('L', 5), 
		 ('U', 2), 
		 ('L', 1), 
		 ('U', 2), 
		 ('R', 2), 
		 ('U', 3), 
		 ('L', 2), 
		 ('U', 2)]) == 62

if __name__ == '__main__':
	plan = []
	d = {'0': 'R', '1':'D', '2':'L', '3':'U'}
	for line in sys.stdin:
		direction, steps, num = line.strip('\n').split(' ')
		plan.append((d[num[-2]], int(num[2:-2], 16)))
	print(solve(plan))  #59574883048274


# (0, 0) ---------------------------------------- (0, 6)
#   |                                               | 
# (2, 0) -------- (2, 2)                            | 
#                   |                               |  
#                   |                               | 
# (5, 0) -------- (5, 2)          (5, 4) -------- (5, 6)
#   |                             (6, 4)  
# (7, 0), (7, 1)                  (7, 4) -------- (7, 6)
#            |                                      |
#         (9, 1) -------------------------------- (9, 6)





