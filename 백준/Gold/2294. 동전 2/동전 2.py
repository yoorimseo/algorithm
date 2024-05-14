N, K = map(int, input().split())
MAX = float("INF")

coin = []
for _ in range(N):
    coin.append(int(input()))

memo = [MAX] * (K+1)
memo[0] = 0

for n in range(N):        
    for k in range(coin[n], K+1):
        prev_k = k - coin[n]
        case1 = MAX
        if 0 <= prev_k:
            case1 = memo[prev_k] + 1
        case2 = memo[k]
        memo[k] = min(case1, case2)

if memo[K] == MAX:
    print(-1)
else:
    print(memo[K])