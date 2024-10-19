T = int(input())

for _ in range(T):
    N = int(input())
    reverse_N = int(str(N)[::-1])
    res = N + reverse_N

    if res == int(str(res)[::-1]):
        print('YES')
    else:
        print('NO')