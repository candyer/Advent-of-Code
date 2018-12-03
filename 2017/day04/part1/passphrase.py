# http://adventofcode.com/2017/day/4

# A new system policy has been put in place that requires all accounts 
# to use a passphrase instead of simply a password. A passphrase consists 
# of a series of words (lowercase letters) separated by spaces.

# To ensure security, a valid passphrase must contain no duplicate words.

# For example:

# aa bb cc dd ee is valid.
# aa bb cc dd aa is not valid - the word aa appears more than once.
# aa bb cc dd aaa is valid - aa and aaa count as different words.
# The system's full passphrase list is available as your puzzle input. 
# How many passphrases are valid?



import sys

from collections import Counter as c
def is_valid(passphrases):
	d = c(passphrases)
	for i in d.values():
		if i > 1:
			return False
	return True

if __name__ == '__main__':
	res = 0
	for line in sys.stdin:
		passohrases = line.split()
		if is_valid(passohrases):
			res += 1
	print res


# print is_valid(['aa', 'bb', 'cc', 'dd', 'aaa']) == True
# print is_valid(['aytvvo', 'awm', 'ojaaigg', 'awm', 'dbfaokz']) == False

