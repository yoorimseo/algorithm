T = int(input())

for _ in range(T):
    n = int(input())

    for (idx, i) in enumerate(bin(n)[2:][::-1]):
        if i == '1':
            print(idx, end=' ')