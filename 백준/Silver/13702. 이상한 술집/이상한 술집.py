import sys
input = sys.stdin.readline

N, K = map(int, input().split())
kettles = [int(input()) for _ in range(N)]

start = 1
end = max(kettles)
res = 0

while start <= end:
    mid = (start + end) // 2
    total = sum(i // mid for i in kettles)

    if total >= K:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)