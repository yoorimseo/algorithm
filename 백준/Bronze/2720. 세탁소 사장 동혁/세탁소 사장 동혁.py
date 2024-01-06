T = int(input())

for _ in range(T):
    price = int(input())
    q = 0
    d = 0
    n = 0
    p = 0

    while price > 0:
        if price >= 25:
            q += price // 25
            price %= 25
        elif price >= 10:
            d += price // 10
            price %= 10
        elif price >= 5:
            n += price // 5
            price %= 5
        elif price >= 1:
            p += price // 1
            price %= 1

    print(q, d, n, p)