T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    res = A + B

    if res >= 24:
        res -= 24

    print(f'#{i+1} {res}')