# https://adventofcode.com/2017/day/18

import sys

def isInt(s):
	return s.lstrip("-").isdigit()

def f(s, d):
	if isInt(s):
		return int(s)
	else:
		if s not in d: 
			d[s] = 0
		return d[s]	

def solve1(instructions):
	n = len(instructions)
	d = {}
	sount = 0
	i = 0
	
	while i < n:
		if instructions[i][0] != 'snd' and instructions[i][0] != 'rcv':
			cmd, letter, val = instructions[i]
			if cmd == 'set':
				d[letter] = f(val, d)
				i += 1
			elif cmd == 'add':			
				d[letter] = f(letter, d) + f(val, d)
				i += 1
			elif cmd == 'mul':
				d[letter] = f(letter, d) * f(val, d)
				i += 1
			elif cmd == 'mod':
				d[letter] = f(letter, d) % f(val, d)
				i += 1
			elif cmd == 'jgz':
				if f(letter, d) > 0:
					i += f(val, d)
				else:
					i += 1
		else:
			cmd, letter = instructions[i]
			if cmd == 'snd':
				sound = f(letter, d)
				i += 1
			elif cmd == 'rcv':
				if f(letter, d) > 0:
					d[letter] = sound
					break
	return sound
	
if __name__ == '__main__':
	instructions = []
	for line in sys.stdin.readlines():
		instructions.append(line.split())
	print 'part 1 result: {}'.format(solve1(instructions))

# print solve([
# 	['set', 'i', '31'], 
# 	['set', 'a', '1'], 
# 	['mul', 'p', '17'], 
# 	['jgz', 'p', 'p'], 
# 	['mul', 'a', '2'], 
# 	['add', 'i', '-1'], 
# 	['jgz', 'i', '-2'], 
# 	['add', 'a', '-1'], 
# 	['set', 'i', '127'], 
# 	['set', 'p', '952'], 
# 	['mul', 'p', '8505'], 
# 	['mod', 'p', 'a'], 
# 	['mul', 'p', '129749'], 
# 	['add', 'p', '12345'], 
# 	['mod', 'p', 'a'], 
# 	['set', 'b', 'p'], 
# 	['mod', 'b', '10000'], 
# 	['snd', 'b'], 
# 	['add', 'i', '-1'], 
# 	['jgz', 'i', '-9'], 
# 	['jgz', 'a', '3'], 
# 	['rcv', 'b'], 
# 	['jgz', 'b', '-1'], 
# 	['set', 'f', '0'], 
# 	['set', 'i', '126'], 
# 	['rcv', 'a'], 
# 	['rcv', 'b'], 
# 	['set', 'p', 'a'], 
# 	['mul', 'p', '-1'], 
# 	['add', 'p', 'b'], 
# 	['jgz', 'p', '4'], 
# 	['snd', 'a'], 
# 	['set', 'a', 'b'], 
# 	['jgz', '1', '3'], 
# 	['snd', 'b'], 
# 	['set', 'f', '1'], 
# 	['add', 'i', '-1'], 
# 	['jgz', 'i', '-11'], 
# 	['snd', 'a'], 
# 	['jgz', 'f', '-16'], 
# 	['jgz', 'a', '-19']]) #4601
