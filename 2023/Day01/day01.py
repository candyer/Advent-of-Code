
# https://adventofcode.com/2023/day/1

########################
##### -- part 1 -- #####
########################

import sys

def solve(s):
	line_total = 0
	for c in s:
		if c.isdigit():
			line_total += int(c) * 10
			break
	for c in s[::-1]:
		if c.isdigit():
			line_total += int(c)
			break
	return line_total

if __name__ == '__main__':
	total = 0
	for line in sys.stdin:
		total += solve(line)
	print(total) #52974


########################
##### -- part 2 -- #####
########################

import sys

def solve(s):
	d = {"one": 1, "two": 2,  "three": 3,  "four": 4,  "five": 5,  
		 "six": 6,  "seven": 7,  "eight": 8,  "nine": 9,
		 "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
		 "7": 7, "8": 8, "9": 9 }
	left, right = {}, {}
	for digit in d.keys():
		l = s.find(digit)
		if l != -1: left[l] = digit
		r = s.rfind(digit)
		if r != -1:  right[r] = digit
	return d[min(left.items())[-1]] * 10 + d[max(right.items())[-1]]

if __name__ == '__main__':
	total = 0
	for line in sys.stdin:
		total += solve(line)
	print(total)  #53340


# print(solve('threexyztwone') == 31)
# print(solve('7pqrstsixteen7') == 77)
# print(solve('4nineeightseven2') == 42)
# print(solve('xtwone3four') == 24)





