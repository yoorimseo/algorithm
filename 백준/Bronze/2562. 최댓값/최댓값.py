import sys

lines = sys.stdin.readlines()
arr = []

for line in lines:
  arr.append(int(line))

print(max(arr), arr.index(max(arr)) + 1, sep='\n')