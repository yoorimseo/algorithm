N = int(input())
graph = [[] for _ in range(N+1)]
res = []

for i in range(1, N+1):
    v = int(input())
    graph[v].append(i)

def dfs(start, n):
    visited[n] = True

    for g in graph[n]:
        if not visited[g]:
            dfs(start, g)
        elif start == g:
            res.append(start)
            return

for i in range(1, N+1):
    visited = [False] * (N+1)
    dfs(i, i)

res.sort()
print(len(res))
print(*res, sep='\n')