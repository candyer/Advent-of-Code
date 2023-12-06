
# https://adventofcode.com/2023/day/5

import sys

########################
##### -- part 1 -- #####
########################

def solve(arr, seeds):
	location = float('inf')
	for seed in seeds:
		for maps in arr:
			for des, source, rng in maps:
				if source <= seed < source + rng:
					seed = seed - source + des
					break
		location = min(location, seed)
	return location #331445006


########################
##### -- part 2 -- #####
########################

def find_interval(start, layer):
	for x, y, z in layer:
		if y <= start < y + z:
			return x, y, z

	# get rid of the edge cases
	closest = float('inf')
	for _, y, _ in layer:
		if y < start: continue
		if y > closest: continue
		closest = y
	return start, start, closest - start # make a fake identity range

def to_next(start, x, y):
	return x + start - y

def one_layer(seeds, layer):
	''' return new seeds for next layer'''
	results = []
	while seeds:
		seed = seeds.pop()
		start, end = seed
		x, y, z = find_interval(start, layer)
		if end >= y + z:
			new_start = y + z
			new_end = end
			seeds.append((new_start, new_end))
			end = y + z - 1

		results.append((to_next(start, x, y), to_next(end, x, y)))
	return results

def all_layers(seeds, layers):
	for layer in layers:
		seeds = one_layer(seeds, layer)
	return min(seeds)[0]	

def solve(arr, seeds):
	location = []
	n = len(seeds)
	pairs = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, n, 2)]
	return all_layers(pairs, arr) # 6472060

# print(one_layer([(79, 93)], [[50, 98, 2], [52, 50, 48]])) #[(81, 95)]
# print(one_layer([(79, 99)], [[50, 98, 2], [52, 50, 48]])) #[(81, 99), (50, 51)]

if __name__ == "__main__":
	arr = []
	tmp, seeds = sys.stdin.readline().strip('\n').split(": ")
	seeds = list(map(int, seeds.split(" ")))
	for line in sys.stdin:
		if line == '\n':
			arr.append([])
			continue
		if ':' in line:
			continue
		arr[-1].append(list(map(int, line.strip("\n").split(" "))))
	print(solve(arr, seeds))

# print(solve([
# 	[[50, 98, 2], [52, 50, 48]],
# 	[[0, 15, 37], [37, 52, 2], [39, 0, 15]],
# 	[[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]],
# 	[[88, 18, 7], [18, 25, 70]],
# 	[[45, 77, 23], [81, 45, 19], [68, 64, 13]],
# 	[[0, 69, 1], [1, 0, 69]],
# 	[[60, 56, 37], [56, 93, 4]]], [79, 14, 55, 13]))

