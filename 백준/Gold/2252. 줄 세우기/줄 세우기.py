N, M = map(int, input().split())

arr = [[] for _ in range(N + 1)]
degree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    degree[b] += 1

from collections import deque

def topological_sort():
    que = deque()
    ans = []
    for i in range(1, N + 1):
        if degree[i] == 0:
            que.append(i)

    while que:
        idx = que.popleft()
        ans.append(idx)

        for a in arr[idx]:
            degree[a] -= 1
            if degree[a] == 0:
                que.append(a)
    print(*ans)

topological_sort()