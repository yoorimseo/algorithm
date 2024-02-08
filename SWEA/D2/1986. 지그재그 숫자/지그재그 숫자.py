T = int(input())

for i in range(1, T+1):
    N = int(input())
    res = 1
    for j in range(2, N+1):
        if j % 2 == 0:
            res -= j
        else:
            res += j

    print(f'#{i} {res}')