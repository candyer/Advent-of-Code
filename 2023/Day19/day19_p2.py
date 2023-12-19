
# https://adventofcode.com/2023/day/19

######################
### -- part 2 -- #####
######################

import sys
import operator

def value2count(value):
	total = 1
	for start, end in value.values():
		interval = max(0, (end - start - 1))
		total *= interval
	return total

assert value2count({
		'x': (0, 4001),
		'm': (0, 4001),
		'a': (0, 4001),
		's': (0, 4001),
	}) == 4000**4

assert value2count({
		'x': (3000, 2000),
		'm': (0, 4001),
		'a': (0, 4001),
		's': (0, 4001),
	}) == 0

def solve(cmds):
	first_value = {
		'x': (0, 4001),
		'm': (0, 4001),
		'a': (0, 4001),
		's': (0, 4001),
	}

	def rec(cmd, value):
		if cmd == 'R': return 0
		if cmd == 'A': return value2count(value)
		total = 0
		for updater, otherwise, command in cmds[cmd]:
			total += rec(command, updater(value))
			value = otherwise(value)
		return total
	return rec('in', first_value)

def cond2lambda(cond):
	var = cond[0]
	ind = 1 if cond[1] == '<' else 0
	op = min if cond[1] == '<' else max
	val = int(cond[2:])
	def f(value): # update value if choose this branch
		copy = dict(value)
		x = list(copy[var])
		x[ind] = op(x[ind], val)
		copy[var] = tuple(x)
		return copy

	ind2 = 0 if cond[1] == '<' else 1
	op2 = max if cond[1] == '<' else min
	val2 = (val - 1) if cond[1] == '<' else (val + 1)
	def g(value): # update value if not choose this branch
		copy = dict(value)
		x = list(copy[var])
		x[ind2] = op2(x[ind2], val2)
		copy[var] = tuple(x)
		return copy

	return f, g

def main():
	cmds = {}
	for line in sys.stdin:
		if line == '\n':
			break
		name, line = line.split('{')
		line = line.split('}')[0]
		commands = line.split(',')
		cmds[name] = []
		for command in commands:
			if ':' not in command:
				cmds[name].append((lambda x: x, lambda x: x, command))
				continue
			cond, result = command.split(':')
			cmds[name].append((*cond2lambda(cond), result))
	return solve(cmds)

if __name__ == "__main__":
	print(main())  #130303473508222
