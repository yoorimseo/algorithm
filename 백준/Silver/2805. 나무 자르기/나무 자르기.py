N, M = map(int, input().split())
heights = sorted(list(map(int, input().split())))
start, end = 1, max(heights)

while start <= end:
    mid = (start + end) // 2
    res = 0

    for h in heights:
        if h >= mid:
            res += h - mid

    if res >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)