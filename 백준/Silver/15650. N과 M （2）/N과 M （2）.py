from itertools import combinations

N, M = map(int, input().split())
arr = list(range(1, N+1))
res = list(combinations(arr, M))

for i in res:
    print(*i)