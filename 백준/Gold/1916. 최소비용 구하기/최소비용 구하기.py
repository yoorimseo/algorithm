from heapq import heappop, heappush

N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    arr[u].append((v, w))

S, E = map(int, input().split())

INF = 10 ** 9
dist = [INF] * (N+1)

def dijkstra(s):
    visited = [False] * (N+1)
    q = [(0, s)]
    dist[s] = 0

    while q:
        d, v = heappop(q)

        if visited[v]:
            continue

        visited[v] = True
        for i, nv in arr[v]:
            distance = d + nv
            if distance < dist[i]:
                dist[i] = distance
                heappush(q, (distance, i))

dijkstra(S)
print(dist[E])