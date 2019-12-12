import sys
def iterate(arr, v):
	for i in range(4):
		for j in range(i + 1, 4):
			if arr[i] < arr[j]:
				v[i] += 1
				v[j] -= 1
			elif arr[i] > arr[j]:
				v[i] -= 1
				v[j] += 1
	return v


def solve(steps, positions):
	i = 0 
	velocity = [[0 for k in range(4)] for j in range(3)]
	while i < steps:
		for j in range(3):
			velocity[j] = iterate(positions[j], velocity[j])
			positions[j] = [a + b for a, b in zip(positions[j], velocity[j])]
		i += 1

	ps = [0] * 4
	vs = [0] * 4
	for i in range(3):
		for j in range(4):
			ps[j] += abs(positions[i][j])
			vs[j] += abs(velocity[i][j])
	res = 0
	for a, b in zip(ps, vs):
		res += a * b
	return res


if __name__ == '__main__':
	positions = [[] for i in range(3)]
	for line in sys.stdin:
		i = 0
		for pos in line.strip('\n')[1:-1].split(', '):
			positions[i].append(int(pos[2:]))
			i += 1
	print(solve(1000, positions))


assert(solve(10, [[-1, 2, 4, 3], [0, -10, -8, 5], [2, -7, 8, -1]]) == 179)
assert(solve(100, [[-8, 5, 2, 9], [-10, 5, -7, -8], [0, 10, 3, -3]]) == 1940)
assert(solve(1000, [[19, 1, 14, 8], [-10, 2, -4, 7], [7, -3, 1, -6]]) == 6227)

