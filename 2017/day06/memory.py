# http://adventofcode.com/2017/day/6

def solve1(array):
	n = len(array)
	seen = []
	res = 0
	x = 0
	while array not in seen:
		seen.append(array[:])
		res += 1
		maxi = max(array)
		idx = array.index(maxi)
		array[idx] = 0
		for i in range(maxi):
			idx += 1
			array[idx % n] += 1
	return res

def solve2(array):
	n = len(array)
	seen = []
	res = 0
	x = 0
	while array not in seen:
		seen.append(array[:])
		res += 1
		maxi = max(array)
		idx = array.index(maxi)
		array[idx] = 0
		for i in range(maxi):
			idx += 1
			array[idx % n] += 1
	return res - seen.index(array)


print solve1([0,2,7,0]) == 5
print solve1([4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]) == 6681

print solve2([0,2,7,0]) == 4
print solve2([4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]) ==2392

