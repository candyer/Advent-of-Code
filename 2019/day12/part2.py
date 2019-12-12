import sys
from math import gcd

def lcm(a, b):
    return (a * b) // gcd(a, b)

def simulation(arr, v):
	for i in range(4):
		for j in range(i + 1, 4):
			if arr[i] < arr[j]:
				v[i] += 1
				v[j] -= 1
			elif arr[i] > arr[j]:
				v[i] -= 1
				v[j] += 1
	return [a + b for a, b in zip(arr, v)]

def loop(pos, v):
	copy_pos = pos[:]
	i = 1
	while True:
		pos = simulation(pos, v)
		if pos == copy_pos:
			return i + 1
		i += 1

def solve(positions):
	count = []
	res = 1
	for j in range(3):
		tmp = loop(positions[j], [0, 0, 0, 0])
		res = lcm(res, tmp)
	return res


if __name__ == '__main__':
	positions = [[] for i in range(3)]
	for line in sys.stdin:
		i = 0
		for pos in line.strip('\n')[1:-1].split(', '):
			positions[i].append(int(pos[2:]))
			i += 1
	print(solve(positions))

assert(solve([[-1, 2, 4, 3], [0, -10, -8, 5], [2, -7, 8, -1]]) == 2772)
assert(solve([[19, 1, 14, 8], [-10, 2, -4, 7], [7, -3, 1, -6]]) == 331346071640472)
assert(solve([[-8, 5, 2, 9], [-10, 5, -7, -8], [0, 10, 3, -3]]) == 4686774924)
