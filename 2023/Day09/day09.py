
# https://adventofcode.com/2023/day/9

import sys

def find_pattern(arr):
	next_val = arr[-1]
	while set(arr) != set([0]):
		pattern = []
		for i in range(len(arr) - 1):
			pattern.append(arr[i + 1] - arr[i])
		next_val += pattern[-1]
		arr = pattern
	return next_val

def solve(reports):
	res = 0
	for report in reports:
		res += find_pattern(report)
	return res

########################
##### -- part 1 -- #####
########################

if __name__ == '__main__':
	reports = []
	for line in sys.stdin:
		reports.append(list(map(int, line.strip("\n").split(" "))))
	print(solve(reports)) #1898776583

assert(solve([[0, 3, 6, 9, 12, 15], [1, 3, 6, 10, 15, 21], [10, 13, 16, 21, 30, 45]]) == 114)


########################
##### -- part 2 -- #####
########################

if __name__ == '__main__':
	reports = []
	for line in sys.stdin:
		reports.append(list(map(int, line.strip("\n").split(" ")[::-1]))) #[::-1] is the only differece compare to part 1
	print(solve(reports)) #1100

assert(solve([[15, 12, 9, 6, 3, 0], [21, 15, 10, 6, 3, 1], [45, 30, 21, 16, 13, 10]]) == 2)

