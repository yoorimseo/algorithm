n = int(input())
m = int(input())
computers = [[] for _ in range(n+1)]
visited = [False] * (n+1)
res = []

for _ in range(m):
    x, y = map(int, input().split())
    computers[x].append(y)
    computers[y].append(x)

def dfs(v):
    visited[v] = True
    if v != 1:
        res.append(v)

    for i in computers[v]:
        if visited[i] == False:
            dfs(i)

dfs(1)

print(len(res))
