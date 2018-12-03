# https://adventofcode.com/2017/day/15

import sys

def solve1(vals):
	a, b = vals[0], vals[1]
	factor_a, factor_b = 16807, 48271
	count = 0
	for i in range(40000000):
		a = a * factor_a % 2147483647
		b = b * factor_b % 2147483647
		if a & 0xffff == b & 0xffff:
			count +=1
	return count

def solve2(vals):
	a, b = vals[0], vals[1]
	factor_a, factor_b = 16807, 48271
	count = 0
	for i in range(5000000):
		while True:
			a = a * factor_a % 2147483647
			if a % 4 == 0:
				break
		while True:
			b = b * factor_b % 2147483647
			if b % 8 == 0:
				break
		if a & 0xffff == b & 0xffff:
			count +=1
	return count		

if __name__ == '__main__':
	vals = []
	for line in sys.stdin.readlines():
		vals.append(int(line.split()[4]))
	print 'part 1 result: {}'.format(solve1(vals))
	print 'part 2 result: {}'.format(solve2(vals))

