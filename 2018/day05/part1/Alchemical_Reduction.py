# https://adventofcode.com/2018/day/5


import sys

def can_be_destroyed(chr1, chr2):
	return chr1 != chr2 and chr1.lower() == chr2.lower()

def solve(string):
	stack = [string[0]]
	count = 1
	i = 1
	while i < len(string):
		if stack and can_be_destroyed(stack[-1], string[i]):
			stack.pop()
			count -= 1
		else:
			stack.append(string[i])
			count += 1
		i += 1
	return count


if __name__ == '__main__':
	print solve(sys.stdin.readline())

