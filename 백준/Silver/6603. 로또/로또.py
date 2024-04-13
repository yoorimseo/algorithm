def dfs(depth, start):
    if depth == 6:
        print(*res)
        return

    for i in range(start, k):
        res.append(S[i])
        dfs(depth+1, i+1)
        res.pop()

while True:
    inp = list(map(int, input().split()))
    k = inp[0]
    S = inp[1:]
    res = []

    dfs(0, 0)

    if not k:
        break

    print()