import sys

from collections import Counter as c
def check_duplicate(s):
	'''
	given a sequence of letters
	return (if duplicate of 2 letters exist, if duplicate of 3 letters exist)
	'''
	two = three = False
	if 2 in c(s).values():
		two = True
	if 3 in c(s).values():
		three = True
	return (two, three)

def solve(array):
	a = b = 0
	for subarray in array:
		two, three = check_duplicate(subarray)
		if two:
			a += 1
		if three:
			b += 1
	return a * b

if __name__ == '__main__':
	array = []
	for line in sys.stdin:
		array.append( line.strip('\n'))
	print solve(array)
