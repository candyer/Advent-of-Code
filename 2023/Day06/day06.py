
# https://adventofcode.com/2023/day/6

import sys

########################
##### -- part 1 -- #####
########################
def solve(times, dis):
	res = 1
	for time, d in zip(times, dis):
		count = 0
		for i in range(time + 1):
			if i * (time - i) > d:
				count += 1
		res *= count
	return res

if __name__  == '__main__':
	times = list(map(int, [ x for x in sys.stdin.readline().strip("\n").split(': ')[1].split(' ') if x]))
	dis = list(map(int, [ x for x in sys.stdin.readline().strip("\n").split(': ')[1].split(' ') if x]))
	print(solve(times, dis))

assert(solve([7, 15, 30], [9, 40, 200]) == 288)
assert(solve([44, 70, 70, 80], [283, 1134, 1134, 1491]) == 219849)




########################
##### -- part 2 -- #####
########################
def solve(time, dis):
	count = 0
	for i in range(time + 1):
		if i * (time - i) > dis:
			count += 1
	return count

if __name__  == '__main__':
	times = int(sys.stdin.readline().strip("\n").split(': ')[1].replace(' ', ''))
	dis = int(sys.stdin.readline().strip("\n").split(': ')[1].replace(' ', ''))
	print(solve(times, dis))

assert(solve(71530, 940200) == 71503)
assert(solve(44707080, 283113411341491) == 29432455)

