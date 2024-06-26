N = int(input())
arr = list(map(int, input().split()))
line = list(range(1, N+1))
res = []

for i in range(-1, -N-1, -1):
    res.insert(arr[i], line[i])

print(*res)