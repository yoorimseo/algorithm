N, M = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(M):
    arr.sort()
    x = arr[0]
    y = arr[1]

    arr[0] = x + y
    arr[1] = x + y

print(sum(arr))