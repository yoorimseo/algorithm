import sys

N, M = map(int, sys.stdin.readline().strip().split())
arr = list(0 for _ in range(N))

lines = sys.stdin.readlines()

for line in lines:
  i, j, k = map(int, line.strip().split())
  for n in range(i, j + 1):
    arr[n-1] = k

print(*arr)