
import sys
from collections import defaultdict

def find_most_common_min(array):
	count = [0] * 60
	for start, end in array:
		for i in range(start, end):
			count[i] += 1
	maxi = max(count)
	return maxi, count.index(maxi)
	

def solve(timeline):
	user_sleeptime = defaultdict(list)
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

	maxi_count = minute = 0
	
	for k, v in user_sleeptime.items():
		maxi, pos = find_most_common_min(v)
		if maxi > maxi_count:
			maxi_count = maxi
			minute = pos
			user = k
	return user * minute


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



