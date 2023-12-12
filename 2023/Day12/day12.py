
# https://adventofcode.com/2023/day/12

import sys

def memo(f):
	mem = {}
	def m(status, record, strike=0):
		k = (status, tuple(record), strike)
		if k not in mem:
			mem[k] = f(status, record, strike)
		return mem[k]
	return m

@memo
def count_options(status, record, strike=0):
	if strike and len(record) == 0:
		return 0
	# end of status
	if len(status) == 0:
		if strike == 0 and len(record) == 0: return 1
		if [strike] == record: return 1
		return 0

	curr = status[0]
	if curr == '.':
		if strike:
			if strike != record[0]:
				return 0
			return count_options(status[1:], record[1:], 0)
		return count_options(status[1:], record, 0)

	if curr == '#':
		return count_options(status[1:], record, strike + 1)

	# curr == '?'
	total = 0
	# treat as #
	total += count_options('#' + status[1:], record, strike)
	# treat as .
	total += count_options('.' + status[1:], record, strike)
	return total

def solve(arr):
	res = 0
	for status, record in arr:
		tmp = count_options(status, record)
		res += count_options(status, record)
	return res

# print(solve([('???.###', [1, 1, 3]), 
# 			 ('.??..??...?##.', [1, 1, 3]), 
# 			 ('?#?#?#?#?#?#?#?', [1, 3, 1, 6]), 
# 			 ('????.#...#...', [4, 1, 1]), 
# 			 ('????.######..#####.', [1, 6, 5]), 
# 			 ('?###????????', [3, 2, 1])]))

########################
##### -- part 1 -- ##### 
########################
if __name__ == '__main__':
	arr = []
	for line in sys.stdin:
		status, record = line.strip('\n').split(' ')
		arr.append((status, list(map(int, record.split(',')))))
	print(solve(arr))


########################
##### -- part 2 -- ##### 
########################
if __name__ == '__main__':
	arr = []
	for line in sys.stdin:
		status, record = line.strip('\n').split(' ')
		status = '?'.join([status] * 5)
		record = list(map(int, record.split(','))) * 5
		arr.append((status, record))
	print(solve(arr))
