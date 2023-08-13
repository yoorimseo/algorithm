T = int(input())

for _ in range(T):
    x, y = input().split()
    x = int(x, 2)
    y = int(y, 2)
    res = format(x + y, 'b')

    print(res)