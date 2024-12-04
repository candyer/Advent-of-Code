
# https://adventofcode.com/2024/day/4
# --- Day 4: Ceres Search ---

########################
##### -- part 1 -- #####
########################

import sys

def solve(matrix):
	total = 0
	rows, cols = len(matrix), len(matrix[0])
	for row in range(3, rows - 3):
		for col in range(3, cols - 3):
			if matrix[row][col] == 'X':

				# horizontal
				total += matrix[row][col - 3:col + 1] == ['S', 'A', 'M', 'X']
				total += matrix[row][col:col + 4] == ['X', 'M', 'A', 'S']

				# vertical
				tmp = []
				for r in range(row - 3, row + 1):
					tmp.append(matrix[r][col])
					total += tmp == ['S', 'A', 'M', 'X']
				tmp = []
				for r in range(row, row + 4):
					tmp.append(matrix[r][col])
					total += tmp == ['X', 'M', 'A', 'S']

				# diagonal
				for r, c in [[-1, -1], [-1, 1], [1, -1], [1, 1]]:
					tmp, x, y = [], row, col
					for _ in range(4):
						tmp.append(matrix[x][y])
						x += r
						y += c
					total += tmp == ['X', 'M', 'A', 'S']

	return total
    

if __name__ == "__main__":
	matrix = []
	for line in sys.stdin:
		row = ["."] * 4 + list(line.strip("\n")) + ["."] * 4 #add paddings
		matrix.append(row)
	n = len(matrix[0])
	matrix = [["."] * n] * 4 + matrix + [["."] * n] * 4 #add paddings
	print(solve(matrix))

