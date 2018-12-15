

import sys


def solve(pattern):
	m = len(pattern)
	recipes = [3, 7]
	elf_1, elf_2 = 0, 1
	n = 2
	while True:
		digit_sum = recipes[elf_1] + recipes[elf_2]
		tmp = map(int, str(digit_sum))
		for recipe in tmp:
			recipes.append(recipe)
			n += 1
			if recipes[-m:] == pattern:
				return n - m
		elf_1 = (elf_1 + recipes[elf_1] + 1) % n
		elf_2 = (elf_2 + recipes[elf_2] + 1) % n


if __name__ == '__main__':
	pattern = map(int, sys.stdin.readline())
	print solve(pattern)


assert solve([0, 1, 2, 4, 5]) == 5
assert solve([5, 1, 5, 8, 9]) == 9
assert solve([9, 2, 5, 1, 0]) == 18
assert solve([3, 0, 6, 2, 8, 1]) == 20298300


