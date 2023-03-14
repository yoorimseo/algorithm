import sys

num = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

print(min(arr), max(arr))