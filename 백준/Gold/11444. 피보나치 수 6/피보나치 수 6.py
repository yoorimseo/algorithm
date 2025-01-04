n = int(input())

def matrix_multiplication(a, b):
    n = len(a)
    mod = 1000000007
    c = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += (a[i][k] * b[k][j]) % mod
            c[i][j] %= mod

    return c

def fibonacci(n):
    if n <= 1:
        return n

    ans = [[1, 0], [0, 1]]
    a = [[1, 1], [1, 0]]

    while n > 0:
        if n % 2 == 1:
            ans = matrix_multiplication(ans, a)
        a = matrix_multiplication(a, a)
        n //= 2

    return ans[0][1]

print(fibonacci(n))