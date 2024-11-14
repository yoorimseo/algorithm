T = int(input())

for _ in range(T):
    arr = input().split()
    res = []

    for i in arr:
        res.append(i[::-1])

    print(*res)