import sys

def solve(s: str) -> int:
	row, col = 25, 6
	len_layer = row * col
	
	min_0 = float('inf')
	res = 0
	i = 0
	while i < len(s):
		tmp = s[i: i + len_layer]
		count_0 = tmp.count('0')
		if count_0 < min_0:
			min_0 = count_0
			res = tmp.count('1') * tmp.count('2')	
		i += len_layer
	return res

if __name__ == '__main__':
	for line in sys.stdin:
		print(solve(line))