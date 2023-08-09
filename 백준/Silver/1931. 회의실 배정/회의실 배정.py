N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr = sorted(arr, key = lambda x : [x[1], x[0]])
cnt = 0
start = 0

for i in arr:
    if i[0] >= start:
        start = i[1]
        cnt += 1

print(cnt)