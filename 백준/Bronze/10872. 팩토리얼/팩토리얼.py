N = int(input())
res = 1

if N < 2:
    print(1)
else:
    for i in range(N, 0, -1):
        res *= i

    print(res)