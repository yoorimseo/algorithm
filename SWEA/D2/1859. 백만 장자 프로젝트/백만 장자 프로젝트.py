T = int(input())

for i in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    max_price = 0
    res = 0

    for p in price[::-1]:
        if p >= max_price:
            max_price = p
        else:
            res += max_price - p

    print(f'#{i} {res}')