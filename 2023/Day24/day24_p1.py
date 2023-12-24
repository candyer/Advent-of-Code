
# https://adventofcode.com/2023/day/24

######################
### -- part 1 -- #####
######################

import sys
from itertools import combinations 

def is_inside(x, y):
	return (200000000000000 <= x <= 400000000000000) and (200000000000000 <= y <= 400000000000000)

def is_in_future(stone, x, y):
	(px, py), (vx, vy) = stone
	if vx > 0: return  x > px
	elif vx == 0: return x == px
	else: return x < px

def intersection(stone1, stone2):
	(px1, py1), (vx1, vy1) = stone1
	(px2, py2), (vx2, vy2) = stone2

	if vy1 * vx2 == vy2 * vx1 or vx1 * vy2 == vx2 * vy1:
		return float('inf'), float('inf')

	x = (px1 * vy1 * vx2 - py1 * vx1 * vx2 - px2 * vy2 * vx1 + py2 * vx2 * vx1) / (vy1 * vx2 - vy2 * vx1)
	y = (py1 * vx1 * vy2 - px1 * vy1 * vy2 - py2 * vx2 * vy1 + px2 * vy2 * vy1) / (vx1 * vy2 - vx2 * vy1)

	return x, y

def solve(hailstones):
	total = 0
	for stone1, stone2 in combinations(hailstones,2):
		x, y = intersection(stone1, stone2)
		if is_in_future(stone1, x, y) and is_in_future(stone2,  x, y):
			total += is_inside(x, y)
	return total

def main():
	hailstones = []
	for line in sys.stdin:
		pos, vilocity = line.strip('\n').split(' @ ')
		px, py, pz = list(map(int, pos.split(', ')))
		vx, vy, vz = list(map(int, vilocity.split(', ')))
		hailstones.append(((px, py), (vx, vy)))

	print(solve(hailstones))

# print(solve([((19, 13), (-2, 1)), 
# 			 ((18, 19), (-1, -1)), 
# 			 ((20, 25), (-2, -2)), 
# 			 ((12, 31), (-1, -2)), 
# 			 ((20, 19), (1, -5))]))

if __name__ == '__main__':
	main()
