N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
arr = []

def dfs(start):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(start, N):
        arr.append(num[i])
        dfs(i)
        arr.pop()

dfs(0)