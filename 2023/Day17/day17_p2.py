
# https://adventofcode.com/2023/day/17

######################
### -- part 2 -- #####
######################

import sys
from collections import defaultdict
from heapq import heappush, heappop

UP    = (-1,  0)
DOWN  = ( 1,  0)
LEFT  = ( 0, -1)
RIGHT = ( 0,  1)

move = {
    UP:    (LEFT, RIGHT,),
    DOWN:  (LEFT, RIGHT,),
    LEFT:  (UP,   DOWN,),
    RIGHT: (UP,   DOWN,),
}


def solve(grid):
	rows, cols = len(grid), len(grid[0])
	scores = defaultdict(lambda: float('inf'))
	flattened_scores = defaultdict(lambda: float('inf'))
	maxi = 10

	# def print_path():
	# 	for i in range(rows):
	# 		print(''.join([f'{flattened_scores[(i, j)]: 4}' for j in range(cols)]))

	q = [
		(-grid[0][0], (0, 0), RIGHT, maxi),
	 	(-grid[0][0], (0, 0), DOWN, maxi)
	]
	while q:
		score, pos, momentum, steps_left = heappop(q)
		r, c = pos
		if r < 0 or r >= rows or c < 0 or c >= cols:
			continue
		score += grid[r][c]
		key = (pos, momentum, steps_left)
		if score >= scores[key]:
			continue
		scores[key] = score
		flattened_scores[pos] = min(flattened_scores[pos], score)
		if pos == (rows - 1, cols - 1):
			continue

		# teleport forward
		if steps_left == maxi:
			dr, dc = momentum
			for i in range(3):
				steps_left -= 1
				r += dr
				c += dc
				if r < 0 or r >= rows or c < 0 or c >= cols:
					continue
				score += grid[r][c]
			next_pos = (r + dr, c + dc)
			heappush(q, (score, next_pos, momentum, steps_left - 1))
			continue
		# move forward
		if steps_left:
			dr, dc = momentum
			next_pos = (r + dr, c + dc)
			heappush(q, (score, next_pos, momentum, steps_left - 1))
		# turn
		for next_momentum in move[momentum]:
			heappush(q, (score - grid[r][c], pos, next_momentum, maxi))

	# print_path()
	return flattened_scores[(rows - 1, cols - 1)]

if __name__ == '__main__':
	grid = []
	for line in sys.stdin:
		grid.append(list(map(int, line.strip('\n'))))
	print(solve(grid)) #1106

assert(solve([[2, 4, 1, 3, 4, 3, 2, 3, 1, 1, 3, 2, 3],
			 [3, 2, 1, 5, 4, 5, 3, 5, 3, 5, 6, 2, 3],
			 [3, 2, 5, 5, 2, 4, 5, 6, 5, 4, 2, 5, 4],
			 [3, 4, 4, 6, 5, 8, 5, 8, 4, 5, 4, 5, 2],
			 [4, 5, 4, 6, 6, 5, 7, 8, 6, 7, 5, 3, 6],
			 [1, 4, 3, 8, 5, 9, 8, 7, 9, 8, 4, 5, 4],
			 [4, 4, 5, 7, 8, 7, 6, 9, 8, 7, 7, 6, 6],
			 [3, 6, 3, 7, 8, 7, 7, 9, 7, 9, 6, 5, 3],
			 [4, 6, 5, 4, 9, 6, 7, 9, 8, 6, 8, 8, 7],
			 [4, 5, 6, 4, 6, 7, 9, 9, 8, 6, 4, 5, 3],
			 [1, 2, 2, 4, 6, 8, 6, 8, 6, 5, 5, 6, 3],
			 [2, 5, 4, 6, 5, 4, 8, 8, 8, 7, 7, 3, 5],
			 [4, 3, 2, 2, 6, 7, 4, 6, 5, 5, 5, 3, 3],
	]) == 94)
###########################################################
  #  0  70  69  83  12  15  17  20  21  22  25  64  67
  # 62  77  84 102  51  65  71  85  67  72  78  80  83
  # 73  89  94 109  60  75  80  93  80  84  86  91  95
  # 81 100  99 124  69  81  85 100  94  99 103 108 104
  # 13  58  58  71  29  37  37  47  39  43  42  66  60
  # 14  66  70  84  34  43  45  54  48  51  46  78  69
  # 18  77  78  91  42  49  51  63  56  58  53  88  82
  # 21  84  83 101  45  52  58  68  63  67  59  94  86
  # 25  78  74  97  49  55  62  71  71  73  67  90  80
  # 29  83  80 101  50  57  66  75  79  79  71  95  83
  # 30  85  82 105  44  52  58  66  72  77  76 101  86
  # 67  90  86 111  71  77  89 102  99 106 104 104  91
  # 71  93  88 113  72  81  89 101  94  99 104 107  94
###########################################################

assert(solve([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
			 [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1], 
			 [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1], 
			 [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1], 
			 [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1]]) == 71)
###########################################################
 #   0 105 106 107   4   5   6   7   8   9  10 107
 # inf inf inf inf inf inf inf inf inf inf inf inf
 # inf inf inf inf inf inf inf inf inf inf inf inf
 # inf inf inf inf inf inf inf inf inf inf inf inf
 #  36  77  78  79  40  41  42  43  44  45  46  71
###########################################################


