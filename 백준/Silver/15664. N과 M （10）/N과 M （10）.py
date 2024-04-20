N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False] * N
res = []

def dfs(start):
    if len(res) == M:
        print(*res)
        return

    temp = 0

    for i in range(start, N):
        if not visited[i] and temp != arr[i]:
            visited[i] = True
            res.append(arr[i])
            temp = arr[i]
            dfs(i + 1)
            visited[i] = False
            res.pop()

dfs(0)