T = int(input())

for i in range(T):
    N = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0

    while N != 1:
        if N % 11 == 0:
            N //= 11
            e += 1
        elif N % 7 == 0:
            N //= 7
            d += 1
        elif N % 5 == 0:
            N //= 5
            c += 1
        elif N % 3 == 0:
            N //= 3
            b += 1
        elif N % 2 == 0:
            N //= 2
            a += 1

    print(f'#{i+1}', a, b, c, d, e)