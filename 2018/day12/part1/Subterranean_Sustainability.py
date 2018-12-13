# https://adventofcode.com/2018/day/12
# https://en.wikipedia.org/wiki/Cellular_automaton

import sys
from collections import defaultdict


def solve(initial, d):
	pre = ['.'] * 10 + initial[:] + ['.'] * 100
	n = len(pre)
	for i in range(20):
		j = 0
		curr = pre[:]
		while j < n - 2:
			tmp = pre[j : j + 5]
			if tmp in d['#']:
				curr[j + 2] = '#'
			elif tmp in d['.']:
				curr[j + 2] = '.'
			j += 1
		pre = curr
	count = 0
	for i, c in enumerate(pre, start=-10):
		if c == '#':
			count += i
	return count


if __name__ == '__main__':
	array = [line.strip('\n') for line in sys.stdin]
	initial = list(array[0].split(': ')[1])
	d = defaultdict(list)
	for notes in array[2:]:
		pattern, result = notes.split(' => ')
		d[result].append(list(pattern))
	print solve(initial, d)

