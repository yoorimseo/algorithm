T = int(input())

for i in range(T):
    P, Q = map(int, input().split())
    x, y = 0, 1

    for j in range(1, P+1):
        x, y = y, x+y

    print(f'Case #{i+1}: {x % Q}')