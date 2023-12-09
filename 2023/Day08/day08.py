
# https://adventofcode.com/2023/day/8

import sys
from collections import defaultdict

########################
##### -- part 1 -- #####
########################

def solve(instructions, network):
	start, steps, n = 'AAA', 0, len(instructions)
	while True:
		if instructions[steps % n ] == 'L':
			start = network[start][0]
		else:
			start = network[start][1]
		steps += 1
		if start == 'ZZZ':
			return steps #18673

if __name__ == "__main__":
	instructions = sys.stdin.readline().strip("\n")
	_ = sys.stdin.readline()
	network = defaultdict(list)
	for line in sys.stdin:
		start, end = line.strip("\n").split(" = ")
		end = end[1:-1].split(", ")
		network[start] = end
	print(solve(instructions, network))

assert(solve('RL', 
			{'AAA': ['BBB', 'CCC'], 
			 'BBB': ['DDD', 'EEE'], 
			 'CCC': ['ZZZ', 'GGG'], 
			 'DDD': ['DDD', 'DDD'], 
			 'EEE': ['EEE', 'EEE'], 
			 'GGG': ['GGG', 'GGG'], 
			 'ZZZ': ['ZZZ', 'ZZZ']}) == 2)

assert(solve('LLR', 
			{'AAA': ['BBB', 'BBB'], 
			 'BBB': ['AAA', 'ZZZ'], 
			 'ZZZ': ['ZZZ', 'ZZZ']}) == 6)


########################
##### -- part 2 -- #####
########################

# reuse the code from part 1 to find the steps for each starting node
# then find the "Least common multiple" of these steps

'''
the input loops perfectly, so this solution works, otherwise it won't.
for the example below, you need an extra step to find the real loop, 
which is 11A -> 11B -> 11C <=> 11Z

L
11A = (11B, XXX)
11B = (11C, XXX)
11C = (11Z, XXX)
11Z = (11C, XXX)
XXX = (XXX, XXX)
'''

def count_steps(instructions, network):
	start, steps, n = 'AAA', 0, len(instructions)
	while True:
		if instructions[steps % n ] == 'L':
			start = network[start][0]
		else:
			start = network[start][1]
		steps += 1
		if start == 'ZZZ':
			return steps #18673

def lcm(arr):
	return reduce(lambda x, y: (x * y) // math.gcd(x , y), arr)

def solve(starting_nodes, instructions, network):
	steps = []
	for starting_node in starting_nodes:
		steps.append(count_steps(instructions, network))
	return lcm(steps)

if __name__ == "__main__":
	instructions = sys.stdin.readline().strip("\n")
	_ = sys.stdin.readline()
	network = defaultdict(list)
	starting_nodes = []
	for line in sys.stdin:
		start, end = line.strip("\n").split(" = ")
		end = end[1:-1].split(", ")
		if start.endswith('A'):
			starting_nodes.append(start)
		network[start] = end
	print(solve(starting_nodes, instructions, network)) #17972669116327

assert (solve(['11A', '22A'], 'LR',
			{'11A': ['11B', 'XXX'], 
			'11B': ['XXX', '11Z'], 
			'11Z': ['11B', 'XXX'], 
			'22A': ['22B', 'XXX'], 
			'22B': ['22C', '22C'], 
			'22C': ['22Z', '22Z'], 
			'22Z': ['22B', '22B'], 
			'XXX': ['XXX', 'XXX']}) == 6)


