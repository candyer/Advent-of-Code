# https://adventofcode.com/2017/day/11

import sys

def solve(array):
	coor = [0, 0, 0]
	res1 = res2 = 0
	for step in array:

		if step == 'n':
			coor[1] += 1
			coor[2] -= 1
		elif step == 's':
			coor[1] -= 1
			coor[2] += 1

		if step == 'ne':
			coor[0] += 1
			coor[2] -= 1
		elif step == 'sw':
			coor[0] -= 1
			coor[2] += 1

		elif step == 'nw':
			coor[0] -= 1
			coor[1] += 1
		elif step == 'se':
			coor[0] += 1
			coor[1] -= 1
	
		# print coor
		tmp = (abs(coor[0]) + abs(coor[1]) + abs(coor[2])) / 2
		res1 = tmp
		res2 = max(res2, tmp)

	print 'part 1 result: {}'.format(res1)
	print 'part 2 result: {}'.format(res2)

if __name__ == '__main__':
	for line in sys.stdin.readlines():
		array = line.split(',')
		solve(array)

# print solve(['ne','ne','ne']) == 3
# print solve(['ne','ne','sw','sw']) == 0
# print solve(['ne','ne','s','s']) == 2
# print solve(['se','sw','se','sw','sw']) == 3
