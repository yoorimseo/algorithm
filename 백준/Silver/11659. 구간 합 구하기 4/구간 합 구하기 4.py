import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
arr = [0]
temp = 0

for n in num:
    temp += n
    arr.append(temp)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    res = arr[j] - arr[i-1]
    print(res)