import sys
from typing import List

def f(arr: List[int]) -> int:
	n = len(arr)
	i = 0
	while i < n:
		opcode = arr[i]
		if opcode == 99:
			return arr
		else:
			if arr[i + 3] >= n:
				return False
			a, b = arr[arr[i + 1]], arr[arr[i + 2]]
			if opcode == 1:
				arr[arr[i + 3]] = a + b
			else:
				arr[arr[i + 3]] = a * b
			i += 4	
	return arr	

def solve(arr: List[int]) -> int:
	n = len(arr)
	for i in range(100):
		for j in range(100):
			arr1 = arr[:]
			arr1[1] = i
			arr1[2] = j
			x = f(arr1)
			if x:
				if x[0] == 19690720:
					return i * 100 + j

if __name__ == '__main__':
	for line in sys.stdin:
		arr = list(map(int, line.split(',')))
		print(solve(arr))