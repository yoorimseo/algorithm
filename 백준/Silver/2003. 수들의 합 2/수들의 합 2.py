N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
sum_arr = 0
cnt = 0

while True:
    if sum_arr >= M:
        sum_arr -= arr[start]
        start += 1
    else:
        if end == N:
            break
        sum_arr += arr[end]
        end += 1

    if sum_arr == M:
        cnt += 1

print(cnt)