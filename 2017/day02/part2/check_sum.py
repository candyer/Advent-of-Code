# http://adventofcode.com/2017/day/2

# the goal is to find the only two numbers in each row where one evenly divides 
# the other - that is, where the result of the division operation is a whole number. 
# They would like you to find those numbers on each line, divide them, and add up 
# each line's result.

# For example, given the following spreadsheet:

# 5 9 2 8
# 9 4 7 3
# 3 8 6 5
# In the first row, the only two numbers that evenly divide are 8 and 2; the result 
# of this division is 4.
# In the second row, the two numbers are 9 and 3; the result is 3.
# In the third row, the result is 2.
# In this example, the sum of the results would be 4 + 3 + 2 = 9.

# What is the sum of each row's result in your puzzle input?


import sys

def find_divisible_pair(array):
	n = len(array)
	for i in range(n):
		for j in range(n - 1, -1, -1):
			if array[i] / array[j] < 2:
				break
			if array[i] % array[j] == 0:
				return array[i] / array[j]

def check_sum(grid):
	row = len(grid)
	res = 0
	for r in range(row):
		res += find_divisible_pair(grid[r])
	return res

if __name__ == '__main__':
	spreadsheet = []
	for line in sys.stdin:
		tmp = map(int, line.split())
		tmp.sort(reverse=True)
		spreadsheet.append(tmp)
	print check_sum(spreadsheet)

# spreadsheet = [
# [5735, 5280, 5058, 5048, 4504, 4362, 3805, 1809, 1794, 1521, 1088, 772, 230, 220, 178, 177], 
# [7464, 6870, 6629, 6539, 5961, 5706, 4638, 4473, 4173, 4140, 3839, 387, 271, 258, 229, 185], 
# [5854, 5340, 5250, 5149, 4601, 3995, 3955, 3916, 2892, 2497, 2000, 1110, 256, 249, 210, 184], 
# [609, 608, 550, 545, 495, 468, 439, 385, 319, 188, 182, 165, 153, 144, 142, 126], 
# [1261, 1222, 1123, 1098, 1001, 942, 665, 567, 286, 227, 139, 128, 122, 107, 104, 69], 
# [2287, 2217, 1998, 1728, 1522, 1496, 1362, 1355, 1148, 1138, 918, 202, 111, 109, 91, 90], 
# [489, 431, 426, 386, 372, 369, 348, 344, 242, 226, 153, 133, 124, 120, 112, 67], 
# [3409, 3168, 3086, 2998, 2490, 1574, 1002, 990, 749, 588, 265, 163, 154, 151, 144, 133], 
# [4098, 3855, 3648, 3550, 3071, 2692, 2269, 1630, 966, 760, 468, 329, 215, 192, 173, 162], 
# [5912, 5616, 5551, 5514, 4884, 4862, 4226, 3700, 1984, 1839, 586, 300, 239, 216, 169, 163], 
# [3257, 3199, 2982, 2864, 2775, 2685, 2062, 1749, 1319, 1221, 1045, 213, 211, 198, 194, 156], 
# [1299, 1157, 1125, 1025, 998, 977, 919, 809, 478, 273, 198, 103, 94, 89, 85, 69], 
# [7451, 7104, 7070, 6989, 6672, 6290, 6041, 5071, 4782, 2901, 2025, 1965, 230, 215, 207, 192], 
# [2315, 2292, 2072, 1944, 1878, 1446, 1417, 1379, 1261, 1053, 689, 641, 91, 86, 77, 74], 
# [5391, 5021, 4712, 4362, 4326, 3734, 3538, 2529, 2178, 1953, 1579, 794, 306, 296, 261, 248], 
# [4431, 4392, 4289, 3972, 2426, 2396, 2336, 2157, 1902, 1764, 854, 288, 244, 229, 216, 192]
# ]

# example = [
# 	[9, 8, 5, 2],
# 	[9, 7, 4, 3],
# 	[8, 6, 5, 3],
# ]

# print check_sum(spreadsheet) == 308
# print check_sum(example)# == 9

