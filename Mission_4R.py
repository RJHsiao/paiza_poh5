#! /bin/env python3

if __name__ == '__main__':
	x,y,n = [int(i) for i in input().split()]
	table = [None] * y
	for i in range(y):
		table[i] = [int(i) for i in input().split()]

	s = 0
	for j in range(n):
		x1,y1,x2,y2 = [int(i) for i in input().split()]
		for ty in range(y1-1,y2):
			for tx in range(x1-1,x2):
				s += table[ty][tx]
				table[ty][tx] = 0

	print(s)