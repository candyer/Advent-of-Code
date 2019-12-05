import sys
from typing import List, Tuple

def breakDown(num: int) -> Tuple[int, List[int]]:
	modes = list(map(int, str(num)[:-2][::-1]))
	modes.extend([0] * (2 - len(modes)))
	return (num % 100, modes)

def solve(arr: List[int], input_instruction: int) -> int:
	diagnostic_code = 0
	i = 0
	while True:
		opcode, modes = breakDown(arr[i])
		if opcode == 99:
			return diagnostic_code

		a = i + 1 if modes[0] else arr[i + 1] #parameter 1
		b = i + 2 if modes[1] else arr[i + 2] #parameter 2
		c = arr[i + 3] #action on this position
		
		if opcode == 1:
			arr[c] = arr[a] + arr[b]
			i += 4

		elif opcode == 2:
			arr[c] = arr[a] * arr[b]
			i += 4

		elif opcode == 3:
			arr[a] = input_instruction
			i += 2

		elif opcode == 4:
			diagnostic_code = arr[a]
			i += 2

if __name__ == '__main__':
	for line in sys.stdin:
		arr = list(map(int, line.split(',')))
		input_instruction = 1
		print(solve(arr, input_instruction))


