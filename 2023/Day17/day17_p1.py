
# https://adventofcode.com/2023/day/17

######################
### -- part 1 -- #####
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

	q = [(-grid[0][0], (0, 0), RIGHT, 3)]
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

		# move forward
		if steps_left:
			dr, dc = momentum
			next_pos = (r + dr, c + dc)
			heappush(q, (score, next_pos, momentum, steps_left - 1))

		# turn
		for next_momentum in move[momentum]:
			dr, dc = next_momentum
			next_pos = (r + dr, c + dc)
			heappush(q, (score, next_pos, next_momentum, 2))

	return flattened_scores[(rows - 1, cols - 1)]

if __name__ == '__main__':
	grid = []
	for line in sys.stdin:
		grid.append(list(map(int, line.strip('\n'))))
	print(solve(grid)) #956

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
	]) == 102)
###########################################################
  #  0   4   5   8  14  17  23  27  29  32  38  40  46
  #  3   5   6  11  15  20  25  30  32  37  43  42  45
  #  6   7  11  16  17  21  26  32  37  41  43  47  49
  #  9  11  15  21  22  29  31  39  41  46  47  52  51
  # 17  16  19  25  28  33  38  46  48  53  52  55  57
  # 18  21  22  30  34  42  46  53  58  61  56  60  63
  # 23  26  27  34  42  49  54  62  66  68  66  66  70
  # 28  32  31  38  46  53  61  70  76  79  75  71  73
  # 33  38  37  41  50  56  64  75  83  86  85  80  80
  # 41  44  45  45  51  58  67  81  89  94  89  89  84
  # 44  46  48  49  55  63  69  79  86  92  94  93  87
  # 49  51  52  55  60  64  72  80  91  99 103  96  98
  # 53  54  54  56  62  69  75  81  86  92 101  99 102
###########################################################
