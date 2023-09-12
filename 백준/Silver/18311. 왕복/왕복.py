n, k = map(int, input().split())
line = list(map(int, input().split()))
line = line + line[::-1]

for i in range(n * 2):
    k -= line[i]

    if k < 0:
        if i > n:
            print((n*2) - i)
            break
        else:
            print(i + 1)
            break