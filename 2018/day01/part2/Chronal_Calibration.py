import sys

def solve(changes):
	n = len(changes)
	i = 0
	tmp = 0
	## use set or dictionary, search is O(1), list is a bad idea here, because search is O(n)
	frequency = set([0]) 
	while True:
		tmp += changes[i]
		if tmp in frequency:
			return tmp
		else:
			frequency.add(tmp)
		i = (i + 1) % n


if __name__ == '__main__':
	changes = []
	for line in sys.stdin:
		changes.append(int(line.strip('\n')))
	print solve(changes)
