N, M = map(int, input().split())
arr = []
for _ in range(N):
    item = list(map(int, input().split()))
    arr.append(item)

K = int(input())

for _ in range(K):
    res = 0
    i, j, x, y = map(int, input().split())

    for a in range(i-1, x):
        for b in range(j-1, y):
            res += arr[a][b]

    print(res)