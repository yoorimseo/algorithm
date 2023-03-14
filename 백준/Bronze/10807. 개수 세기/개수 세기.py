import sys

num = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))
find = int(sys.stdin.readline().strip())
res = list(filter(lambda n: n == find, arr))

print(len(res))