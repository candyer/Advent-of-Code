
import sys

def reverse(array, n, start, step):
	if start + step < n:
		sub_array = array[start: start + step] 
	else:
		sub_array = array[start % n: ] + array[:step + start % n - n]
	sub_array = sub_array[::-1]
	for i in range(step):
		array[(start + i) % n] = sub_array[i]
	return array

def solve1(steps):
	array = range(256)
	curr = 0
	skip = 0
	for step in steps:
		array = reverse(array, 256, curr, step)
		curr += step + skip
		skip += 1
	return array[0] * array[1]
	

if __name__ == '__main__':
	for line in sys.stdin.readlines():
		array = map(int, line.split(','))
	print 'part 1 result: {}'.format(solve1(array))









		