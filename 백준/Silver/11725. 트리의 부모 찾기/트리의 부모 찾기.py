import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [0] * (N+1)

def dfs(v):
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = v
            dfs(i)

dfs(1)

for i in range(2, N+1):
    print(visited[i])