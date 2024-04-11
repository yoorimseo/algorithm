N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
arr = []

def dfs(n):
    if len(arr) == M:
        print(*arr)
        return

    for i in num:
        if i not in arr:
            arr.append(i)
            dfs(i)
            arr.pop()

dfs(min(num))