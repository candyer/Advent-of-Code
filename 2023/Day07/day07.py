
# https://adventofcode.com/2023/day/7

########################
##### -- part 1 -- ##### 
########################
# solution 1: convert TJQKA to ABCDE for sorting hands easily.

import sys
from collections import Counter as c
def check_type(hand):
	display = sorted(list(c(hand).values()))
	return [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [1, 1, 3], [2, 3], [1, 4], [5]].index(display)

def solve(hands):
	rank = [[] for i in range(7)]
	for hand in hands.keys():
		rank[check_type(hand)].append(hand)
	count = 1
	res = 0
	for i in range(7):
		rank[i].sort()
		for r in rank[i]:
			res += hands[r] * count
			count += 1
	return res #253205868

if __name__ == "__main__":
	hands = {}
	switch = {'T': 'A', 'J': 'B', "Q": 'C', 'K': 'D', 'A': 'E', '2': '2', '3': '3','4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
	for line in sys.stdin:
		hand, bid = line.strip("\n").split(" ")
		hand = ''.join([switch[chr] for chr in list(hand)])
		hands[hand] = int(bid)
	print(solve(hands))

########################
##### -- part 1 -- #####
########################
# solution 2: convert each hand(base_13) to a number(base_10), to sort the hands.

import sys
from collections import Counter as c

def base13_base10(hand):
	strength = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1, '2': 0}
	num = 0
	for c in hand:
		num *= 13
		num += strength[c]
	return num

def check_type(hand):
	display = sorted(list(c(hand).values()))
	return [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [1, 1, 3], [2, 3], [1, 4], [5]].index(display)

def solve(hands):
	rank = [[] for i in range(7)]
	for hand in hands.keys():
		rank[check_type(hand)].append(hand)
	count = 1
	res = 0
	for i in range(7):
		rank[i].sort(key=base13_base10)
		for r in rank[i]:
			res += hands[r] * count
			count += 1
	return res  #253205868

if __name__ == "__main__":
	hands = {}
	for line in sys.stdin:
		hand, bid = line.strip("\n").split(" ")
		hands[hand] = int(bid)
	print(solve(hands))



########################
##### -- part 2 -- ##### 
########################

import sys
from collections import Counter as c

def base13_to_base10(hand):
	strength = {'A': 12, 'K': 11, 'Q': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1, 'J': 0}
	num = 0
	for c in hand:
		num *= 13
		num += strength[c]
	return num

def check_type(hand):
	rep_J = hand.count("J")
	if rep_J == 5:
		return 6
	hand = hand.replace('J', '')
	display = list(sorted(list(c(hand).values())))
	display[-1] += rep_J
	return [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [1, 1, 3], [2, 3], [1, 4], [5]].index(display)

def solve(hands):
	rank = [[] for i in range(7)]
	for hand in hands.keys():
		rank[check_type(hand)].append(hand)
	count = 1
	res = 0
	for i in range(7):
		rank[i].sort(key=base13_to_base10)
		for r in rank[i]:
			res += hands[r] * count
			count += 1
	return res 

if __name__ == "__main__":
	hands = {}
	for line in sys.stdin:
		hand, bid = line.strip("\n").split(" ")
		hands[hand] = int(bid)
	print(solve(hands))  #253907829
