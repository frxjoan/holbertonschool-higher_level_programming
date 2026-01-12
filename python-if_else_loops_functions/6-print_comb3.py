#!/usr/bin/python3
for i in range(9):
	for j in range(10):
		if (i != j):
			if (j > i):
				if (i == 0 and j == 1):
					print("01", end = "")
				else:
					print(", {}{}".format(i, j), end = "")
