# https://adventofcode.com/2017/day/19


import sys

def solve(maze):
	letters = []
	steps = 0
	rows = len(maze)
	cols = len(maze[0])
	row = 0
	col = maze[0].index('|')
	direction = 'down'

	while maze[row][col] != ' ':
		steps += 1

		if not maze[row][col] in ['|', '+', '-']:
			letters.append(maze[row][col])

		if direction == 'down' and row + 1 < rows:
			row += 1
		elif direction == 'left' and col - 1 >= 0:
			col -= 1
		elif direction == 'up' and row - 1 >= 0:
			row -= 1
		elif direction == 'right' and col + 1 <= cols:
			col += 1

		if maze[row][col] == '+':
			if direction in ['up', 'down']:
				if maze[row][col - 1] != ' ':
					direction = 'left'
				else:
					direction = 'right'
			else:
				if maze[row + 1][col] != ' ':
					direction = 'down'
				else:
					direction = 'up'
	print 'part 1 result: {}'.format(''.join(letters))
	print 'part 2 result: {}'.format(steps)

if __name__ == '__main__':
	maze = []
	for line in sys.stdin.readlines():
		maze.append(line.strip('\n'))
	solve(maze)



