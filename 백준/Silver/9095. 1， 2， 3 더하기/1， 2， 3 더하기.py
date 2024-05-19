T = int(input())
num = [1, 2, 3]

for _ in range(T):
    n = int(input())
    dp = [0] * (n+1)

    for i in range(1, n+1):
        if i < 3:
            dp[i] = i
        elif i == 3:
            dp[i] = 4
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[n])