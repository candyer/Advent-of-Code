

import sys


def solve(num):
	recipes = [3, 7]
	elf_1, elf_2 = 0, 1
	n = 2
	while True:
		digit_sum = recipes[elf_1] + recipes[elf_2]
		if digit_sum > 9:
			recipes.append(digit_sum / 10)
			recipes.append(digit_sum % 10)
			n += 2
		else:
			recipes.append(digit_sum)
			n += 1
		if n >= num + 10:
			return "".join(map(str, recipes[num : num + 10]))

		elf_1 = (elf_1 + recipes[elf_1] + 1) % n
		elf_2 = (elf_2 + recipes[elf_2] + 1) % n


assert solve(306281) == '3718110721'


if __name__ == '__main__':
	print solve(int(sys.stdin.readline()))



