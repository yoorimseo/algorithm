T = int(input())
for i in range(T):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    res = [0] * 8
    for j in range(len(money)):
        if N // money[j] != 0:
            res[j] = N // money[j]
            N %= money[j]
    print(f'#{i+1}')
    print(*res)