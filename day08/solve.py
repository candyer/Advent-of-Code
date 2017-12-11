# # http://adventofcode.com/2017/day/8

import sys
from collections import defaultdict
if __name__ == '__main__':
	data = defaultdict(int)
	max_value = 0
	for line in sys.stdin.readlines():
		name1, sign1, val1, ifs, name2, sign2, val2 = line.split()
		if eval('data[name2] ' + sign2 + val2):
			if sign1 == 'inc':
				data[name1] += int(val1)
			else:
				data[name1] -= int(val1)
			max_value = max(max_value, data[name1])
	print 'part 1 result: {}'.format(max(data.values()))
	print 'part 2 result: {}'.format(max_value)





