from collections import deque

def bfs(n):
    q = deque()
    q.append(n)

    while q:
        cur = q.popleft()

        if cur == K:
            return visited[cur]

        for i in (cur+1, cur-1, cur * 2):
            if 0 <= i <= MAX and not visited[i]:
              visited[i] = visited[cur] + 1
              q.append(i)

N, K = map(int, input().split())
MAX = 10 ** 5
visited = [0] * (MAX + 1)

print(bfs(N))