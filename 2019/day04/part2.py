#####################
#### brute force ####
#####################
def is_password(num: int) -> bool:
	'''
	the problem description is a bit confusing, find if there is an adjacent duplicate with length exactly 2!
	for example 
		- '122233366' meet the criteria because of '66';
		- '123333333558' meet the criteria because of '55';
		- '11122233333' does not meet the criteria because none of these '111', '222', '33333' have length 2!
	'''
	s = str(num)
	n = len(s)
	any_adjacent_duplicate_exact_twice = False
	blocks = []
	s += '*'
	count = 1
	for i in range(n):
		if s[i] == s[i + 1]:
			count += 1
		else:
			if count == 2:
				any_adjacent_duplicate_exact_twice = True
			blocks.append(count)
			count = 1
	non_decrease = all(s[i] <= s[i + 1] for i in range(n - 1))
	return any_adjacent_duplicate_exact_twice and non_decrease

assert(is_password(123444) == False)
assert(is_password(111122) == True)
assert(is_password(1222233888888888) == True)
assert(is_password(111122444) == True)

def solve(start: int, end: int) -> int:
	count = 0
	for num in range(start, end + 1):
		if is_password(num):
			count += 1
	return count

assert(solve(372037, 905157) == 299)
