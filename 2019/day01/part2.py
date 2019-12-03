import sys

def solve(num: int) -> int:
	res = 0
	while num > 6:
		num = num // 3 - 2
		res += num
	return res

assert(solve(14) == 2)
assert(solve(1969) == 966)
assert(solve(100756) == 50346)

if __name__ == '__main__':
	res = 0
	for line in sys.stdin:
		mass = int(line.strip('\n'))
		res += solve(mass)
	print(res)
