#!/usr/bin/env python3
import sys

result = 0
if __name__ == "__main__":
    argc = len(sys.argv) - 1

for i in range(argc):
    result += int(sys.argv[i + 1])
print("{}".format(result))
