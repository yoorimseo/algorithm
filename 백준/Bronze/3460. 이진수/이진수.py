T = int(input())

for _ in range(T):
    n = int(input())
    b = format(n, 'b')
    for i in range(len(b)):
        if b[::-1][i] == '1':
            print(i, end=' ')