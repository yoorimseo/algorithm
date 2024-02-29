import sys

input = sys.stdin.readline

N = int(input())
budget = list(map(int, input().split()))
M = int(input())

start = 1
end = max(budget)

while start <= end:
    mid = (start + end) // 2
    total = 0

    for b in budget:
        if b < mid:
            total += b
        else:
            total += mid

    if total <= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)