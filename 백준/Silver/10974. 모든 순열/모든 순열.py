N = int(input())
res = []

def dfs():
    if len(res) == N:
        print(*res)
        return

    for i in range(1, N+1):
        if i not in res:
            res.append(i)
            dfs()
            res.pop()

dfs()