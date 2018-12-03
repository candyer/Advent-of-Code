# https://adventofcode.com/2017/day/17

def solve1(step):
	state = [0]
	curr = 0
	count = 1
	for i in range(2017):
		curr = (curr + step) % count + 1
		state.insert(curr, i + 1)
		count += 1
	idx = state.index(2017)
	return state[idx + 1]

def solve2(step):
    curr = 0
    count = 1
    res = 0
    for i in range(50000000):
        curr = (curr + step) % count + 1
        if curr == 1:
            res = i + 1
        count += 1
    return res

print solve1(348) == 417
print solve2(348) == 34334221
