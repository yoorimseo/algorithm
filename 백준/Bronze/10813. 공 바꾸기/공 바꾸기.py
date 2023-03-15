import sys

N, M = map(int, sys.stdin.readline().strip().split())
arr = list(i for i in range(1, N + 1))

lines = sys.stdin.readlines()

for line in lines:
  i, j = map(int, line.strip().split())
  k = arr[i - 1]
  arr[i - 1] = arr[j - 1]
  arr[j - 1] = k

print(*arr)