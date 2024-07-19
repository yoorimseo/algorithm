n = int(input())
dp = [0] * (n+1)
dp[1] = 1

def fibo(n):
    if n < 2:
        return n

    if dp[n]:
        return dp[n]

    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]

fibo(n)
res = (dp[n] * 2 + dp[n-1]) * 2

print(res)