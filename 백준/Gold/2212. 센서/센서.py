import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
arr = sorted(list(map(int, input().split())))
res = []

for i in range(N-1):
    res.append(arr[i+1] - arr[i])

res.sort()

print(sum(res[:N-K]))