
# https://adventofcode.com/2023/day/4

import sys

########################
##### -- part 1 -- #####
########################

def solve(winning_nums, nums_i_have):
	res = 0
	for num in winning_nums:
		if num and num in nums_i_have:
			res += 1
	if res :
		return pow(2, res - 1)
	return 0

if __name__ == '__main__':
	total = 0
	scratchcards = []
	for line in sys.stdin:
		card_id, numbers = line.split(": ")
		winning_nums, nums_i_have = numbers.strip('\n').split(" | ")
		total += solve(winning_nums.split(" "), set(nums_i_have.split(" ")))
	print(total) #24848


########################
##### -- part 2 -- #####
########################

def find_matches(winning_nums, nums_i_have):
	match = 0
	for num in winning_nums:
		if num and num in nums_i_have:
			match += 1
	return match

def solve(matches):
	scratchcards = [1] * len(matches)
	for i, match in enumerate(matches):
		if match:
			for j in range(i + 1, i + match + 1):
				scratchcards[j] += scratchcards[i]
	return sum(scratchcards)

if __name__ == '__main__':
	matches = []
	for i, line in enumerate(sys.stdin):
		card_id, numbers = line.split(": ")
		winning_nums, nums_i_have = numbers.strip('\n').split(" | ")
		matches.append(find_matches(winning_nums.split(" "), set(nums_i_have.split(" "))))
	print(solve(matches)) #7258152


