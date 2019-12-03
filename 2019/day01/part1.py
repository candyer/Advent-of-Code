import sys

if __name__ == '__main__':
	res = 0
	for line in sys.stdin:
		mass = int(line.strip('\n'))
		res += mass // 3 - 2
	print(res)
