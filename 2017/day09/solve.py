# http://adventofcode.com/2017/day/9

import sys

def solve(array):
	i = 0
	while i < len(array):
		if array[i] == '!':
			array = array[:i] +  array[i + 2:]
			i = 0
		i += 1

	res_part1 = 0
	res_part2 = 0

	while '<' in array and '>' in array:
		j = array.index('<')
		k = array.index('>')	
		array = array[ : j] + array[k + 1 : ]
		res_part2 += k - j - 1	

	depth = 0
	for x in array:
		if x == "{":
			depth += 1
		if x == "}":
			res_part1 += depth
			depth -= 1
	print 'part 1 result: {}'.format(res_part1)
	print 'part 2 result: {}'.format(res_part2)

if __name__ == '__main__':
	for line in sys.stdin.readlines():
		solve(list(line))

## part 1
# assert solve(list('{{<a!>},{<a!>},{<a!>},{<ab>}}')) == 3
# assert solve(list('{{<!!>},{<!!>},{<!!>},{<!!>}}')) == 9
# assert solve(list('{{<ab>},{<ab>},{<ab>},{<ab>}}')) == 9
# assert solve(list('{{{},{},{{}}}}')) == 16
# assert solve(list('{<{!>}>}')) == 1
# assert solve(list('{<<<<<>>}')) == 1

## part 2
# assert solve(list('{{<a!>},{<a!>},{<a!>},{<ab>}}')) == 17
# assert solve(list('{{<!!>},{<!!>},{<!!>},{<!!>}}')) == 0
# assert solve(list('{{<ab>},{<ab>},{<ab>},{<ab>}}')) == 8
# assert solve(list('{{{},{},{{}}}}')) == 0
# assert solve(list('{<{!>}>}')) == 2
# assert solve(list('<random characters>')) == 17
# assert solve(list('<{!>}>')) == 2
# assert solve(list('<{o"i!a,<{i<a>')) == 10


