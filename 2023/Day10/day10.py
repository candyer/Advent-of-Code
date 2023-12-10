
# https://adventofcode.com/2023/day/10

import sys

########################
##### -- part 1 -- #####
########################

UP    = (-1,  0)
DOWN  = ( 1,  0)
LEFT  = ( 0, -1)
RIGHT = ( 0,  1)

PIPES = {
	'J': (UP, LEFT),
	'L': (UP, RIGHT),
	'F': (DOWN, RIGHT),
	'7': (DOWN, LEFT),
	'|': (UP, DOWN),
	'-': (LEFT, RIGHT),
}

def first_step(start, maze):
	d = {UP: '|F7', DOWN: '|JL', LEFT: '-LF', RIGHT: '-J7'}
	row, col = start
	for (dr, dc), v in d.items():
		r, c = row + dr, col + dc
		if maze[r][c] in v:
			return (r, c)
	raise(Exception('should never happen'))

def next_step_iter(pos, maze, seen):
	todo = [pos]
	while todo:
		pos = todo.pop()
		if pos in seen: continue
		seen.add(pos)
		row, col = pos
		curr = maze[row][col]
		for dr, dc in PIPES[curr]:
			r, c = row + dr, col + dc
			todo.append((r, c))

def solve(start, maze):
	row, col = len(maze), len(maze[0])
	maze = [['.'] * col] + maze + [['.'] * col]
	pos = first_step(start, maze)
	seen = {start}
	next_step_iter(pos, maze, seen)
	return (len(seen) + 1) // 2

if __name__ == '__main__':
	maze = []
	start = None
	for i, line in enumerate(sys.stdin):
		maze.append(['.'] + list(line.strip('\n')) + ['.'])
		if 'S' in maze[-1]:
			start = (i + 1, maze[-1].index('S'))
	print(solve(start, maze))



########################
##### -- part 2 -- #####
########################
import sys

UP    = (-1,  0)
DOWN  = ( 1,  0)
LEFT  = ( 0, -1)
RIGHT = ( 0,  1)

PIPES = {
	'J': (UP, LEFT),
	'L': (UP, RIGHT),
	'F': (DOWN, RIGHT),
	'7': (DOWN, LEFT),
	'|': (UP, DOWN),
	'-': (LEFT, RIGHT),
}

def figure_start(dirs):
	for k, ds in PIPES.items():
		if all(d in ds for d in dirs):
			return k

def first_step(start, maze):
	d = {UP: '|F7', DOWN: '|JL', LEFT: '-LF', RIGHT: '-J7'}
	row, col = start
	res = []
	for (dr, dc), v in d.items():
		r, c = row + dr, col + dc
		if maze[r][c] in v:
			res.append((dr, dc))
	return res

def next_step_iter(pos, maze, seen):
	todo = [pos]
	while todo:
		pos = todo.pop()
		if pos in seen: continue
		seen.add(pos)
		row, col = pos
		curr = maze[row][col]
		for dr, dc in PIPES[curr]:
			r, c = row + dr, col + dc
			todo.append((r, c))

def count_inside(maze, seen):
	total = 0
	for r, row in enumerate(maze):
		is_inside = False
		prev = '.'
		for c, el in enumerate(row):
			if el == '.' or (r, c) not in seen:
				total += is_inside
				prev = '.'
				continue
			if el == '-': continue
			is_inside = not is_inside
			if prev + el in ('L7', 'FJ'): is_inside = not is_inside
			prev = el
	return total


def solve(start, maze):
	row, col = len(maze), len(maze[0])
	maze = [['.'] * col] + maze + [['.'] * col]
	dirs = first_step(start, maze)
	dr, dc = dirs[0]
	r, c = start
	pos = (r + dr, c + dc)
	maze[r][c] = figure_start(dirs)
	seen = {start}
	next_step_iter(pos, maze, seen)
	return count_inside(maze, seen)


if __name__ == '__main__':
	maze = []
	start = None
	for i, line in enumerate(sys.stdin):
		maze.append(['.'] + list(line.strip('\n')) + ['.'])
		if 'S' in maze[-1]:
			start = (i + 1, maze[-1].index('S'))
	print(solve(start, maze))


