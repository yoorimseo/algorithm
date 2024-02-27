import sys

numA, numB = map(int, sys.stdin.readline().split())
A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))
res = A - B

if len(res):
    print(len(res))
    print(*sorted(list(res)))
else:
    print(0)