# https://adventofcode.com/2024/day/2
# --- Day 2: Red-Nosed Reports ---

########################
##### -- part 1 -- #####
########################

import sys

def solve(arr):
	diffs = []
	for i in range(len(arr) - 1):
		diff = arr[i] - arr[i + 1]
		if diff <  -3 or diff > 3 or diff == 0:
			return False
		diffs.append(diff)

	if all(diff > 0 for diff in diffs):
		return True
	if all(diff < 0 for diff in diffs):
		return True

	return False

if __name__ == '__main__':
	total = 0
	for line in sys.stdin:
		arr = list(map(int, line.strip('\n').split(" ")))
		total += solve(arr)
	print( total) #680


assert(solve([7, 6, 4, 2, 1]) == True)
assert(solve([1, 2, 7, 8, 9]) == False)
assert(solve([9, 7, 6, 2, 1]) == False)
assert(solve([1, 3, 2, 4, 5]) == False)
assert(solve([8, 6, 4, 4, 1]) == False)
assert(solve([1, 3, 6, 7, 9]) == True)







