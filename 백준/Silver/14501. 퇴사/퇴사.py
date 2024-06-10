N = int(input())
schedule = []
for _ in range(N):
    T, P = map(int, input().split())
    schedule.append((T, P))

dp = [0] * (N + 1)

for i in range(N-1, -1, -1):
    time = schedule[i][0]
    profit = schedule[i][1]

    if i + time <= N:
        dp[i] = max(dp[i+1], profit + dp[i + time])
    else:
        dp[i] = dp[i+1]

print(dp[0])