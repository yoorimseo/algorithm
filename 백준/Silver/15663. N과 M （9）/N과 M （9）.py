N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
res = []
visited = [False] * N

def dfs():
    temp = 0

    if len(res) == M:
        print(*res)
        return

    for i in range(N):
        if not visited[i] and temp != arr[i]:
            res.append(arr[i])
            visited[i] = True
            temp = arr[i]
            dfs()
            res.pop()
            visited[i] = False

dfs()