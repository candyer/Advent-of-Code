
# https://adventofcode.com/2024/day/1
# --- Day 1: Historian Hysteria ---

########################
##### -- part 1 -- #####
########################

import sys

def solve(left, right):
	total = 0
	left.sort()
	right.sort()
	for l, r in zip(left, right):
		total += abs(r - l)
	return total

if __name__ == '__main__':
	left, right = [], []
	for line in sys.stdin:
		l, r = line.strip('\n').split("   ")
		left.append(int(l))
		right.append(int(r))
	print(solve(left,right)) #1388114
	
assert(solve([3, 4, 2, 1, 3, 3],[4, 3, 5, 3, 9, 3]) == 11)


########################
##### -- part 2 -- #####
########################

import sys
from collections import defaultdict

def solve(left, right):
	total = 0
	for l in left:
		total += int(l) * right[l]
	return total

if __name__ == '__main__':
	left, right = [], defaultdict(int)
	for line in sys.stdin:
		l, r = line.strip('\n').split("   ")
		left.append(l)
		right[r] += 1
	print(solve(left,right)) #23529853


###########################

import sys
from collections import Counter

def solve(left, right):
	right = Counter(right)
	total = 0
	for l in left:
		total += int(l) * right[l]
	return total

if __name__ == '__main__':
	left, right = [], []
	for line in sys.stdin:
		l, r = line.strip('\n').split("   ")
		left.append(l)
		right.append(r)
	print(solve(left,right)) #23529853
