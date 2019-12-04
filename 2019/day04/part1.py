#####################
#### brute force ####
#####################
def is_password(num: int) -> bool :
	s = str(num)
	n = len(s)
	adjacent_double = any(s[i] == s[i + 1] for i in range(n - 1))
	non_decrease = all(s[i] <= s[i + 1] for i in range(n - 1))
	return adjacent_double and non_decrease

def solve(start: int, end: int) -> int:
	count = 0
	for num in range(start, end + 1):
		if is_password(num):
			count += 1
	return count

assert(solve(372037, 905157) == 481)


