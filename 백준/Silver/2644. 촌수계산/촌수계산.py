n = int(input())
A, B = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
res = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            res[i] = res[v] + 1
            dfs(i)

dfs(A)

if res[B] > 0:
    print(res[B])
else:
    print(-1)