from collections import deque

N, K = map(int, input().split())
MAX = 10 ** 5
visited = [0] * (MAX + 1)
cnt, res = 0, 0

def bfs(n):
    global res
    global cnt

    q = deque()
    q.append(n)

    while q:
        cur = q.popleft()

        if cur == K:
            res = visited[cur]
            cnt += 1
            continue

        for i in (cur+1, cur-1, cur * 2):
            if 0 <= i <= MAX and (visited[i] == 0 or visited[i] >= visited[cur] + 1):
              visited[i] = visited[cur] + 1
              q.append(i)

bfs(N)
print(res, cnt, sep='\n')