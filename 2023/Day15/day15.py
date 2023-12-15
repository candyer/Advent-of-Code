
# https://adventofcode.com/2023/day/15

######################
### -- part 1 -- #####
######################

import sys

def hash(s):
	val = 0
	for c in s:
		val += ord(c)
		val *= 17
		val %= 256
	return val

def solve(strings):
	total = 0
	for s in strings:
		total += hash(s)
	return total

assert(solve(['rn=1', 'cm-', 'qp=3', 'cm=2', 'qp-', 'pc=4', 'ot=9', 'ab=5', 'pc-', 'pc=6', 'ot=7']) == 1320)

if __name__ == '__main__':
	strings = sys.stdin.readline().split(',')
	print(solve(strings))


#######################
#### -- part 2A -- #### handle two cases: '=' and '-'
#######################

import sys

def hash(s):
	val = 0
	for c in s:
		val += ord(c)
		val *= 17
		val %= 256
	return val

def solve(strings):
	boxes = [[] for _ in range(256)]
	for s in strings:
		if '=' in s:
			c, focal_length = s.split('=')
			focal_length = int(focal_length)
			box = hash(c)
			flag = True
			for i in range(len(boxes[box])):
				cc, val = boxes[box][i]
				if cc == c:
					boxes[box][i] = [c, focal_length]
					flag = False
					break
			if flag:
				boxes[box].append([c, focal_length])
		else: #'-' in s:
			c = s[:-1]
			box = hash(c)
			for i in range(len(boxes[box])):
				cc, val = boxes[box][i]
				if cc == c:
					boxes[box].pop(i)
					break
	total = 0
	for i, box in enumerate(boxes):
		for j, (ccc, val) in enumerate(box):
			total += (i + 1) * (j + 1) * val
	return total

assert(solve(['rn=1', 'cm-', 'qp=3', 'cm=2', 'qp-', 'pc=4', 'ot=9', 'ab=5', 'pc-', 'pc=6', 'ot=7'])==145)

if __name__ == '__main__':
	strings = sys.stdin.readline().split(',')
	print(solve(strings))


#######################
#### -- part 2B -- #### only handle '-' case
#######################

import sys

def hash(s):
	val = 0
	for c in s:
		val += ord(c)
		val *= 17
		val %= 256
	return val

def solve(strings):
	boxes = [[] for _ in range(256)]
	for s in strings:		
		c, focal_length = s.split('=')
		focal_length = int(focal_length)
		box = hash(c)
		flag = True
		for i in range(len(boxes[box])):
			cc, val = boxes[box][i]
			if cc == c:
				boxes[box][i] = [c, focal_length]
				flag = False
				break
		if flag:
			boxes[box].append([c, focal_length])

	total = 0
	for i, box in enumerate(boxes):
		for j, (_, val) in enumerate(box):
			total += (i + 1) * (j + 1) * val
	return total

def preprocess_input(strings):
	''' 
	get rid of all the '-' instructions, so we only need to handle one case
	''' 
	to_remove = set()
	arr = []
	for s in strings[::-1]:
		if '-' in s:
			to_remove.add(s[:-1])
		if '=' in s:
			identifier = s.split('=')[0]
			if identifier not in to_remove:
				arr.append(s)
	return arr[::-1]

if __name__ == '__main__':
	strings = sys.stdin.readline().split(',')
	print(solve(preprocess_input(strings)))
