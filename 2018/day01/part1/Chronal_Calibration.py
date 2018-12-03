import sys

if __name__ == '__main__':
	res = 0
	for line in sys.stdin:
		change = int(line.strip('\n'))
		res += change
	print res
