N = int(input())
arr = []

di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)


def dfs(i, j):
    visited[i][j] = True
    cnt = 1

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == '1' and not visited[ni][nj]:
            cnt += dfs(ni, nj)

    return cnt

for _ in range(N):
    row = list(input())
    arr.append(row)

visited = [ [False] * N for _ in range(N) ]
result = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and not visited[i][j]:
            cnt = dfs(i, j)
            result.append(cnt)

print(len(result))
for i in sorted(result):
    print(i)