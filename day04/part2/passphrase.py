# http://adventofcode.com/2017/day/4

# a valid passphrase must contain no two words that are anagrams of 
# each other - that is, a passphrase is invalid if any word's letters 
# can be rearranged to form any other word in the passphrase.

# For example:

# - abcde fghij is a valid passphrase.
# - abcde xyz ecdab is not valid - the letters from the third word can 
# 	be rearranged to form the first word.
# - a ab abc abd abf abj is a valid passphrase, because all letters need 
# 	to be used when forming another word.
# - iiii oiii ooii oooi oooo is valid.
# - oiii ioii iioi iiio is not valid - any of these words can be 
# 	rearranged to form any other word.
# Under this new system policy, how many passphrases are valid?


import sys

from collections import Counter as c
def is_valid(passphrases):
	for i in range(len(passphrases)):
		passphrases[i] = ''.join(sorted(passphrases[i]))
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


# print is_valid(['abcde', 'xyz', 'ecdab']) == False
# print is_valid(['aytvvo', 'awm', 'ojaaigg', 'dbfaokz']) == True

