N = int(input())
rank = sorted([int(input()) for _ in range(N)])
res = 0

for i in range(1, N+1):
    res += abs(i - rank[i-1])

print(res)