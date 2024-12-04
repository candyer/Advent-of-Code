
# https://adventofcode.com/2024/day/3
# --- Day 3: Mull It Over ---

########################
##### -- part 1 -- #####
########################

import sys

def solve(line):
    res = 0
    for s in line.split("mul(")[1:]:
        ss = s.split(")", maxsplit = 1)[0].split(",")
        if len(ss) == 2:
            x , y = ss
            if x.isdigit() and y.isdigit():
                res += int(x) * int(y)
    return res

if __name__ == "__main__":
	total = 0
	for line in sys.stdin:
		total += solve(line.strip("\n"))
	print(total) #166630675
