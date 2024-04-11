N, M = map(int, input().split())
arr = []

def dfs(n):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(n, N+1):
        arr.append(i)
        dfs(n)
        arr.pop()

dfs(1)