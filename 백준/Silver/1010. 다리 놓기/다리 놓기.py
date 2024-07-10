T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    a = max(n, m)
    b = min(n, m)

    x, y, z = 1, 1, 1

    for i in range(1, a+1):
        x *= i

    for j in range(1, b+1):
        y *= j

    for k in range(1, a-b+1):
        z *= k

    print(x // (y * z))