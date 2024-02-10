T = int(input())

for i in range(T):
    L, U, X = map(int, input().split())
    res = 0
    if X < L:
        res = L - X
    elif X > U:
        res = -1

    print(f'#{i+1} {res}')