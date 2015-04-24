#! /bin/env python3

if __name__ == '__main__':
	n = int(input())
	sums = [0,0,0,0,0,0,0]
	for i in range(n):
		sums[i % 7] += int(input())
	for s in sums:
		print(s)