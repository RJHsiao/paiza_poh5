#! /bin/env python3

if __name__ == '__main__':
	x,y = [int(i) for i in input().split()]
	table = [None] * y
	for i in range(y):
		table[i] = [int(i) for i in input().split()]
		for j in range(x):
			if table[i][j] != 1:
				table[i][j] = 0

	for j in range(x):
		count = 0
		for i in range(y):
			if table[i][j] == 1:
				count += 1
		for i in range(y - count):
			table[i][j] = 0
		for i in range(y - count, y):
			table[i][j] = 1

	for t in table:
		print(" ".join(str(x) for x in t))