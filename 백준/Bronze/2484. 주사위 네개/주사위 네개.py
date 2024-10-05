N = int(input())
res = 0

for _ in range(N):
    dice = list(map(int, input().split()))
    check = dict()

    for i in dice:
        if i not in check:
            check[i] = 1
        else:
            check[i] += 1

    check = sorted(list(check.items()), key=lambda x: (x[1], x[0]), reverse=True)
    temp = 0

    if check[0][1] == 4:
        temp = 50000 + (check[0][0] * 5000)
    elif check[0][1] == 3:
        temp = 10000 + (check[0][0] * 1000)
    elif check[0][1] == 2:
        if check[1][1] == 2:
            temp = 2000 + (check[0][0] * 500) + (check[1][0] * 500)
        else:
            temp = 1000 + (check[0][0] * 100)
    else:
        temp = max(dice) * 100

    res = max(res, temp)

print(res)