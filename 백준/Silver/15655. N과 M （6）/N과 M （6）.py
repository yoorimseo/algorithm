N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
res = []

def dfs(start):
    if len(res) == M:
        print(*res)
        return

    for i in range(start, N):
        if arr[i] not in res:
            res.append(arr[i])
            dfs(i+1)
            res.pop()

dfs(0)