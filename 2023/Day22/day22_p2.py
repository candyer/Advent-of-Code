# https://adventofcode.com/2023/day/22

######################
### -- part 2 -- #####
######################

import sys
from collections import defaultdict

def solve(bricks):
	bricks.sort(key=lambda x: x[0][2])
	basalt = defaultdict(lambda: (0, 0)) # (height "z", id of the thing "floor")
	above_me = defaultdict(set)
	below_me = defaultdict(set)

	idx = 1
	for brick in bricks:
		(x1, y1, z1), (x2, y2, z2) = brick
		assert x1 <= x2
		assert y1 <= y2
		assert z1 <= z2
		# find tallest spot bellow me
		tallest = 0
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				val, _ = basalt[(x, y)]
				tallest = max(tallest, val)
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				val, surface = basalt[(x, y)]
				if val == tallest:
					above_me[surface].add(idx)
					below_me[idx].add(surface)
		# update the world after I land
		tallest += (z2 - z1) + 1
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				basalt[(x, y)] = (tallest, idx)
		idx += 1

	return would_fall(above_me, below_me)

def would_fall(above_me, below_me):
	def rec(surface, removed):
		if not below_me[surface].issubset(removed): return 0
		if surface not in above_me: return 1
		total = 1
		removed.add(surface)
		for above in above_me[surface]:
			total += rec(above, removed)
		return total

	tot = 0
	for surface, aboves in above_me.items():
		if surface == 0: continue
		removed = {surface}
		for above in aboves:
			tot += rec(above, removed)
	return tot

def main():
	bricks = []
	for line in sys.stdin:
		left, right = line.strip('\n').split('~')
		left = list(map(int, left.split(',')))
		right = list(map(int, right.split(',')))
		bricks.append([left, right])
	print(solve(bricks))

if __name__ == '__main__':
	main()

