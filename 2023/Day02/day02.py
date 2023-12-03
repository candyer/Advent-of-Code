
# https://adventofcode.com/2023/day/2

import sys
from collections import defaultdict

def solve(arr):
	total = 0
	if arr[-1] == '\n': arr = arr[:-1]
	d = defaultdict(int)
	for games in arr.split('; '):
		for game in games.split(", "):
			num, color = game.split(' ')
			if int(num) > d[color]:
				d[color] = int(num)
	return d

########################
##### -- part 1 -- #####
########################
if __name__ == '__main__':
	total = 0
	red, green, blue = 12, 13, 14
	for line in sys.stdin:
		game_id, games = line.split(": ")
		i = int(game_id.split(" ")[-1])
		d = solve(games)
		if d["red"] <= red and d["green"] <= green and d["blue"] <= blue:
			total += int(i)
	print(total) #2720


########################
##### -- part 2 -- #####
########################
if __name__ == '__main__':
	total = 0
	for line in sys.stdin:
		game_id, games = line.split(": ")
		i = int(game_id.split(" ")[-1])
		d = solve(games)
		total += d['green'] * d['red'] * d['blue']
	print(total) #71535
	

