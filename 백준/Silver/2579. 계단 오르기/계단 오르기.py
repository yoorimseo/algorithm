N = int(input())
scores = [int(input()) for _ in range(N)]
dp = [0] * N
dp[0] = scores[0]

if N >= 2:
    dp[1] = scores[0] + scores[1]

for i in range(2, N):
    dp[i] = max(dp[i-3] + scores[i-1] + scores[i], dp[i-2] + scores[i])

print(dp[N-1])