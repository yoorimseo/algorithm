from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, ''.join(input().split()))) for _ in range(N)]
queue = deque([(0, 0)])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nX, nY = x+dx[i], y+dy[i]

        if 0 <= nX < N and 0 <= nY < M:
            if maze[nX][nY] == 1:
                queue.append((nX, nY))
                maze[nX][nY] = maze[x][y] + 1
print(maze[N-1][M-1])