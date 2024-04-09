from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))
res = 0

for i in range(1, N+1):
    temp = list(combinations(arr, i))
    for j in temp:
        if sum(j) == S:
            res += 1

print(res)