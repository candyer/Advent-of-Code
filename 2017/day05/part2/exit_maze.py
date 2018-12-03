# # http://adventofcode.com/2017/day/5

import sys

def exit_maze(maze):
	n = len(maze)
	idx = 0
	steps = 0
	while 0 <= idx < n:
		tmp = maze[idx]
		if tmp >= 3:
			maze[idx] -= 1
		else:
			maze[idx] += 1
		idx += tmp
		steps += 1
	return steps 

if __name__ == '__main__':
	maze = []
	for line in sys.stdin:
		maze.append(int(line.strip('\n')))
	print exit_maze(maze)

# # print exit_maze([0,3,0,1,-3]) #10

