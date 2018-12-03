# https://adventofcode.com/2017/day/12


import sys
from collections import defaultdict

def dfs(graph, node, visited, children):
	if node in visited:
		return children
	children.add(node)
	visited.add(node)
	for child in graph[node]:
		dfs(graph, child, visited, children)

def solve1(graph):
	children = visited = set()
	dfs(graph, '0', visited, children)
	return len(children)

def solve2(graph):
	count = 0
	children = visited = set()
	for node in graph:
		if not node in visited:
			count += 1
			dfs(graph, node, visited, children)
	return count

if __name__ == '__main__':
	graph = defaultdict(list)
	for line in sys.stdin.readlines():
		node, children = line.strip().split(' <-> ')
		children = children.split(', ')
		for child in children:
			graph[node].append(child)
	print 'part 1 result: {}'.format(solve1(graph))
	print 'part 2 result: {}'.format(solve2(graph))


# assert solve1({'1': ['1'], '0': ['2'], '3': ['2', '4'], '2': ['0', '3', '4'], '5': ['6'], '4': ['2', '3', '6'], '6': ['4', '5']}) == 6
# assert solve2({'1': ['1'], '0': ['2'], '3': ['2', '4'], '2': ['0', '3', '4'], '5': ['6'], '4': ['2', '3', '6'], '6': ['4', '5']}) == 2


