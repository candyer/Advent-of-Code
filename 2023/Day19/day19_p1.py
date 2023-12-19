
# https://adventofcode.com/2023/day/19

######################
### -- part 1 -- #####
######################

import sys
import operator

def solve(cmds, values):
	total = 0
	for value in values:
		cmd = 'in'
		while True:
			if cmd == 'R':
				break
			if cmd == 'A':
				total += sum(value.values())
				break
			for pred, nxt in cmds[cmd]:
				if pred(value):
					cmd = nxt
					break
	return total

def cond2lambda(cond):
	var = cond[0]
	op = operator.lt if cond[1] == '<' else operator.gt
	val = int(cond[2:])
	def f(value):
		return op(value[var], val)
	return f

def main():
	cmds = {}
	values = []
	parse_cmds = True
	for line in sys.stdin:
		if line == '\n':
			parse_cmds = False
			continue
		if parse_cmds:
			name, line = line.split('{')
			line = line.split('}')[0]
			commands = line.split(',')
			cmds[name] = []
			for command in commands:
				if ':' not in command:
					cmds[name].append((lambda x: True, command))
					continue
				cond, result = command.split(':')
				cmds[name].append((cond2lambda(cond), result))
			continue
		line = line.split('{')[1].split('}')[0].split(',')
		value = {eq.split('=')[0]:int(eq.split('=')[1]) for eq in line}
		values.append(value)
	return solve(cmds, values)

if __name__ == "__main__":
	print(main()) #342650
