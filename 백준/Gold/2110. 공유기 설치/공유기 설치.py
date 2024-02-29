import sys

input = sys.stdin.readline

N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

start = 1
end = arr[-1] - arr[0]
res = 0

while start <= end:
    mid = (start + end) // 2
    curr = arr[0]
    cnt = 1

    for i in range(1, len(arr)):
        if arr[i] >= curr + mid:
            cnt += 1
            curr = arr[i]

    if cnt >= C:
        start = mid + 1
        res = mid
    else:
        end = mid - 1

print(res)