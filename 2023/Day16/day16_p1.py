
# https://adventofcode.com/2023/day/16

######################
### -- part 1 -- #####
######################

import sys

UP    = (-1,  0)
DOWN  = ( 1,  0)
LEFT  = ( 0, -1)
RIGHT = ( 0,  1)

move = {
    UP: {
        '|':  (UP,),
        '-':  (LEFT, RIGHT,),
        '/':  (RIGHT,),
        '\\': (LEFT,),
        '.':  (UP,),
    },
    DOWN: {
        '|':  (DOWN,),
        '-':  (LEFT, RIGHT,),
        '/':  (LEFT,),
        '\\': (RIGHT,),
        '.':  (DOWN,),
    },
    LEFT: {
        '|':  (UP, DOWN,),
        '-':  (LEFT,),
        '/':  (DOWN,),
        '\\': (UP,),
        '.':  (LEFT,),
    },
    RIGHT: {
        '|':  (UP, DOWN,),
        '-':  (RIGHT,),
        '/':  (UP,),
        '\\': (DOWN,),
        '.':  (RIGHT,),
    }
}

def next_pos(sign, pos, direction):
	''' came from pos, and direction, return next pos and direction '''
	res = []
	for next_dir in move[direction][sign]:
		new_pos = (pos[0] + next_dir[0], pos[1] + next_dir[1])
		res.append((new_pos, next_dir))
	return res

def solve(grid):
	seen = set()
	seen_pos = set()
	queue = [((0, 0), RIGHT)]
	while queue:
		key = queue.pop()
		pos, dirc = key
		if key in seen:
			continue
		x, y = pos
		if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
			continue
		seen.add(key)
		seen_pos.add(pos)
		queue.extend(next_pos(grid[x][y], pos, dirc))
	return len(seen_pos)
	
assert(solve(['.|...\\....', 
			 '|.-.\\.....', 
			 '.....|-...', 
			 '........|.', 
			 '..........', 
			 '.........\\', 
			 '..../.\\\\..', 
			 '.-.-/..|..', 
			 '.|....-|.\\', 
			 '..//.|....']) == 46)


if __name__ == '__main__':
	grid = []
	for line in sys.stdin:
		grid.append(line.strip('\n'))
	print(solve(grid))  #6906
