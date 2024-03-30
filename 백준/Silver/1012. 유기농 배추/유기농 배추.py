from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())

def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nX, nY = x+dx[i], y+dy[i]
            if 0 <= nX < h and 0 <= nY < w and graph[nX][nY] == 1:
                graph[nX][nY] = 0
                queue.append((nX, nY))

for _ in range(T):
    w, h, k = map(int, input().split())
    graph = [[0] * w for _ in range(h)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    cnt = 0

    for i in range(w):
        for j in range(h):
            if graph[j][i] == 1:
                bfs(graph, j, i)
                cnt += 1

    print(cnt)