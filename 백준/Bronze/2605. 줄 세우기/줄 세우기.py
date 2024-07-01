N = int(input())
arr = list(map(int, input().split()))
res = []

for i in range(N):
    res.insert(arr[i], i+1)

res.reverse()

print(*res)