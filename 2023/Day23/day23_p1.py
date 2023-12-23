
# https://adventofcode.com/2023/day/23

import sys

sys.setrecursionlimit(15000)

moves = {'^': (-1, 0), '<':(0, -1), 'v':(1, 0), '>':(0, 1), }
def solve(grid):
	pos = (0, grid[0].index('.'))
	exit = (len(grid) - 1, grid[-1].index('.'))
	visited = {pos}

	def dfs(pos, visited):
		r, c = pos
		if grid[r][c] == '#':
			return -1
		if pos in visited:
			return -1
		if pos == exit:
			return len(visited)
		visited.add(pos)
		if grid[r][c] in moves:
			dr, dc = moves[grid[r][c]]
			return dfs((r + dr, c + dc), set(visited))

		res = []
		for (dr, dc) in moves.values():
			new_r = r + dr
			new_c = c + dc
			res.append(dfs((new_r, new_c), set(visited)))
		return max(res)

	return dfs((pos[0] + 1, pos[1]), visited)


print(solve(['#.#####################', 
			 '#.......#########...###', 
			 '#######.#########.#.###', 
			 '###.....#.>.>.###.#.###', 
			 '###v#####.#v#.###.#.###', 
			 '###.>...#.#.#.....#...#', 
			 '###v###.#.#.#########.#', 
			 '###...#.#.#.......#...#', 
			 '#####.#.#.#######.#.###', 
			 '#.....#.#.#.......#...#', 
			 '#.#####.#.#.#########v#', 
			 '#.#...#...#...###...>.#', 
			 '#.#.#v#######v###.###v#', 
			 '#...#.>.#...>.>.#.###.#', 
			 '#####v#.#.###v#.#.###.#', 
			 '#.....#...#...#.#.#...#', 
			 '#.#########.###.#.#.###', 
			 '#...###...#...#...#.###', 
			 '###.###.#.###v#####v###', 
			 '#...#...#.#.>.>.#.>.###', 
			 '#.###.###.#.###.#.#v###', 
			 '#.....###...###...#...#', 
			 '#####################.#']))
def main():
	grid = []
	for line in sys.stdin:
		grid.append(line.strip('\n'))
	print(solve(grid))

if __name__ == '__main__':
	main()

