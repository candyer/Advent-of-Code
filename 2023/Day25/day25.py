
# https://adventofcode.com/2023/day/25

import sys
from collections import defaultdict


def make_graphviz(graph):
	for key, val in graph.items():
		for v in val:
			print(key, '--', v)

from collections import deque

def find_augmenting_path(g, source='rkn', sync='blt'):
	seen = set()
	dq = deque()
	dq.appendleft((source, []))
	while dq:
		node, path = dq.pop()
		if node in seen:
			continue
		seen.add(node)
		new_path = path + [node]
		if node == sync:
			return new_path
		for sib in g[node]:
			dq.appendleft((sib, new_path))
	return []

def consume_path(g, path):
	for a, b in zip(path, path[1:]):
		g[a].remove(b)
		g[b].remove(a)

def find_connected(g, source='rkn'):
	seen = set()
	q = [source]
	while q:
		node = q.pop()
		if node in seen: continue
		seen.add(node)
		q.extend(g[node])
	return seen

def solve(g):
	# flow
	flow = 0
	while True:
		path = find_augmenting_path(g)
		if not path: break
		consume_path(g, path)
		print(f'{path=}')
		flow += 1
	assert flow == 3
	print(f'{flow=}')
	connected = find_connected(g)
	left = len(connected)
	right = len(g.keys()) - left
	return left * right

def main():
	graph = defaultdict(set)
	for line in sys.stdin:
		left, right = line.strip('\n').split(': ')
		right = right.split(' ')
		for node in right:
			graph[node].add(left)
			graph[left].add(node)
	print(solve(graph))

# print(solve({'rhn': {'hfx', 'xhk', 'bvb', 'jqt'}, 
# 			 'jqt': {'xhk', 'ntq', 'rhn', 'nvd'}, 
# 			 'xhk': {'bvb', 'ntq', 'hfx', 'jqt', 'rhn'}, 
# 			 'nvd': {'lhk', 'pzl', 'jqt', 'cmg', 'qnr'}, 
# 			 'frs': {'qnr', 'rsh', 'lhk', 'lsr'}, 
# 			 'rsh': {'rzs', 'frs', 'lsr', 'pzl'}, 
# 			 'pzl': {'hfx', 'rsh', 'lsr', 'nvd'}, 
# 			 'lsr': {'frs', 'rsh', 'lhk', 'pzl', 'rzs'}, 
# 			 'hfx': {'pzl', 'bvb', 'ntq', 'xhk', 'rhn'}, 
# 			 'qnr': {'cmg', 'rzs', 'frs', 'nvd'}, 
# 			 'cmg': {'lhk', 'bvb', 'rzs', 'qnr', 'nvd'}, 
# 			 'lhk': {'cmg', 'frs', 'lsr', 'nvd'}, 
# 			 'bvb': {'ntq', 'hfx', 'cmg', 'xhk', 'rhn'}, 
# 			 'ntq': {'hfx', 'xhk', 'bvb', 'jqt'}, 
# 			 'rzs': {'qnr', 'rsh', 'lsr', 'cmg'}}))

if __name__ == '__main__':
	main()



