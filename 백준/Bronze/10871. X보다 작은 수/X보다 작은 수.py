import sys

N, X = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
res = list(filter(lambda n: n < X, arr))

print(*res)