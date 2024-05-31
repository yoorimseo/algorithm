from heapq import heappop, heappush

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
degree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    degree[b] += 1

def topolrogical_sort():
    que = []
    for i in range(1, N + 1):
        if degree[i] == 0:
            heappush(que, i)

    ans = []
    while que:
        idx = heappop(que)
        ans.append(idx)

        for a in arr[idx]:
            degree[a] -= 1
            if degree[a] == 0:
                heappush(que, a)

    print(*ans)

topolrogical_sort()