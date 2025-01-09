N = int(input())
dasom = int(input())
votes = sorted([int(input()) for _ in range(N-1)], reverse=True)

res = 0

if N == 1:
    print(0)
else:
    while votes[0] >= dasom:
        votes[0] -= 1
        dasom += 1
        res += 1

        votes.sort(reverse=True)

    print(res)