import sys

def solve(s: str) -> int:
	row, col = 6, 25
	len_layer = row * col
	i = 0
	count = len_layer
	tmp = ['2'] * len_layer
	while i < len(s):
		if tmp[i % len_layer] == '2' and s[i] != '2':
			tmp[i % len_layer] = s[i]
		i += 1

	tmp = ''.join(tmp)
	image = []
	for j in range(0, len_layer, col):
		line = tmp[j:j + col].replace('0', '___').replace('1', '@@@')
		image.append(line)
	return '\n'.join(image)


if __name__ == '__main__':
	for line in sys.stdin:
		print(solve(line))
