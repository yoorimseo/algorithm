from collections import deque

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append([i, j])

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y

        if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
            box[nx][ny] = box[x][y] + 1
            queue.append([nx, ny])

day = 0

for row in box:
    for i in row:
        if i == 0:
            print(-1)
            exit(0)

    day = max(day, max(row))

print(day - 1)