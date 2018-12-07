# https://adventofcode.com/2018/day/4

import sys
from collections import defaultdict

def find_most_common_min(array):
	count = [0] * 60
	for start, end in array:
		for i in range(start, end):
			count[i] += 1
	return count.index(max(count))
	

def solve(timeline):
	user_sleeptime = defaultdict(list)
	user_total_sleeptime = defaultdict(int)
	user = 0
	start = 0
	for year, month, day, hour, minute, log in timeline:
		if type(log) == int:
			user = log
		elif log == 'falls asleep':
			start = minute
		else:
			end = minute
			user_sleeptime[user].append((start, end))
			user_total_sleeptime[user] += end - start

	tmp = 0
	for k, v in user_total_sleeptime.items():
		if v > tmp:
			user = k
			tmp = v
	return find_most_common_min(user_sleeptime[user]) * user


if __name__ == '__main__':
	timeline = []
	for line in sys.stdin:
		times, log = line.strip('\n').split('] ')
		date, time = times[1:].split(' ')
		year, month, day = date.split('-')
		hour, minute = time.split(':')
		if log.startswith('Guard'):
			log = int(log.split(' ')[1][1:])
		year, month, day, hour, minute = map(int, [year, month, day, hour, minute])
		timeline.append([year, month, day, hour, minute, log])
	timeline.sort()
	print solve(timeline)



