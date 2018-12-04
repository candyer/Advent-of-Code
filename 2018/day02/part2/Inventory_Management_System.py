import sys

def check_num_of_diff_letters(a, b):
	'''
	given two sequences of letters
	return True if only one letter is different at the same position, False otherwise
	'''	
	count = 0
	for c1, c2 in zip(a, b):
		if c1 != c2:
			count += 1
			if count > 1:
				return False
	return True


def check_common_letters(a, b):
	'''
	given two sequences of letters
	return the string of common letters at the same positions
	'''	
	res = []
	for c1, c2 in zip(a, b):
		if c1 == c2:
			res.append(c1)
	return ''.join(res)


def solve(array):
	array.sort()
	for i in range(len(array) - 1):
		if check_num_of_diff_letters(array[i], array[i + 1]):
			return check_common_letters(array[i], array[i + 1])


if __name__ == '__main__':
	array = []
	for line in sys.stdin:
		array.append( line.strip('\n'))
	print solve(array)

