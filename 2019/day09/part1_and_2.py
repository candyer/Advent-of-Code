import sys
from typing import List, Tuple, Dict
from collections import defaultdict

def breakDown(num: int) -> Tuple[int, List[int]]:
	modes = list(map(int, str(num)[:-2][::-1]))
	modes.extend([0] * (3 - len(modes)))
	return (num % 100, modes)

def solve(d: Dict[int, int], inpt: int) -> int:
	relative_base = 0
	output = 0
	i = 0

	while True:
		opcode, modes = breakDown(d[i])
		if opcode == 99:
			return output

		a = i + 1 if modes[0] == 1 else d[i + 1] if modes[0] == 0 else d[i + 1] + relative_base
		b = i + 2 if modes[1] == 1 else d[i + 2] if modes[1] == 0 else d[i + 2] + relative_base
		c = d[i + 3] if modes[2] == 0 else d[i + 3] + relative_base

		############################################################
		if opcode == 1:
			d[c] = d[a] + d[b]
			i += 4

		elif opcode == 2:
			d[c] = d[a] * d[b]
			i += 4

		elif opcode == 3:
			d[a] = inpt
			i += 2

		elif opcode == 4:
			i += 2
			output = d[a]

		elif opcode == 5:
			if d[a]:
				i = d[b]
			else:
				i += 3

		elif opcode == 6:
			if d[a]:
				i += 3
			else:
				i = d[b]

		elif opcode == 7:
			if d[a] < d[b]:
				d[c] = 1
			else:
				d[c] = 0
			i += 4

		elif opcode == 8:
			if d[a] == d[b]:
				d[c] = 1
			else:
				d[c] = 0
			i += 4

		elif opcode == 9:
			relative_base += d[a]
			i += 2


if __name__ == '__main__':
	for line in sys.stdin:
		d = defaultdict(int)
		i = 0
		for num in map(int, line.split(',')):
			d[i] = num
			i += 1
		print('part1 result: {}'.format(solve(d, 1)))
		print('part2 result: {}'.format(solve(d, 2)))


