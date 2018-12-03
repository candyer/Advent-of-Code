# https://adventofcode.com/2017/day/25

def generate(state, pos, d):
		blueprints = {
			'a': [(1,  1,  'b'), (0,  1,  'f')],
			'b': [(0, -1,  'b'), (1, -1,  'c')],
			'c': [(1, -1,  'd'), (0,  1,  'c')],
			'd': [(1, -1,  'e'), (1,  1,  'a')],
			'e': [(1, -1,  'f'), (0, -1,  'd')],
			'f': [(1,  1,  'a'), (0, -1,  'e')]
		}
		val, direction, new_state = blueprints[state][d.get(pos, 0)]
		d[pos] = val
		return new_state, pos + direction

def solve1():
	state = 'a'
	pos = 0
	d = {}
	for i in range(12425180):
		state, pos = generate(state, pos, d)
	return sum(d.values())

print solve1()






