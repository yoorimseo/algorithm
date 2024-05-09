N = int(input())
MOD = 10007
res = [0 for _ in range(N+1)]

def F(n):
    if n <= 2:
        return n

    if res[n] > 0:
        return res[n]

    res[n] = F(n-1) + F(n-2)
    res[n] %= MOD
    return res[n]

print(F(N))