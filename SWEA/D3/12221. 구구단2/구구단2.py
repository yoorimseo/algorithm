T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    res = 0
    if A >= 10 or B >= 10:
        res = -1
    else:
        res = A * B

    print(f'#{i+1} {res}')