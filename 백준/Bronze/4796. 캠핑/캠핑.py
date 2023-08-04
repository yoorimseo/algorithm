i = 1

while True:
    L, P, V = list(map(int, input().split()))

    if L + P + V == 0:
        break

    days = int(V / P) * L
    days += min(V % P, L)

    print(f'Case {i}: {days}')

    i += 1