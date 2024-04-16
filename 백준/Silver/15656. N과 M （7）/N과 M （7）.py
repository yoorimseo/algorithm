N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
res = []

def dfs():
    if len(res) == M:
        print(*res)
        return

    for i in arr:
        res.append(i)
        dfs()
        res.pop()

dfs()