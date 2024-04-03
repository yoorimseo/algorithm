N, K = map(int, input().split())
A = list(map(int, input().split()))
visited = [False] * N
res = 0

def dfs(n, weight):
    global res

    if weight < 500:
        return

    if n == N:
        res += 1
        return

    weight -= K

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(n+1, weight + A[i])
            visited[i] = False

dfs(0, 500)
print(res)