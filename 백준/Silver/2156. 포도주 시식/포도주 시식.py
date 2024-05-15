import sys
sys.setrecursionlimit(10**5)

N = int(input())

wine = []
for _ in range(N):
    wine.append(int(input()))

memo = [0] * N
memo[0] = wine[0]

if 1 < N:
    memo[1] = wine[0] + wine[1]
if 2 < N:
    memo[2] = max(memo[1], max(wine[0], wine[1]) + wine[2])

for i in range(3, N):
    case1 = memo[i - 1]
    case2 = memo[i - 2] + wine[i]
    case3 = memo[i - 3] + wine[i - 1] + wine[i]
    memo[i] = max(case1, case2, case3)

print(memo[N-1])