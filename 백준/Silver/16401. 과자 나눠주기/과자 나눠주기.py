import sys

M, N = map(int, sys.stdin.readline().split())
snacks = list(map(int, sys.stdin.readline().split()))
start, end = 1, int(1e9)
res = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for s in snacks:
        cnt += s // mid

    if cnt >= M:
        res = max(res, mid)
        start = mid + 1
    else:
        end = mid - 1

print(res)