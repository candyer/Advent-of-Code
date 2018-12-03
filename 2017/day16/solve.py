# https://adventofcode.com/2017/day/16

import sys

def spin(array, n):
	return array[16 - n :] + array[: 16 - n]

def exchange(array, x, y):
	array[x], array[y] = array[y], array[x]
	return array

def partner(array, x, y):
	index_x = array.index(x)
	index_y = array.index(y)
	array[index_x], array[index_y] = array[index_y], array[index_x]
	return array

def solve1(moves, array):
	for move in moves:
		if move[0] == 's':
			n = int(move[1:])
			array = spin(array, n)
		elif move[0] == 'p':
			types, x, slash, y = move
			array = partner(array, x, y)
		else:
			x, y = map(int, move[1:].split('/'))
			array = exchange(array, x, y)
	return array

def cycle(moves):
	array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
	store = []
	count = 0
	while True:
		array = solve1(moves, array)
		tmp = ''.join(array)
		if tmp in store: 
			return count
		store.append(tmp)
		count += 1

def solve2(moves, array):
	for i in range(1000000000 % cycle(moves)):
		array = solve1(moves, array) 
	return ''.join(array)

if __name__ == '__main__':
	for line in sys.stdin.readlines():
		moves = line.split(',')
		array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
		print 'part 1 result: {}'.format(''.join(solve1(moves, array)))
		print 'part 2 result: {}'.format(''.join(solve2(moves, array)))




