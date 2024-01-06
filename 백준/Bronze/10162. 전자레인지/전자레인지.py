T = int(input())

if T % 10 != 0 and T % 10 < 10:
    print(-1)
else:
    A = 0
    B = 0
    C = 0

    while T != 0:
        if T >= 300:
            A += T // 300
            T %= 300
        elif T >= 60:
            B += T // 60
            T %= 60
        elif T >= 10:
            C += T // 10
            T %= 10
    print(A, B, C)