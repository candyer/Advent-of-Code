import sys
from typing import List

def solve(arr: List[int]) -> int:
	i = 0
	while i < len(arr):
		opcode = arr[i]
		if opcode == 99:
			return arr
		else:
			a, b = arr[arr[i + 1]], arr[arr[i + 2]]
			if opcode == 1:
				arr[arr[i + 3]] = a + b
			else:
				arr[arr[i + 3]] = a * b
			i += 4	
	return arr	

assert(solve([1,0,0,0,99]) == [2,0,0,0,99])
assert(solve([2,3,0,3,99]) == [2,3,0,6,99])
assert(solve([2,4,4,5,99,0]) == [2,4,4,5,99,9801])
assert(solve([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99])
assert(solve([1,9,10,3,2,3,11,0,99,30,40,50]) == [3500,9,10,70,2,3,11,0,99,30,40,50])

if __name__ == '__main__':
	for line in sys.stdin:
		arr = list(map(int, line.split(',')))
		arr[1] = 12
		arr[2] = 2
		print(solve(arr)[0])