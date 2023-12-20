
# https://adventofcode.com/2023/day/20

######################
### -- part 1 -- #####
######################

import sys
from collections import deque, defaultdict

def make_state(config, modules):
	backward = defaultdict(list)
	for key, val in config.items():
		for v in val:
			backward[v].append(key)

	state = {}
	for key, val in modules.items():
		if val == '%':
			state[key] = False
		else:
			state[key] = {}
			for v in backward[key]:
				state[key][v] = False
	return state

def one_run(config, modules, state):
	dq = deque()
	dq.append(('broadcaster', False, 'button'))
	count = [0, 0]

	while dq:
		node, pulse, frm = dq.popleft()
		# print(f'{frm} -{pulse}-> {node}')
		count[pulse] += 1
		if node not in modules:
			continue
		if modules[node] == '%':
			if pulse:
				continue
			state[node] = not state[node]
			pulse = state[node]
		if modules[node] == '&':
			state[node][frm] = pulse
			pulse = not all(state[node].values())

		for nxt in config[node]:
			dq.append((nxt, pulse, node))

	return count

def solve(config, modules):
	# return config, modules
	state = make_state(config, modules)
	counts = [0, 0]

	for _ in range(1000):
		count = one_run(config, modules, state)
		counts[0] += count[0]
		counts[1] += count[1]
	return counts[0] * counts[1]

def main():
	config = {}
	modules = {}
	for line in sys.stdin:
		left, right = line.strip('\n').split(' -> ')
		right = right.split(', ')
		if left == 'broadcaster':
			left = '_' + left
		module = left[0]
		name = left[1:]
		config[name] = right
		modules[name] = module
	print(solve(config, modules))

if __name__ == '__main__':
	main()		
