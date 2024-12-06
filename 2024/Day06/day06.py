# https://adventofcode.com/2024/day/6
# --- Day 6: Guard Gallivant ---

########################
##### -- part 1 -- #####
########################

import sys

def solve(grid, r, c):
	count = 0
	visited = set()
	rows, cols = len(grid), len(grid[0])
	direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
	d = 0
	while -1 < r < rows and -1 < c < cols:
		visited.add((r, c))
		if grid[r][c] == "#":
			visited.remove((r, c))
			r -= direction[d][0]
			c -= direction[d][1]
			d = (d + 1) % 4
		else:
			r += direction[d][0]
			c += direction[d][1]
	return len(visited)


if __name__ == "__main__":
	grid = []
	r = 0
	for i, line in enumerate(sys.stdin):
		row = line.strip("\n")
		if "^" in row:
			r = i
			c = row.index("^")
		grid.append(row)

	print(solve(grid, r, c)) #5067


assert(solve([
	'....#.....', 
	'.........#', 
	'..........', 
	'..#.......', 
	'.......#..', 
	'..........', 
	'.#..^.....', 
	'........#.', 
	'#.........', 
	'......#...'], 
	6, 4) == 41)

